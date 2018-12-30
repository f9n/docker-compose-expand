from jinja2 import Template

from .yaml import load_content


def render(content, item):
    tm = Template(str(content))
    msg = tm.render(**item)
    msg_object = load_content(msg)
    return msg_object
