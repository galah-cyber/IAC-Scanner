# IAC-Scanner

A python wrapper for Checkov, TFLint, and tfsec

# Installation

This project is not currently available from the Python Package Index.  

To install, navigate your terminal to the projects root directory and run
```
pip install .
```
To just run, navigate your terminal to the projects root directory and run
```
python -m IACScanner
```

# Usage

```
IACScanner
```

Default behaviour is to run a scan on all files in the current directory through the Checkov scanner. 
With results for failing tests displayed in the console window 

```
optional arguments:
  -h, --help            show this help message and exit
  -t TOOL, --tool TOOL  Tool to run (Checkov, TFLint, tfsec) (default: checkov)
  -d DIRECTORY, --directory DIRECTORY
                        Directory to read files from (default: ./)
  -i INPUT, --input INPUT
                        Individual file to scan (default: None)
  -f FORMAT, --format FORMAT
                        Format of output (CLI, JSON) (default: CLI)
  -o OUTPUT, --output OUTPUT
                        Directory to output files to. If none output to screen
  --loud, --no-loud     Show passed checks and full output
  ```
