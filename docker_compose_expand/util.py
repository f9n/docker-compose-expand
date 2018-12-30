import io

import oyaml as yaml


def load_yaml_content(content):
    return yaml.load(content)


def read_yaml_file(filepath):
    with io.open(filepath, "r", encoding="utf8") as f:
        return load_yaml_content(f)


def write_yaml_file(filepath, content=""):
    with io.open(filepath, "w", encoding="utf8") as f:
        yaml.dump(content, f, default_flow_style=False)

