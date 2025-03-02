import numpy as np
import random
import matplotlib.pyplot as plt

# Define fixed cities (x, y coordinates)
cities = [
    (10, 20), (40, 80), (70, 90), (20, 50), (90, 60),
    (60, 30), (50, 70), (80, 20), (30, 40), (100, 10)
]

# Compute the distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the total route distance
def route_distance(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) + distance(route[-1], route[0])

# Fitness function (lower distance = higher fitness)
def fitness(route):
    return 1 / (route_distance(route) + 1e-6)  # Avoid division by zero

# Generate a random route (random permutation of cities)
def random_route():
    return random.sample(cities, len(cities))

# Create an initial population
def create_population(size=10):
    return [random_route() for _ in range(size)]

# Tournament Selection
def selection(population, k=3):
    tournament = random.sample(population, k)
    return max(tournament, key=fitness)

# Crossover (Order Crossover - OX1)
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    
    remaining = [city for city in parent2 if city not in child]
    j = 0
    for i in range(size):
        if child[i] is None:
            child[i] = remaining[j]
            j += 1
    return child

# Mutation (Swap Mutation)
def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Genetic Algorithm
def genetic_algorithm(pop_size=50, generations=500, mutation_rate=0.1):
    population = create_population(pop_size)

    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)  # Sort by fitness
        new_population = [population[0]]  # Keep the best solution (Elitism)

        while len(new_population) < pop_size:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

        # Print best route per generation
        if generation % 50 == 0:
            best_distance = route_distance(population[0])
            print(f"Generation {generation}: Best Distance = {best_distance:.2f}")

    return population[0], route_distance(population[0])

# Function to plot the best route
def plot_route(route, title="Best Route Found"):
    plt.figure(figsize=(8, 6))
    x, y = zip(*route)
    plt.plot(x + (x[0],), y + (y[0],), marker='o', linestyle='-', color='b')  # Connect cities
    plt.scatter(x, y, c='red', marker='o')  # Mark cities
    for i, city in enumerate(route):
        plt.text(city[0], city[1], str(i+1), fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid()
    plt.show()

# Run the algorithm
best_route, best_distance = genetic_algorithm()
print("\nBest Route Found:", best_route)
print("Best Distance:", best_distance)

# Plot the best route
plot_route(best_route)
