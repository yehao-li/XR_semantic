# genetic algorithm

# def fitness(x):
#     for i, user in enumerate(self.user_list):
#         user.power = x[i]
#     sum_SemCom = calc_sum_SemCom(self.user_list)
#     return -sum_SemCom
#
# def constraint(x):
#     return np.array([P_d - sum(x)])
#
# b = (0, P_d)
# bnds = (b,) * self.user_num
# con = {'type': 'eq', 'fun': constraint}
# cons = ([con])
# x0 = np.random.rand(self.user_num)
# res = minimize(fitness, x0, method='SLSQP', bounds=bnds, constraints=cons)
# for i, user in enumerate(user_list):
#     user.power = res.x[i]
def alloc_power_genetic_algo(self, user_list):
    # set the number of generations
    generation_num = 100
    # set the number of chromosomes
    chromosome_num = 100
    # set the number of genes
    gene_num = self.user_num
    # set the number of elite chromosomes
    elite_num = 10
    # set the number of children
    children_num = 90
    # set the mutation rate
    mutation_rate = 0.01
    # set the number of iterations
    iteration_num = 100
    # set the number of iterations without improvement
    iteration_without_improvement = 0
    # set the best fitness
    best_fitness = 0
    # set the best chromosome
    best_chromosome = None
    # set the best chromosome list
    best_chromosome_list = []
    # set the best fitness list
    best_fitness_list = []
    # set the average fitness list
    average_fitness_list = []
    # set the worst fitness list
    worst_fitness_list = []
    # set the average fitness
    average_fitness = 0
    # set the worst fitness
    worst_fitness = 0
    # set the fitness list
    fitness_list = []
    # set the fitness
    fitness = 0
    # set the chromosome list
    chromosome_list = []
    # set the chromosome
    chromosome = []
    # set the gene list
    gene_list = []
    # set the gene
    gene = 0
    # set the children list
    children_list = []
    # set the children
    children = []
    # set the new chromosome list
    new_chromosome_list = []
    # set the new chromosome
    new_chromosome = []
    # set the new gene list
    new_gene_list = []
    # set the new gene
    new_gene = 0
    # set the new power list
    new_power_list = []
    # set the new power
    new_power = 0
    # set the new user list
    new_user_list = []
    # set the new user
    new_user = None
    # set the new sum SemCom
    new_sum_SemCom = 0
    # set the new fitness
    new_fitness = 0
    # set the new fitness list
    new_fitness_list = []
    # set the new best fitness
    new_best_fitness = 0
    # set the new best chromosome
    new_best_chromosome = None
    # set the new best chromosome list
    new_best_chromosome_list = []
    # set the new best fitness list
    new_best_fitness_list = []
    # set the new average fitness list
    new_average_fitness_list = []
    # set the new worst fitness list
    new_worst_fitness_list = []
    # set the new average fitness
