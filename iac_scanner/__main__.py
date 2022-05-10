from .arguments import Arguments
from .scanner_runner import ScannerRunner
import time

def create_file(result, tool):
    if result is not None:
        f = open(f"{tool}-{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.json", "a")
        f.write(result.stdout.decode('utf-8'))

arguments = Arguments()

for tool in arguments.tools:
    try:
        result = ScannerRunner.run_scanner(arguments, tool)
        if arguments.toFile:
            create_file(result, tool)

    except Exception as e:
        print (e)

