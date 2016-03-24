import random

goal_organism = 'METHINKS IT IS A WEASEL'
bases = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
mutation_rate = 0.04
number_of_children = 100

def mutate(parent_code, mutation_rate):
    new_code = []
    for character in parent_code:
        if random.random() < mutation_rate:
            new_code.append(random.choice(bases))
        else:
            new_code.append(character)
    return ''.join(new_code)

def reproduce(parent_code, number_of_children):
    children = []
    for x in range(number_of_children):
        children.append(mutate(parent_code, mutation_rate))
    return children

def naturally_select(organisms): #returns most "fit" organism. The rest are discarded (they die off)
    fittest_organism = 0
    fittest_organism_code = ''
    for child in organisms:
        fittness = 0
        for x in range(len(child)):
            if child[x-1] == goal_organism[x-1]:
                fittness += 1
        if fittness >= fittest_organism:
            fittest_organism = fittness
            fittest_organism_code = child
    return fittest_organism_code

def abiogenesis(): #generates first organism. "Genome" is all random letters.
    return ''.join([random.choice(bases) for x in range(len(goal_organism))])

first_organism = abiogenesis()
surviving_organism = first_organism
generation = 1
organisms = [first_organism]
while surviving_organism != goal_organism:
    print("Generation: %s" % str(generation))
    surviving_organism = naturally_select(organisms)
    print("Fittest organism's genetic code: %s" % surviving_organism)
    organisms = reproduce(surviving_organism, number_of_children)
    generation += 1