import subprocess
import sys

from . import __version__
from .utils import yaml, template


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
        for defined_expandable_service in self.defined_expandable_services:
            expanded_services = self.__generate_expandable_services(
                name_field=defined_expandable_service["name"],
                service_field=defined_expandable_service["service"],
                loop_field=defined_expandable_service["loop"],
            )
            for service in expanded_services:
                self.real_services.update(service)

    def __generate_service(self, name, service, item):
        _name = template.render(name, item)
        _new_service = template.render(service, item)
        return {_name: _new_service}

    def __generate_services(self, variables, name_field, service_field):
        _services = []
        for item in variables:
            _new_service_object = self.__generate_service(
                name_field, service_field, item
            )
            _services.append(_new_service_object)

        return _services

    def __generate_expandable_services(self, name_field, service_field, loop_field):
        expanded_loop_field = loop_field
        if isinstance(loop_field, str):
            expanded_loop_field = template.render(loop_field, self.variables)
        elif isinstance(loop_field, list):
            pass

        return self.__generate_services(expanded_loop_field, name_field, service_field)

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
