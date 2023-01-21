import time
import csv
import infrastructure as infra
import matplotlib.pyplot as plt

ind_var_dict = {'service_radius': 0, 'user_num': 1, 'semantic_ratio': 2}


def get_sum_SemCom(init_service_radius, init_user_num, init_semantic_ratio, alloc_func, ind_var):
    results = []
    service_radius, user_num, semantic_ratio = init_service_radius, init_user_num, init_semantic_ratio
    # ranging the service radius or user number or semantic ratio
    for i in range(0, 50):
        # calculate the time taken to run the program
        startTime = time.time()
        # set step size
        if ind_var == 'service_radius':
            service_radius += 0.001
        elif ind_var == 'user_num' or ind_var == 'computation_time':
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
    return results


# run and plot
def run(init_service_radius, init_user_num, init_semantic_ratio, ind_var):
    re_rand = get_sum_SemCom(init_service_radius, init_user_num, init_semantic_ratio, 'rand', ind_var)
    re_avg = get_sum_SemCom(init_service_radius, init_user_num, init_semantic_ratio, 'avg', ind_var)
    re_greedy = get_sum_SemCom(init_service_radius, init_user_num, init_semantic_ratio, 'greedy', ind_var)
    re_algo = get_sum_SemCom(init_service_radius, init_user_num, init_semantic_ratio, 'algo', ind_var)
    idy, dep_var = 3, 'Sum_SemCom'
    if ind_var == 'computation_time':
        ind_var, idy, dep_var = 'user_num', 4, 'Computation Time'
    idx = ind_var_dict[ind_var]
    # plot the results
    plt.plot([i[idx] for i in re_rand], [i[idy] for i in re_rand], label='random')
    plt.plot([i[idx] for i in re_avg], [i[idy] for i in re_avg], label='average')
    plt.plot([i[idx] for i in re_greedy], [i[idy] for i in re_greedy], label='greedy')
    plt.plot([i[idx] for i in re_algo], [i[idy] for i in re_algo], label='genetic algorithm')
    plt.xlabel(ind_var)
    plt.ylabel(dep_var)
    plt.legend()
    plt.show()


# run the program when semantic_ratio changes
run(0.04, 20, 0.00, 'semantic_ratio')

# run the program when service_radius changes
run(0.01, 20, 0.30, 'service_radius')

# run the program when user_num changes
run(0.04, 0, 0.30, 'user_num')

# run the program when computation_time changes
run(0.04, 0, 0.30, 'computation_time')
