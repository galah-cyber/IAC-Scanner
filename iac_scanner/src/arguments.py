import argparse

class Arguments:
    config = None

    def __init__(self):
        parser = argparse.ArgumentParser(description="CLI tool to run IAC security scanners", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument("-t", "--tool", default="checkov", help="Tool to run (Checkov, TFLint, tfsec)")
        parser.add_argument("-d", "--directory", default="./", help="Directory to read files from")
        parser.add_argument("-i", "--input", help="Individual file to scan")
        parser.add_argument("-f", "--format", default="CLI", help="Format of output (CLI, JSON)")
        parser.add_argument("-o", "--output", default="", help="Directory to output files to")
        parser.add_argument('--loud', action=argparse.BooleanOptionalAction, help="Show passed checks")

        args = parser.parse_args()   
        self.config = vars(args)

    @property
    def directory(self):
        return self.config["directory"]

    @property
    def format(self):
        return self.config["format"].upper()

    @property
    def inputFile(self):
        return self.config["input"]

    @property
    def toFile(self):
        return self.config["toFile"]

    @property
    def output(self):
        return self.config["output"]

    @property
    def tool(self):
        return self.config["tool"].upper()

    @property
    def loud(self):
        return self.config["loud"]

