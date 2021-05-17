import datetime
import time
import pygame


def musicplayer(filename, stopper):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)
    while True:
        a = input("Write s to stop \n")
        if stopper == a.lower():
            pygame.mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg}  {datetime.datetime.now()}\n")


if __name__ == '__main__':
    init_water = time.time()
    init_eye = time.time()
    init_exe = time.time()
    watertime = 35*60
    eyetime = 40*60
    exetime = 60*60

    while True:
        if time.time() - init_water > watertime:
            print("Water Drinking Time.")
            musicplayer("water.mp3", "s")
            init_water = time.time()
            log_now("Drank water at ")
        if time.time() - init_exe > exetime:
            print("Exercise Time.")
            musicplayer("exe.mp3", "s")
            init_exe = time.time()
            log_now("Exercise done at ")

        if time.time() - init_eye > eyetime:
            print("Eye Exercise Time.")
            musicplayer("eye.mp3", "s")
            init_eye = time.time()
            log_now("Rubbed his eyes at ")

