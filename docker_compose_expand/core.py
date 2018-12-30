import subprocess
import sys

from . import __version__
from .utils import yaml


class DockerComposeExpand:
    def __init__(
        self, input_file="docker-compose-expand.yml", output_file="docker-compose.yml"
    ):
        """ Create initial variables """
        self.input_file = input_file
        self.output_file = output_file
        self.version = ""
        self.real_services = dict()
        self.variables = ""

        self.defined_expandable_services = []

    def check():
        """ Check docker-compose-expand.yml file """
        pass

    def load(self):
        """ Load docker-compose-expand file """
        _content = yaml.read_file(self.input_file)
        _services = _content["services"]
        if _services is not None:
            self.real_services = _services

        self.version = _content["version"]
        self.variables = _content["expand"]["vars"]
        self.defined_expandable_services = _content["expand"]["services"]

    def reload():
        """ Reload docker-compose-expand.yml file """
        pass

    def generate(self):
        """ Generate services based on the expand field in the docker-compose-expand.yml file"""
        pass

    def save(self):
        """ Save the services to docker-compose.yml file """
        content = {"version": self.version, "services": self.real_services}
        yaml.write_file(filepath=self.output_file, content=content)

    def run(self):
        """ Run docker-compose tool"""
        if len(sys.argv) > 1 and sys.argv[1] in ["version"]:
            print("docker-compose-expand version {}".format(__version__))

        subprocess.call(["docker-compose", *sys.argv[1:]])
        sys.exit(0)
