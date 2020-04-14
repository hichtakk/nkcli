import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

from nkcli.horse import Horse, Pedigree
from nkcli.constants import get_en_color, get_en_sex


class Scraper(object):

    def send_request(self, url):
        req = Request(url)
        body = None
        try:
            response = urlopen(req)
            body = response.read()
        except HTTPError as e:
            # error code
            print(e)
        except URLError as e:
            print(e)
        return body


    def get_horse(self, horse_id):
        url = "https://db.netkeiba.com/horse/{}".format(horse_id)
        html = self.send_request(url)
        soup = BeautifulSoup(html, features="lxml")
        #name = soup.find("div", class_="horse_title").h1.text
        name = soup.find("title").text.split("|")[0].strip()
        attributes = soup.find("div", class_="horse_title").find("p", class_="txt_01")
        label = attributes.find("span")
        if label != None:
            label.decompose()
        attributes = attributes.text.split()
        status = None
        sex = None
        color = None
        if len(attributes) == 3:
            # list consist of STATUS, SEX-AGE and COLOR
            status = attributes[0]
            sex = attributes[1]
            m = re.search(r"^.(?P<age>\d+.*)", sex)
            if m != None:
                sex = re.sub(m.groups(0)[0], "", sex)
            color = attributes[2]
        elif len(attributes) == 2:
            # list consist of SEX and COLOR
            sex = attributes[0]
            color = attributes[1]
        elif len(attributes) == 1:
            # list consist of SEX
            sex = attributes[0]
        profile = soup.find("div", class_="db_prof_area_02")
        foaled = profile.find("th", text="生年月日").parent.find("td").text.strip()
        m = re.search(r"^(?P<year>\d{4}).*", foaled)
        foaled = int(m.group("year"))
        record = profile.find("th", text="通算成績").parent.find("td").find("a").text
        earnings = profile.find("th", text="獲得賞金").parent.find("td").text.strip()

        horse = Horse(horse_id)
        horse.name = name
        if sex != None:
            horse.sex = get_en_sex(sex)
        horse.color = get_en_color(color)
        horse.foaled = foaled
        horse.record = record
        horse.earnings = earnings
        if status == "現役":
            horse.retired = False

        return horse


    def get_pedigree(self, horse_id):
        url = "https://db.netkeiba.com/horse/ped/{}".format(horse_id)
        html = self.send_request(url)
        soup = BeautifulSoup(html, features="lxml")
        pedigree = soup.find("table", class_="blood_table")
        sire = pedigree.find("td", rowspan=16, class_="b_ml")
        dam =  pedigree.find("td", rowspan=16, class_="b_fml")
        if sire.text.strip() != "":
            sire_name = sire.a.text.strip()
            sire_id = sire.a.get("href").strip("/").lstrip("horse/")
        else:
            sire_name = ""
            sire_id = ""
    
        if dam.text.strip() != "":
            dam_name = dam.a.text.strip()
            dam_id = dam.a.get("href").strip("/").lstrip("horse/")
        else:
            dam_name = ""
            dam_id = ""

        sire_name_list = sire_name.split("\n")
        sire_name_ja = sire_name_list[0]
        if len(sire_name_list) == 1:
            sire_name_en = ""
        else:
            sire_name_en = re.sub(r"\(.*\)", "", sire_name_list[1])

        dam_name_list = dam_name.split("\n")
        dam_name_ja = dam_name_list[0]
        if len(dam_name_list) == 1:
            dam_name_en = ""
        else:
            dam_name_en = re.sub(r"\(.*\)", "", dam_name_list[1])
        sire_dict = {"id": sire_id, "name": sire_name_ja, "international_name": sire_name_en}
        dam_dict = {"id": dam_id, "name": dam_name_ja, "international_name": dam_name_en}
        pedigree = Pedigree(sire_dict, dam_dict)

        return pedigree

    def user_favorite(self, user_id):
        url = "https://user.netkeiba.com/?pid=user_horse&id={}".format(user_id)
        html = self.send_request(url)
        soup = BeautifulSoup(html, features="lxml")
        favorites = soup.find("div", class_="fav_horse_box").find("table").find_all("tr")
        for favorite in favorites[1:]:
            print(favorite.find("td", class_="horse_name_cell").text.strip())


    def cookie_to_id(self, cookie):
        url = "https://user.netkeiba.com"
        req = Request(url, None, {"Cookie": "netkeiba={}".format(cookie)})
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, features="lxml")
        avator = soup.find("div", class_="prof_box_left_01").find("img")
        user_id = avator.get("src").split("/")[-2]

        return user_id