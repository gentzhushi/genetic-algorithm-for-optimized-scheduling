import random

machines = {
    'Lathe': [('Turning', 30), ('Milling', 25), ('Drilling', 20)],
    'Milling Machine': [('Milling', 30), ('Drilling', 25), ('Cutting', 15), ('Trimming', 30)],
    'Welder': [('Welding', 40), ('Cutting', 20), ('Grinding', 30)],
    'Grinder': [('Grinding', 25), ('Polishing', 15), ('Trimming', 20)],
    'Saw': [('Cutting', 40), ('Trimming', 35)],
    'Bender': [('Bending', 30), ('Forming', 20), ('Cutting', 10)],
    'Press': [('Pressing', 35), ('Forming', 25)],
    'CNC Router': [('Cutting', 25), ('Milling', 20), ('Engraving', 15)],
    'Sander': [('Sanding', 30), ('Polishing', 20)],
    'Laser Cutter': [('Cutting', 30), ('Engraving', 20)]
}

tasks = {
    'Turning': ['Lathe'],
    'Milling': ['Lathe', 'Milling Machine', 'CNC Router'],
    'Drilling': ['Lathe', 'Milling Machine'],
    'Welding': ['Welder'],
    'Grinding': ['Welder', 'Grinder'],
    'Polishing': ['Grinder', 'Sander'],
    'Cutting': ['Milling Machine', 'Welder', 'Saw', 'Bender', 'CNC Router', 'Laser Cutter'],
    'Trimming': ['Milling Machine', 'Saw', 'Grinder'],
    'Bending': ['Bender'],
    'Forming': ['Bender', 'Press'],
    'Pressing': ['Press'],
    'Engraving': ['CNC Router', 'Laser Cutter'],
    'Sanding': ['Sander']
}
# turning milling drilling
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