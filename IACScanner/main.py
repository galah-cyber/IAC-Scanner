from distutils import extension
from .arguments import Arguments
from .scanner_runner import ScannerRunner
import time
import sys

__name__ = 'IACScanner'


def create_file(result, arguments):
    extension = "txt"
    if arguments.format == "JSON":
        extension = "json"
    f = open(f"{arguments.output}/{arguments.tool}-{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.{extension}", "a")
    f.write(result.stdout.decode('utf-8'))


def run():
    arguments = Arguments()

    try:
        result = ScannerRunner.run_scanner(arguments)
        if result is not None:
            if arguments.output:
                file = create_file(result, arguments)

    except Exception as e:
        print (e)

if __name__ == "__main__":
    sys.exit(run)


