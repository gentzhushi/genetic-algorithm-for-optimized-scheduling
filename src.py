import random
import json
from collections import defaultdict
import heapq

def generate_chromosome(tasks_list: list, tasks: dict) -> list:
    # ka me gjenerate random choice of machine for said task, for every task
    chromosome = defaultdict(list)
    for task in tasks_list:
        machine = random.choice(tasks[task])
        chromosome[task] = machine
    return chromosome
    # task -> machine

def calculate_fitness(chromosome: dict, machines: dict) -> int:
    # kromozomi: machine -> task
    time_map = defaultdict(int)
    for task, machine in chromosome.items():
            time_map[machine] += machines[machine][task]
    return max(time_map.values())
    # ktheje kohen ma tgat per tcilen eshte ndonje maqine nxan.

def selection(generation: list) -> list:
    # ka me i zgjedh gjysen ma fit tni gjenerates (gjenerata osht array me kromozome)
    # bone heap
    min_heap = [calculate_fitness(chrom) for chrom in generation]
    heapq.heapify(min_heap)

    # merri bottom 50%
    selection = [heapq.heappop(min_heap) for _ in range(len(generation) // 2)]

    return selection

def crossover(parent1: dict, parent2: dict, CROSSOVER_RATE: float) -> tuple[dict, dict]:
    # ka me i bo crossover 2 kromozome
    if random.random() > CROSSOVER_RATE:
        return parent1, parent2

    child1 = {}
    child2 = {}
    for task in parent1.keys():
        #FLIP A COIN A ME JA NDRRU MAQINEN PER TASKUN SPECIFIK A JO
        #perndryshe kjo i bjen gjysen e seneve mi marr prej nanes gjysen prej babes, 
        #amo, nuk i merr me ren po ne menyre heterogjene
        if random.choice([True, False]): 
            child1[task] = parent2[task]
            child2[task] = parent1[task]
        else:
            child1[task] = parent1[task]
            child2[task] = parent2[task]
    return child1, child2

def mutate(chromosome: dict, tasks: dict, MUTATION_RATE: float) -> dict:
    # ka me mutate ni kromozom qe e merr si input
    if random.random() > MUTATION_RATE:
        return chromosome
    random_task = random.choice(chromosome.keys())
    chromosome[random_task] = random.choice(tasks[random_task])
    return

# # print(f"{machines}\n\n{tasks}")
# chromosome1 = generate_chromosome(tasks)
# chromosome2 = generate_chromosome(tasks)

# print(f"kromozomi:\n{str(chromosome1)}")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# print(f"fitness: \n{calculate_fitness(chromosome1)}")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# # print(f"top 50%: {selection()}")
# # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# print(f"chromozomes: \n{str(chromosome1)}\n{str(chromosome2)}")
# print(f"crossover: \n{str(crossover(chromosome1, chromosome2, 1))}")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")