from time import localtime, strftime, sleep

class time:
    def wtime():
        t = localtime()
        time = strftime('%d.%m.%Y г. %H:%M:%S', t);
        return time
