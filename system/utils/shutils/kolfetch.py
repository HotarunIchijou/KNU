from cpuinfo import get_cpu_info
from psutil import virtual_memory
from socket import gethostname
import system.utils.logtosys

def fetch():
    CPU = get_cpu_info()["brand_raw"]
    RAM = int(virtual_memory().total / (1024 ** 2))
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠚⠛⠛⠉⠉⠛⠛⠓⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀      '''  + system.utils.logtosys.logintosys.login + '|' + gethostname() + '''
⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⠀⠀⠀⠀⠀      ''' + 'OS: KNU/KolotovkinOS v 1.6.1 (KolotovkinOS 2.0 coming soon)' + '''
⠀⠀⠀⣠⠞⣡⠞⠉⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠉⠳⣌⠳⣄⠀⠀⠀      ''' + 'SH: Kosh v 1.7' + '''
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
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠚⠛⠛⠉⠉⠛⠛⠓⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
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
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠦⣤⣤⣤⣤⣤⣤⠴⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀

''' +
system.utils.logtosys.logintosys.login + '|' + gethostname() +
                  '\nOS: KNU/KolotovkinOS v 1.6.1 mobile\n(KolotovkinOS 2.0 coming soon)'
                  '\nSH: Kosh v 1.7'
                  '\nCPU: ' + CPU +
                  '\nRAM: ' + str(RAM) + 'Мб')
