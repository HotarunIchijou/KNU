from socket import gethostname
from time import sleep
import system.utils.logtosys
from system.utils.shutils import poweroff, wtime, about, help, usrcreate, kolfetch, notfound

def utils():
    var = system.utils.shutils
    return var

def kosh():
    while True:
        usrinp = input("[" + system.utils.logtosys.logintosys.login + "|" + gethostname() + "] ")

        if usrinp.isspace():
            pass

        match usrinp:
            case "off" | "poweroff" | "shutdown":
                print(utils().poweroff.shutdown.off())
                sleep(0.8)
                break
            case "whatstime" | "wtime":
                print(utils().wtime.time.wtime())
            case "about":
                print(utils().about.absys.about())
            case "help" | "помргите":
                print(utils().help.helpinf.helpotpt())
            case "mkusr":
                utils().usrcreate.mkusr()
            case "kolfetch":
                utils().kolfetch.fetch()
            case "kolfetch", hasattr(sys, "getandroidapilevel"):
                utils().kolfetch.mobfetch()
            case _:
                def nf():
                    var = ("Не найдена команда: " + usrinp + "\nЧтобы посмотреть полный список команд, введите \"help\" или \"h\"")
                    return var

                print(nf())
