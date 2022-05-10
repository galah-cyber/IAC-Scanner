import subprocess
from .arguments import Arguments
from .scanners import Scanners

class ScannerRunner:

    @staticmethod
    def __build_checkov(arguments: Arguments):
        
        command = ["checkov", "-o", "json"]

        if arguments.inputFile:
            command.append("--file")
            command.append(arguments.inputFile)
        else:
            command.append("--directory")
            command.append(arguments.directory)
            
        if arguments.quiet:
            command.append("--quiet")

        return command

    @staticmethod
    def __build_tflint(arguments: Arguments):
        command = ["tflint", "--format", "json"]
        
        if arguments.inputFile:
            command.append(arguments.inputFile)
        else:
            command.append(arguments.directory)
            
        return command
    
    @staticmethod
    def __build_tfsec(arguments: Arguments):
        command = ["tfsec"]

        if arguments.inputFile:
            raise Exception("tfsec does not support scanning individual files")
        else:
            command.append(arguments.directory)

        command.append('--format')
        command.append("json")

        return command

    @staticmethod
    def run_scanner(arguments: Arguments, tool: str):

        try:
            selectedTool = Scanners[tool.upper()]
            command = []

            if selectedTool == Scanners.TFLINT:
                command = ScannerRunner.__build_tflint(arguments)
            elif selectedTool == Scanners.TFSEC:
                command = ScannerRunner.__build_tfsec(arguments)
            elif selectedTool == Scanners.CHECKOV:
                command = ScannerRunner.__build_checkov(arguments)

            if arguments.toFile:
                return subprocess.run(command, stdout=subprocess.PIPE)
            else:
                return subprocess.run(command)

        except FileNotFoundError:
            print(f"Can not run {tool}. Make sure it is properly installed")
        except KeyError:
            print(f"{tool} is not supported.")
        except Exception as e:
            print(e)

