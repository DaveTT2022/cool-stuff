import random
import multiprocessing
import math
from multiprocessing import Process
import time

#generating numbers which are on our circle
def number_dict_generator(times, coords):
    while times:
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if round(x ** 2 + y ** 2, 5) == 1:
            times -= 1
            coords[y] = x

#using multiprocessing to make code a bit faster 
def multiprocessing_coords():

    start = time.time()
    thread_list = []
    manager = multiprocessing.Manager()
    coords_dict = manager.dict()

    for i in range (4):
        thread_list.append(Process(target = number_dict_generator, args=(int(times/4), coords_dict)))
    
    for thread in thread_list:
        thread.start()
    

    for thread in thread_list:
        thread.join()
    
    end = time.time()
    print("Multiprocessing time:", end - start)
    coords_dict[0] = 1
    coords_dict[1] = 0
    coords_list = sorted(coords_dict.items())
    return coords_list

#counting distance between all coords and adding to pie
def pie_generator(coords):
    pie = 0.0
    for i in range(len(coords) - 1):
        x_distance = math.pow(coords[i][0] - coords[i+1][0], 2)
        y_distance = math.pow(coords[i][1] - coords[i+1][1], 2)

        pie += math.sqrt(x_distance + y_distance)
    return pie * 2

if __name__ == "__main__":

    times = int(input("How many numbers you want to include? \n"))
    print("wait a little bit")
    coords_list = multiprocessing_coords()
    
    print('result', pie_generator(coords_list))