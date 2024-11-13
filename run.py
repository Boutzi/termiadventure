import sys
import subprocess

_type = sys.argv[1]
_out = sys.argv[2]
_shell = ""

match _type:
    case "dev":
        match _out:
            case "0":
                _shell = "python main.py " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5]
            case "1":
                _shell = "start cmd /c python main.py " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5]
    case "prod":
        match _out:
            case "0":
                _shell = "python main.py"
            case "1":
                _shell = "start cmd /c python main.py"

subprocess.call(_shell, shell=True)