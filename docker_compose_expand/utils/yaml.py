import io

import oyaml as yaml


def load_content(content):
    return yaml.load(content)


def read_file(filepath):
    with io.open(filepath, "r", encoding="utf8") as f:
        return load_content(f)


def write_file(filepath, content=""):
    with io.open(filepath, "w", encoding="utf8") as f:
        yaml.dump(content, f, default_flow_style=False)
