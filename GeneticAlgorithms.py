import random
import string

goal = "genetic_algorithm"
number_candidates = 50
max_generation = 20000

# Creating a class with an object that represents a candidate with a particular atribute(adn) and fitness
class Individual(object):
    def __init__(self, dna, fitness):
        self.dna = dna
        self.fitness = fitness

# Calculating fitness according to the distance between corresponding characters in both strings (goal and origin)
def calculate_fitness(origin, goal):
    fitness = 0
    for i in range(0, len(origin)):
        fitness += (ord(goal[i]) - ord(origin[i])) ** 2
    return fitness

# Simulating mutations
def mutation(parent1, parent2):
    daughter = parent1.dna[:]

    start = random.randint(0, len(parent2.dna) - 1)
    stop = random.randint(0, len(parent2.dna) - 1)
    if start > stop:
        stop, start = start, stop

    # Simulating homologous recombination (meiosis)
    daughter[start:stop] = parent2.dna[start:stop]

    # Simulation a punctual mutation
    position = random.randint(0, len(daughter) - 1)
    daughter[position] = chr(ord(daughter[position]) + random.randint(-1, 1))
    daughter_fitness = calculate_fitness(daughter, goal)

    return Individual(daughter, daughter_fitness)

# Choosing a parent randomly
def random_parent(population):
    return population[int(random.random() * random.random() * (number_candidates - 1))]

# Showing the result of a simulation
def show_generation(generation, population):
    print('Pasos de simulación: %d' % generation)
    print()
    print('  Fitness         ADN')
    print('------------------------')
    for candidate in population:
        print("%6i %15s" % (candidate.fitness, ''.join(candidate.dna)))
    print()

# Creating a population
def init_population():
    population = []
    for i in range(0, number_candidates):
        # Randomly create a string
        dna = [random.choice(string.printable[:-5]) for _ in range(0, len(goal))]
        fitness = calculate_fitness(dna, goal)
        candidate = Individual(dna, fitness)
        population.append(candidate)
    return population

# Simulating a genetic algorithm
def simulation():
    population = init_population()
    generation = 0
    while True and generation < max_generation:
        generation += 1
        population.sort(key=lambda candidate: candidate.fitness)

        if population[0].fitness == 0:
            break

        parent1 = random_parent(population)
        parent2 = random_parent(population)

        daughter = mutation(parent1, parent2)

        if daughter.fitness < population[-1].fitness:
            population[-1] = daughter

    if generation == max_generation:
        print(u'Maximum number of generations.')

    show_generation(generation, population)

simulation()