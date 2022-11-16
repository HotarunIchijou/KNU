from random import sample, randint, choices
from time import sleep
from tqdm import *
def kolpac_info():
    print("Kolpac - принципиально новый пакетный менеджер, разработанный специально для операционной системы KNU")

def kolpac_update():
    utils = ["devtools", "shutils-base", "kolpac", "kolfetch"]
    amt = choices([0,1,2,3,4], weights=[60,20,10,8,2])[0]
    toupdate = sample(utils, k = amt)
    out = ' '.join(toupdate)
    if len(toupdate) == 0:
        sleep(2)
        print("Нечего обновлять")
    else:
        sleep(2)
        print(f"К обновлению готовы пакеты: {out}")
        sleep(1)
        startupdate = input("Начать обновление сейчас? [y, N]: ")
        if "n" in startupdate or "N" in startupdate or "No" in startupdate or "no" in startupdate:
            print("Обновление отменено")
            sleep(1)
        if "y" in startupdate or "Y" in startupdate or "Yes" in startupdate or "yes" in startupdate:
            sleep(0.5)
            print("Начинается обновление")
            sleep(1)
            tq = tqdm(toupdate)
            for i in tq:
                desc_template = "Обновление пакета: {}"
                tq.set_description(desc_template.format(i))
                sleep(randint(0,5))
        else:
            pass

kolpac_update()