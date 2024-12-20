import random
import json

with open("json/machines.json") as file:
    machines = json.load(file)

with open("json/tasks.json") as file:
    tasks = json.load(file)

def generate_chromosome(tasks_list: list) -> list:
    # ka me gjenerate random choice of machine for said task, for every task
    for task in tasks_list:
        machine = random.choice(tasks[task])
        chromosome += [task, machine]
    return chromosome

def calculate_fitness(chromosome: list): # ka me kalkulu total time tni kromozomit
    
    return

def selection(generation): # ka me i zgjedh gjysen ma fit tni gjenerates
    return

def crossover(parent1, parent2): # ka me i bo crossover 2 kromozome
    return

def mutate(chromosome): # ka me mutate ni kromozom qe e merr si input
    return