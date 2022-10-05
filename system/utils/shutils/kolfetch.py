from cpuinfo import get_cpu_info
from psutil import virtual_memory
from socket import gethostname
import system.utils.logtosys
import system.utils.devtools.changever

def fetch():
    CPU = get_cpu_info()["brand_raw"]
    RAM = int(virtual_memory().total / (1024 ** 2))
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠚⠛⠛⠛⠛⠛⠛⠓⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀      '''  + system.utils.logtosys.logintosys.login + '|' + gethostname() + '''
⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⠀⠀⠀⠀⠀      ''' + 'OS: KNU/KolotovkinOS v ' + system.utils.devtools.changever.osv + ' (KolotovkinOS 2.0 coming soon)' + '''
⠀⠀⠀⣠⠞⣡⠞⠉⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠉⠳⣌⠳⣄⠀⠀⠀      ''' + 'SH: Kosh v ' + system.utils.devtools.changever.shv + '''
⠀⠀⡼⠃⠀⡇⠀⣤⣀⠀⣹⠀⠀⠀⠀⠀⠀⠀⠀⣏⠀⢠⣄⡀⢸⠀⠙⣧⠀⠀      ''' +  'CPU: ' + CPU + '''
⠀⡼⠁⠀⠀⠙⠒⠛⠛⠒⠋⠀⠀⠀⢀⡀⠀⠀⠀⠙⠒⠚⠛⠒⠋⠀⠀⠈⣧⠀      '''  + 'RAM: ' + str(RAM) + 'Мб' + '''
⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⠋⠙⣧⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣟⠀⠀⢻⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠿⠯⣙⢿⡀⣠⡤⣄⠀⠀⠀⠀⠀⠀⠀⠀⣽
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠈⢦⡟⠁⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⣿
⢹⡄⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⢈⠇⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⢰⡇
⠀⢻⡀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠈⠀⠉⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀
⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⣿⠦⣄⣀⣀⣠⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⠀
⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠈⠓⠶⠶⠶⠖⠋⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠦⣤⣤⣤⣤⣤⣤⠴⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀''')

def mobfetch():
    CPU = get_cpu_info()["brand_raw"]
    RAM = int(virtual_memory().total / (1024 ** 2))
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠚⠛⠛⠛⠛⠛⠛⠓⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠞⣡⠞⠉⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠉⠳⣌⠳⣄⠀⠀⠀
⠀⠀⡼⠃⠀⡇⠀⣤⣀⠀⣹⠀⠀⠀⠀⠀⠀⠀⠀⣏⠀⢠⣄⡀⢸⠀⠙⣧⠀⠀
⠀⡼⠁⠀⠀⠙⠒⠛⠛⠒⠋⠀⠀⠀⢀⡀⠀⠀⠀⠙⠒⠚⠛⠒⠋⠀⠀⠈⣧⠀
⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⠋⠙⣧⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣟⠀⠀⢻⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠿⠯⣙⢿⡀⣠⡤⣄⠀⠀⠀⠀⠀⠀⠀⠀⣽
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠈⢦⡟⠁⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⣿
⢹⡄⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⢈⠇⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⢰⡇
⠀⢻⡀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠈⠀⠉⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀
⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⣿⠦⣄⣀⣀⣠⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⠀
⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠈⠓⠶⠶⠶⠖⠋⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠦⣤⣤⣤⣤⣤⣤⠴⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀

''' +
system.utils.logtosys.logintosys.login + '|' + gethostname() +
                  '\nOS: KNU/KolotovkinOS v ' + system.utils.devtools.changever.osv + ' mobile\n(KolotovkinOS 2.0 coming soon)'
                  '\nSH: Kosh v ' + system.utils.devtools.changever.shv +
                  '\nCPU: ' + CPU +
                  '\nRAM: ' + str(RAM) + 'Мб')
