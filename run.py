import time
import csv
import infrastructure as infra
# import matplotlib.pyplot as plt

# calculate the time taken to run the program
startTime = time.time()

# independent variable
service_radius = 0.050
user_num = 20
semantic_ratio = 0.01

# create a list of users
xr = infra.XR(service_radius, user_num, semantic_ratio)
user_list = xr.generate_user()

# allocate power to users averagely
xr.alloc_power_avg(user_list)
# todo: allocate power to users in various ways

# select semantic users by their sinr ranks
xr.select_semantic_user(user_list)

# calculate the sum SemCom
sum_SemCom = infra.calc_sum_SemCom(user_list)

endTime = time.time()
duration = endTime - startTime

# summary
filename = 'summary.csv'
with open(filename, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    row = [xr.get_user_num(), xr.get_service_radius(),
           xr.get_semantic_ratio(), duration, sum_SemCom]
    writer.writerow(row)
