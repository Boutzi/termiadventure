class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GREY = '\033[90m'
    LRED = '\033[91m'
    LGREEN = '\033[92m'
    LYELLOW = '\033[93m'
    LBLUE = '\033[94m'
    LMAGENTA = '\033[95m'
    LCYAN = '\033[96m'
    LGREY = '\033[97m'
    PURPLE = '\033[35m'
    ENDC = '\033[0m'

    def getColors(self, color):
        match color:
            case 'BLACK':
                return Colors.BLACK
            case 'RED':
                return Colors.RED
            case 'GREEN':
                return Colors.GREEN
            case 'YELLOW':
                return Colors.YELLOW
            case 'BLUE':
                return Colors.BLUE
            case 'MAGENTA':
                return Colors.MAGENTA
            case 'CYAN':
                return Colors.CYAN
            case 'WHITE':
                return Colors.WHITE
            case 'GREY':
                return Colors.GREY
            case 'LRED':
                return Colors.LRED
            case 'LGREEN':
                return Colors.LGREEN
            case 'LYELLOW':
                return Colors.LYELLOW
            case 'LBLUE':
                return Colors.LBLUE
            case 'LMAGENTA':
                return Colors.LMAGENTA
            case 'LCYAN':
                return Colors.LCYAN
            case 'LGREY':
                return Colors.LGREY
            case _:
                return Colors.ENDC