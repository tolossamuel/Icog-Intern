import random
# initialize the items
items = [
    {"weight": 2, "value": 30},
    {"weight": 3, "value": 24},
    {"weight": 4, "value": 15},
    {"weight": 5, "value": 80},
    {"weight": 9, "value": 10}
]
# inititalize the maximum weight
max_weight = 10
population_size = 10
generations = 100
mutation_rate = 0.1

# initialize population

def init_population():
    return [[random.randint(0, 1) for _ in items] for _ in range(population_size)]

# calculate the fitness of the population

def fitness(chromosome):
    total_weight = sum([item["weight"] for i, item in enumerate(items) if chromosome[i] == 1])
    if total_weight > max_weight:
        return 0
    return total_weight 

# selection
def selection(chromosome):
    tournament = random.sample(chromosome, k=3)
    return max(tournament,key=fitness)

#  crossover
def crossover(parent1,parent2):
    if random.random() < 0.8:
        point = random.randint(1, len(items) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

# mutation
def mutate(chromosome):
    if random.random() < mutation_rate:
        point = random.randint(0, len(items) - 1)
        chromosome[point] = 1 - chromosome[point]
    return chromosome

# genetic algorithm
def genetic_algorithm():
    population = init_population()
    for generation in range(generations):
        population.sort(key = fitness, reverse=True)
        new_population = []
        
        new_population.append(population[0])
        
        while len(new_population) < population_size:
            parent1, parent2 = selection(population), selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population[:population_size]  # Keep population size constant

        # Print best solution of current generation
        best_solution = max(population, key=fitness)
        print(f"Generation {generation + 1}: Best value = {fitness(best_solution)}")

    # Return the best solution
    return max(population, key=fitness)

best_chromosome = genetic_algorithm()

selected_items = [items[i] for i in range(len(items)) if best_chromosome[i] == 1]
total_weight = sum(item["weight"] for item in selected_items)
total_value = sum(item["value"] for item in selected_items)
print("\nBest Solution Found:")
print("Selected Items:", selected_items)
print("Total Weight:", total_weight)
print("Total Value:", total_value)