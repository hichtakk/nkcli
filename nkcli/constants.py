COLOR = {
    "bay": "鹿毛",
    "dark bay": "黒鹿毛",
    "brown": "青鹿毛",
    "black": "青毛",
    "chestnut": "栗毛",
    "liver chestnut": "栃栗毛",
    "gray": "芦毛",
    "white": "白毛"
}

SEX = {
    "stallion": "牡",
    "mare": "牝",
    "gelding": "セ"
}


def get_en_color(ja_color):
    if ja_color == None:
        return "unknown"
    color = [e for e, j in COLOR.items() if j == ja_color][0]
    return color


def get_en_sex(ja_sex):
    color = [e for e, j in SEX.items() if j == ja_sex][0]
    return color