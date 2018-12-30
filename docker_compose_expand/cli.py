import subprocess
import sys

from . import __version__


def main():
    subprocess.call(["docker-compose", *sys.argv[1:]])
    sys.exit(0)


if __name__ == "__main__":
    main()

