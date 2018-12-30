from .core import DockerComposeExpand


def main():
    tool = DockerComposeExpand()
    tool.load()
    tool.generate()
    tool.save()
    tool.run()


if __name__ == "__main__":
    main()

