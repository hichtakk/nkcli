import toml

def read_conf(path=""):
    with open(path) as fd:
        parsed_toml = toml.loads(fd.read())
    return parsed_toml