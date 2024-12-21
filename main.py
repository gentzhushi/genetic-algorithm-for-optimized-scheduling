import json
import src as util
import random

"""
    qka ka me ndodh qitu:
        1 - ki me pas ni array me machines (secila e ka ka ni task, edhe duration sa zgat) 
            aka machineName -> [task name, task duration]
        2 - golla osht me minimizu total duration (fitness functiuon osht total duration, minimalet tu u zgjedh)
        3 - funksionon nbaz t3 funksioneve: 
             > crossover - i bon crossover 2 genotypes
             > mutation - e merr ni kromozom, edhe ja shton ni curveball (e ndrron ni gjen veq palidhje tu shpresu per ma tmiren)
             > selection - i zgjedh top fittest genes prej ni popullation
        4 - duhet me keep track t gjeneratave t orareve sa t ekzekutohet algoritmi(me i grafu)
        
    params:
        1 - lista e tasqeve
        2 - lista e duracioneve
        3 - machine constraints

    returns:
        - [optimal schedule, prduction time]
"""

with open("json/machines.json") as file:
    machines = json.load(file)

with open("json/tasks.json") as file:
    tasks = json.load(file)

POPULLATION_SIZE = 5
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8

POPULLATION = [util.generate_chromosome(tasks, tasks) for _ in range(POPULLATION_SIZE)]
BEST_SCHEDULE = None
BEST_SCHEDULES = []
BEST_SCHEDULE_TIME = float("inf")
BEST_SCHEDULE_TIMES = []

if __name__ == "__main__":
    for generation in range(NUM_GENERATIONS):
        fitnesses = [util.calculate_fitness(schedule, machines) for schedule in POPULLATION]
        local_best_schedule_time = min(fitnesses)
        local_best_schedule = POPULLATION[fitnesses.index(local_best_schedule_time)]
        BEST_SCHEDULE_TIMES += [local_best_schedule_time]
        BEST_SCHEDULES += [local_best_schedule]
        if local_best_schedule_time < BEST_SCHEDULE_TIME:
            BEST_SCHEDULE_TIME = local_best_schedule_time
            BEST_SCHEDULE = local_best_schedule
        print(f"Generation [{generation + 1}] - \tBest Schedule: [{local_best_schedule_time}]-[{local_best_schedule}]")
        
        new_popullation = []
        top_fittest = util.selection(POPULLATION)
        while len(new_popullation) < POPULLATION_SIZE:
            parent1 = top_fittest.pop(0) # pop front
            parent2 = top_fittest.pop(0)
            child1, child2 = util.crossover(parent1, parent2, CROSSOVER_RATE)
            new_popullation.append(util.mutate(child1, tasks))
            if len(new_popullation) < POPULLATION_SIZE:
                new_popullation.append(util.mutate(child2, tasks))
        POPULLATION = new_popullation

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"BEST_SCHEDULE_TIMES: {BEST_SCHEDULE_TIMES}")