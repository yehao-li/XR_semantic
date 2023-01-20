import math
import random
import numpy as np

# parameters
K = 5
I_of_L = 1
alpha = 1
miu = 40
epsilon_c = 1
# Gaussian white power(W)
sigma = 4e-14
# log normal shadow(dB)
log_normal_shadow = 8
# small scale fading (dB)
rayleigh_fading = 0
# large scale fading (dB)
psi = 128.1
gamma = 3.76
# upload max power(W)
P_u = 0.1
# download max power(W)
P_d = 20


class User:

    def __init__(self):
        self.polar_diameter = 0
        self.polar_angle = 0
        self.sinr = 0
        self.SemCom = 0
        self.is_semantic = False
        self.power = 0

    def get_polar_diameter(self):
        return self.polar_diameter

    def get_polat_angle(self):
        return self.polar_angle

    def get_sinr(self):
        return self.sinr

    def get_SemCom(self):
        return self.SemCom

    def get_power(self):
        return self.power

    def get_is_semantic(self):
        return self.is_semantic


# server is a special user which locates at (0, 0)
server = User()


class XR:

    def __init__(self, service_radius, user_num, semantic_ratio):
        # service radius (km)
        self.service_radius = service_radius
        self.user_num = user_num
        self.semantic_ratio = semantic_ratio
        self.user_list = self.generate_user()
        # self.density = self.get_density()

    # def get_density(self):
    #     density = self.user_num / (math.pi * self.service_radius ** 2)
    #     return density

    def get_user_num(self):
        return self.user_num

    def get_service_radius(self):
        return self.service_radius

    def get_semantic_ratio(self):
        return self.semantic_ratio

    # generate user in polar coordinates
    def generate_user(self):
        user_list = []
        for i in range(self.user_num):
            user = User()
            user.polar_diameter = random.uniform(0, self.service_radius)
            user.polar_angle = random.uniform(0, 2 * math.pi)
            user_list.append(user)
        return user_list

    # calculate the sum SemCom
    def calc_sum_SemCom(self):
        sum_SemCom = 0
        for user in self.user_list:
            if user.is_semantic:
                user.SemCom = calc_SemCom(user)
                sum_SemCom += user.SemCom
            else:
                bitcom = calc_BitCom(user, self.user_list)
                user.SemCom = conv_BitCom_to_SemCom(bitcom)
                sum_SemCom += user.SemCom
        return sum_SemCom

    # allocate power to users averagely
    def alloc_power_avg(self):
        for user in self.user_list:
            user.power = P_d / self.user_num

    # todo: allocate power to users greedy
    def alloc_power_greedy(self):
        pass

    # allocate power to users randomly
    def alloc_power_rand(self):
        power_list = np.random.dirichlet(np.ones(self.user_num), size=1)[0] * P_d
        for i, user in enumerate(self.user_list):
            user.power = power_list[i]

    # todo: allocate power to users based on the genetic algorithm
    def alloc_power_genetic_algo(self):
        pass

    # select semantic users from user list
    def select_semantic_user(self):
        self.alloc_power_avg()
        semantic_user_num = int(self.user_num * self.semantic_ratio)
        for user in self.user_list:
            user.sinr = calc_sinr(user, self.user_list)
        self.user_list.sort(key=lambda x: x.sinr)
        for i in range(semantic_user_num):
            self.user_list[i].is_semantic = True


# calculate distance between two points by cosine law (km)
def calc_distance(a, b):
    return math.sqrt(a.polar_diameter ** 2 + b.polar_diameter ** 2 -
                     2 * a.polar_diameter * b.polar_diameter * math.cos(a.polar_angle - b.polar_angle))


# convert db to watt
def conv_db_to_watt(db):
    return 10 ** (db / 10)


# convert BitCom to SemCom
def conv_BitCom_to_SemCom(bitcom):
    return bitcom * I_of_L / miu * epsilon_c


# calculate the channel coefficient
def calc_channel_coefficient(a, b):
    distance = calc_distance(a, b)
    h = (psi + 10 * gamma * math.log10(distance) + log_normal_shadow) / 2.0 + rayleigh_fading
    return conv_db_to_watt(h)


# calculate SemCom
def calc_SemCom(user):
    epsilon = calc_epsilon(user)
    return alpha * I_of_L / K * epsilon


# calculate epsilon (a logistic function) based on fig. 2*, (K = 5)
# *Heterogeneous Semantic and Bit Communications:A Semi-NOMA Scheme
def calc_epsilon(user):
    k, x0 = -0.15, -2  # estimated parameters
    return 1 / (1 + math.exp(k * (user.sinr - x0)))


# calculate BitCom based on eq. 10*
# *Exploiting Semantic Communication for Non-Orthogonal Multiple Access
def calc_BitCom(user, user_list):
    sinr = calc_sinr(user, user_list)
    return alpha * math.log2(1 + sinr)


# calculate SINR
def calc_sinr(user, user_list):
    h = calc_channel_coefficient(user, server)
    interference = 0
    for other_user in user_list:
        if user != other_user:
            interference += other_user.power * calc_channel_coefficient(other_user, server) ** 2
    return user.power * h**2 / (sigma**2 + interference)
