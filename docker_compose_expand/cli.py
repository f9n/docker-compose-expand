import subprocess
import sys

from . import __version__
from .util import read_yaml_file, write_yaml_file


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ["version"]:
        print("docker-compose-expand version {}".format(__version__))

    subprocess.call(["docker-compose", *sys.argv[1:]])
    sys.exit(0)


if __name__ == "__main__":
    main()

