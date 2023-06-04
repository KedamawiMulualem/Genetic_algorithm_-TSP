import pygame
import random
import math

# Initialize Pyg
# Set up the font


import random
import numpy as np
import matplotlib.pyplot as plt

# Define the problem
cities =[]
num_cities = 30

# Define the genetic algorithm parameters
population_size = 50
num_generations = 10000
mutation_rate = 0.01

def flip_points_horizontally(points, box_width, box_height):
    # Make a copy of the original points list
    flipped_points = points.copy()
    
    # Flip the y-coordinate of each point horizontally
    for i, point in enumerate(flipped_points):
        x, y = point
        if x < box_width and y < box_height:
            flipped_points[i] = (x, box_height - y - 1)
    
    return flipped_points

# Define the fitness function
def fitness(route):
    total_distance = 0
    for i in range(num_cities):
        city1 = cities[route[i]]
        city2 = cities[route[(i+1)%num_cities]]
        total_distance += np.linalg.norm(city1 - city2)
    return 1/total_distance

# Define the genetic operators
def initialize_population():
    population = []
    for i in range(population_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

def select_parents(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(0, num_cities-1)
    offspring1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    offspring2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2[:crossover_point]]
    return offspring1, offspring2

def mutate(individual):
    for i in range(num_cities):
        if random.random() < mutation_rate:
            j = random.randint(0, num_cities-1)
            individual[i], individual[j] = individual[j], individual[i]

# Define the visualization function
import pygame

def plot_route(route, generation, best_fitness, screen):
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw the cities as black circles
    for city in cities:
        pygame.draw.circle(screen, (0, 0, 0), (int(city[0]), int(city[1])), 5)

    # Draw the edges of the route as red lines
    for i in range(num_cities):
        city1 = cities[route[i]]
        city2 = cities[route[(i+1)%num_cities]]
        pygame.draw.line(screen, (255, 0, 0), (int(city1[0]), int(city1[1])), (int(city2[0]), int(city2[1])))

    # Draw the city labels as text
    font = pygame.font.SysFont(None, 20)
    for i, city in enumerate(cities):
        text = font.render(chr(i+65), True, (0, 0, 255))
        screen.blit(text, (int(city[0]), int(city[1])))

    # Draw the edge labels as text
    for i in range(num_cities):
        city1 = cities[route[i]]
        city2 = cities[route[(i+1)%num_cities]]
        x = (city1[0] + city2[0]) / 2
        y = (city1[1] + city2[1]) / 2
        text = font.render(str(i+1), True, (255, 0, 255))
        screen.blit(text, (int(x), int(y)))

    # Draw the title as text
    title = f'Generation {generation}: Best Distance = {1/best_fitness:.2f}'
    text = font.render(title, True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

# Set up the main loop

   
WINDOW_SIZE = (1600, 900)
BOX_SIZE = (1600, 900)

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode(WINDOW_SIZE,pygame.RESIZABLE)
pygame.display.set_caption("Shortest Path")

# Set up the clock
clock = pygame.time.Clock()

# Set up the points array
points = []

# Set up the state variable
state = "ADDING_POINTS"


import pygame

def update_screen(screen, route, generation, best_fitness):
    # Clear the Pygame screen
    screen.fill((255, 255, 255))
    
    # Plot the cities in the current route
    for i in range(num_cities):
        city = cities[route[i]]
        pygame.draw.circle(screen, (0, 0, 0), (int(city[0]), int(city[1])), 5)
        font = pygame.font.SysFont('calibri', 15)
        
        for i in range(num_cities):
            city = cities[route[i]]
            city_name = chr(i+65)
            city_num = str(i+1)
            text = font.render(f'{city_name} ({city_num})', True, (0, 0, 0))
            text_rect = text.get_rect(center=(int(city[0])+10, int(city[1])+10))
            screen.blit(text, text_rect)
    
    # Draw lines between cities based on the current path
    for i in range(num_cities):
        city1 = cities[route[i]]
        city2 = cities[route[(i+1)%num_cities]]
        pygame.draw.line(screen, (255, 0, 0), (int(city1[0]), int(city1[1])), (int(city2[0]), int(city2[1])), 3)
    
    # Display the generation number and best fitness on the Pygame screen
    font = pygame.font.SysFont('calibri', 30)
    text = font.render(f'Generation {generation}: Best Distance = {1/best_fitness:.2f}', True, (0, 0, 255))
    text_rect = text.get_rect(center=(400, 550))
    screen.blit(text, text_rect)
    
    # Update the Pygame screen
    pygame.display.update()


    
    # Update the Pygame screen
    pygame.display.update()
def draw_box_and_points(screen, points):
    pygame.draw.rect(screen, BLACK, (0, 0, BOX_SIZE[0], BOX_SIZE[1]), 2)
    for point in points:
        pygame.draw.circle(screen, RED, point, 5)
# Set up the main loop


# Set up the main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == "ADDING_POINTS":
                x, y = event.pos
                if x < BOX_SIZE[0] and y < BOX_SIZE[1]:
                    points.append((x, y))
                    if len(points) == num_cities:

                        state = "RUNNING_GA"
                       # points = flip_points_horizontally(points,BOX_SIZE[0],BOX_SIZE[1])
                        cities = np.array(points)
                        # Run the genetic algorithm
                        population = initialize_population()
                        best_route = None
                        best_fitness = 0
                        for generation in range(num_generations):
                            print(generation)
                            new_population = []
                            for i in range(population_size//2):
                                parent1, parent2 = select_parents(population)
                                offspring1, offspring2 = crossover(parent1, parent2)
                                mutate(offspring1)
                                mutate(offspring2)
                                new_population.extend([offspring1, offspring2])
                            population = new_population
                            population.sort(key=fitness, reverse=True)
                            if fitness(population[0]) > best_fitness:
                                best_route = population[0]
                                best_fitness = fitness(best_route)
                                update_screen(screen, best_route, generation, best_fitness)

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if state == "ADDING_POINTS" and len(points) == num_cities:
                                state = "RUNNING_GA"
                                ga_instance.set_points(points)

    # Update the screen
    screen.fill(WHITE)
    if state !="RUNNING_GA":
        draw_box_and_points(screen, points)
    
        pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Quit pygame
pygame.quit()

