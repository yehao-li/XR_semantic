import time
import csv
import infrastructure as infra
# import matplotlib.pyplot as plt


def run(service_radius, user_num, semantic_ratio, alloc_func, ind_var):
    results = []
    # ranging the service radius or user number or semantic ratio
    for i in range(0, 50):
        # calculate the time taken to run the program
        startTime = time.time()
        # set step size
        if ind_var == 'service_radius':
            service_radius += 0.001
        elif ind_var == 'user_num':
            user_num += 1
        elif ind_var == 'semantic_ratio':
            semantic_ratio += 0.01
        # create an instance of the class XR
        xr = infra.XR(service_radius, user_num, semantic_ratio)
        # select semantic users by sinr when allocate power to users averagely
        xr.select_semantic_user()

        # allocate power to users
        if alloc_func == 'avg':
            # averagely
            xr.alloc_power_avg()
        elif alloc_func == 'rand':
            # randomly
            xr.alloc_power_rand()
        elif alloc_func == 'greedy':
            # greedy
            xr.alloc_power_greedy()
        elif alloc_func == 'algo':
            # genetic algorithm
            xr.alloc_power_genetic_algo()

        # calculate the sum SemCom
        sum_SemCom = xr.calc_sum_SemCom()
        # calculate the duration of the program
        endTime = time.time()
        duration = endTime - startTime
        results.append([service_radius, user_num, semantic_ratio, sum_SemCom, duration, alloc_func])
        # print('service_radius: ', service_radius, 'user_num: ', user_num, 'semantic_ratio: ', semantic_ratio,
        #       'sum_SemCom: ', sum_SemCom, 'duration: ', duration)
    # write the results to a csv file
    with open('summary.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows(results)


# independent variable
init_service_radius = 0.050
init_user_num = 30
init_semantic_ratio = 0.00

# run the program
run(init_service_radius, init_user_num, init_semantic_ratio, 'rand', 'semantic_ratio')
