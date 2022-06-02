from distutils import extension
from src.arguments import Arguments
from src.scanner_runner import ScannerRunner
import time

def create_file(result, arguments):
    extension = "txt"
    if arguments.format == "JSON":
        extension = "json"
    f = open(f"{arguments.output}/{arguments.tool}-{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.{extension}", "a")
    f.write(result.stdout.decode('utf-8'))

arguments = Arguments()

try:
    result = ScannerRunner.run_scanner(arguments)
    if result is not None:
        if arguments.output:
            file = create_file(result, arguments)

except Exception as e:
    print (e)

