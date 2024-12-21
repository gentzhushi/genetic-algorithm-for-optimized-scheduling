# Genetic Algorithm for Optimized Scheduling

This project implements a genetic algorithm to optimize the scheduling of tasks across multiple machines in a factory. The goal is to minimize overall production time while adhering to task and machine constraints.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Execution](#execution)
- [Algorithm Description](#algorithm-description)
- [Contributors](#contributors)

## Requirements

Ensure you have the following installed:

- Python 3.8 or newer
- JSON files `machines.json` and `tasks.json` in the specified format

## Setup

1. Clone this repository.
2. Ensure the `machines.json` and `tasks.json` files are located in a `json/` directory relative to the script.
3. Install necessary Python dependency using `pip3 install matplotlib`

## Execution

Run the script using the following command:

```bash
python3 main.py
```

## Algorithm Description
This section describes the genetic algorithm components implemented in the project.

1. Function: generate_chromosome
   - Description: Randomly assigns tasks to machines.
   - Input: List of tasks.
   - Output: Chromosome represented as a dictionary mapping machines to tasks.
     
2. Function: calculate_fitness
   - Description: Calculates the fitness of a chromosome by evaluating the minimum time required by any machine in the schedule.
   - Input: Chromosome.
   - Output: Fitness score (integer).

3. Function: selection
   - Description: Selects the top 50% of chromosomes from the current generation based on fitness.
   - Input: List of chromosomes (generation).
   - Output: Selected chromosomes.

4. Function: crossover
   - Description: Combines two parent chromosomes to produce two child chromosomes.
   - Input: Two parent chromosomes and a crossover rate.
   - Output: Two child chromosomes.

5. Function: mutate
   - Description: Randomly mutates a chromosome based on the mutation rate.
   - Input: Chromosome and mutation rate.
   - Output: Mutated chromosome.

# Contributors:

- [Euron Osmani](#euron-osmani)
- [Gent Zhushi](#gent-zhushi)
- [Gresa Hasani](#gresa-hasani)
- [Lorik Agaj](#lorik-agaj)

 
