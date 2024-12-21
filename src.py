import random
import json
from collections import defaultdict
import heapq

with open("json/machines.json") as file:
    machines = json.load(file)

with open("json/tasks.json") as file:
    tasks = json.load(file)


def generate_chromosome(tasks_list: list) -> list:
    # ka me gjenerate random choice of machine for said task, for every task
    chromosome = defaultdict(list)
    for task in tasks_list:
        machine = random.choice(tasks[task])
        chromosome[machine].append(task)
    return chromosome


def calculate_fitness(chromosome: dict) -> int:
    # kromozomi: machine -> task
    time_map = defaultdict(int)
    for machine in chromosome.keys():
        for task in chromosome[machine]:
            time_map[machine] += machines[machine][task]
    return min(time_map.values())


# ktheje kohen ma tgat per tcilen eshte ndonje maqine nxan.

def selection(generation: list) -> list:
    # ka me i zgjedh gjysen ma fit tni gjenerates (gjenerata osht array me kromozome)
    # bone heap
    min_heap = [calculate_fitness(chrom) for chrom in generation]
    heapq.heapify(min_heap)

    # merri bottom 50%
    selection = []
    for i in range(len(generation) // 2):
        selection.append(heapq.heappop(min_heap))

    return selection


def crossover(parent1: dict, parent2: dict, CROSSOVER_RATE: float) -> tuple[
    dict, dict]:  # ka me i bo crossover 2 kromozome
    if random.random() > CROSSOVER_RATE:
        return parent1, parent2

    child1 = {}
    child2 = {}
    split_point = random.randint(1, len(parent1) - 2)

    parent1keys = list(parent1.keys())
    parent2keys = list(parent2.keys())

    for i in range(split_point):
        child1[parent1keys[i]] = parent1[parent1keys[i]]
        child2[parent2keys[i]] = parent2[parent2keys[i]]

    for i in range(split_point, len(parent1)):
        child1[parent2keys[i]] = parent2[parent2keys[i]]
        child2[parent1keys[i]] = parent1[parent1keys[i]]

    return child1, child2


def mutate(chromosome: dict, MUTATION_RATE: float) -> dict:  # ka me mutate ni kromozom qe e merr si input
    if random.random > MUTATION_RATE:
        return chromosome

    return


# print(f"{machines}\n\n{tasks}")
chromosome1 = generate_chromosome(tasks)
chromosome2 = generate_chromosome(tasks)

print(f"kromozomi:\n{str(chromosome1)}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(f"fitness: \n{calculate_fitness(chromosome1)}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# print(f"top 50%: {selection()}")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(f"chromozomes: \n{str(chromosome1)}\n{str(chromosome2)}")
print(f"crossover: \n{str(crossover(chromosome1, chromosome2, 1))}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")