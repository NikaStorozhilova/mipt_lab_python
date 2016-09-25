#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    t = 0
    fill_cell()
    while(wall_is_beneath() == False):
        while (wall_is_on_the_right() == False):
            fill_cell()
            move_right()
            t = 1
        fill_cell()
        if(t== 1 and wall_is_beneath() == False):
            move_down()
            fill_cell()
            t = 0
        while (wall_is_on_the_left() == False):
            move_left()
            fill_cell()
            if(wall_is_beneath() == True):
                return
        t = 0
        move_down()
    if(wall_is_on_the_right() == False):
        move_right()
        if cell_is_filled() ==False:
            while (wall_is_on_the_right() == False):
                fill_cell()
                move_right()
            while (wall_is_on_the_left() == False):
                fill_cell()
                move_left()
        else:
            move_left()
    fill_cell()




if __name__ == '__main__':
    run_tasks()