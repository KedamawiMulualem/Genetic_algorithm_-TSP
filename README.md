# Traveling Salesman Problem (TSP) with Genetic Algorithm and Pygame

This project is an implementation of the Genetic Algorithm to solve the Traveling Salesman Problem (TSP) and uses Pygame for visualization.

## Prerequisites

Python 3.7+, Pygame, and Numpy are required to run the program. They can be installed via pip:

```bash
pip install python pygame numpy
```

# Script Outline
## The script is structured as follows:

Import necessary modules.
Define problem parameters like number of cities, population size, number of generations, mutation rate.
Define helper functions to manipulate points.
Define the fitness function for evaluating the performance of a route.
Define the initialization, crossover and mutation functions for the genetic algorithm.
Set up Pygame.
Define the main loop to handle mouse clicks for city placements and initiate the genetic algorithm.
## Key Functions
### 1. Flip_points_horizontally(points, box_width, box_height): 
- This function flips the points in a 2D plane along the horizontal axis.
### 2. Fitness(route): 
- This function calculates the fitness of a given route. Fitness is calculated as the inverse of the total distance of the route.
### 3. Initialize_population(): 
- This function creates an initial population of random routes.
### 4. Select_parents(population): 
- This function selects two parent routes from the population at random.
### 5. Crossover(parent1, parent2): 
- This function combines two parent routes into two new offspring routes.
### 6. Mutate(individual): 
- This function applies mutation to a given route by randomly swapping two cities in the route.
### 7. Update_screen(screen, route, generation, best_fitness): 
- This function updates the Pygame window with the current state of the genetic algorithm, including the best route and its fitness.
### 8. Draw_box_and_points(screen, points): 
- This function draws the box and points on the Pygame window.

## Running the script
### To run the script, navigate to the directory containing the script file and execute:
```bash
python tsp_genetic.py
```
This will open a Pygame window. Left click on the window to place cities. After placing the required number of cities (default is 30), the genetic algorithm will start automatically. The best route and its fitness will be updated on the Pygame window. You can watch as the genetic algorithm evolves better and better routes over time.
