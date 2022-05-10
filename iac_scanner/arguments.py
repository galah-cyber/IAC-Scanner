import argparse

class Arguments:
    config = None

    def __init__(self):
        parser = argparse.ArgumentParser(description="CLI tool to run IAC security scanners", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument("-t", "--tools", nargs='*', required=True, help="Tools to run (Checkov, TFLint, tfsec)")
        parser.add_argument("-d", "--directory", default="./", help="Directory to read files from")
        parser.add_argument("-f", "--file", default="", help="Individual file to scan")
        parser.add_argument("-o", "--output", default="./", help="Directory to output files to")
        parser.add_argument('--quiet', action=argparse.BooleanOptionalAction, help="Only retrieve results for failed checks")
        parser.add_argument("--toFile", action=argparse.BooleanOptionalAction, help="Output to file")

        args = parser.parse_args()   
        self.config = vars(args)

    @property
    def directory(self):
        return self.config["directory"]

    @property
    def inputFile(self):
        return self.config["file"]

    @property
    def toFile(self):
        return self.config["toFile"]

    @property
    def output(self):
        return self.config["output"]

    @property
    def tools(self):
        return self.config["tools"]

    @property
    def quiet(self):
        return self.config["quiet"]

