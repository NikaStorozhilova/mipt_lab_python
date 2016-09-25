#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()

    for i in range(12):
        fill_cell()
        move_down()
        for n in range(i+1):
            move_right()
            fill_cell()
        move_left(i+1)
    fill_cell()
    move_down()



if __name__ == '__main__':
    run_tasks()
