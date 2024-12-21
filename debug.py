import src
import json

with open("json/machines.json") as file:
    machines = json.load(file)

with open("json/tasks.json") as file:
    tasks = json.load(file)

kromozomi = src.generate_chromosome(tasks, tasks)
fitnesi = src.calculate_fitness(kromozomi, machines)
selection = src.selection([src.generate_chromosome(tasks, tasks) for _ in range(10)], machines)

for schedule in selection:
    print(schedule)