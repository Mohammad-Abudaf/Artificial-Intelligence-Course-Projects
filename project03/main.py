"""
Name: Mohammed S. Abu-daf @Shark
ID: 000000000
Topic:
    Artificial Intelligence: Genetic algorithm.
    Genetic algorithm

Contact:
    email: mohammed_abudaf@student.iugaza.edu.ps
    github: https://github.com/Mohammad-Abudaf
"""

import random

try:
    import numpy.random as npr
except ImportError:
    print("Error Importing: numpy not found!\n"
          "hint: try to install numpy lib using pip -- try pip install numpy or\n"
          "pip install -r requirements on your venv or system.")
    exit(-1)


def fitness_function(chromosome: str) -> int:
    """
    definition of fitness function f = (a+b) - (c+d) + (e+f) - (g+h)
    :param chromosome: str
        binary string that define the values of the valuables in binary
        i.e:
            00011100100101111001010001010011
    :return:
        int: value of the function
    """
    a: int = int(chromosome[0: 4], 2)
    b: int = int(chromosome[4: 8], 2)
    c: int = int(chromosome[8: 12], 2)
    d: int = int(chromosome[12: 16], 2)
    e: int = int(chromosome[16: 20], 2)
    f: int = int(chromosome[20: 24], 2)
    g: int = int(chromosome[24: 28], 2)
    h: int = int(chromosome[28:], 2)

    result: int = (a + b) - (c + d) + (e + f) - (g + h)
    return result


def is_valid_chromosome(chrom: str) -> bool:
    """
    this function check the validation of the chromosome
    due to the range of the values  of the variables in range 0 ~ 9
    the chromosome as "1111000011110000111100001111" is invalid
    :param chrom: as str
    :return: bool
        if the chromosome is valid or not!
    """
    index: int = 0
    while index < len(chrom):
        temp: str = chrom[index: index + 4]
        temp_decimal: int = int(temp, 2)
        if temp_decimal > 9:
            return False
        index = index + 4

    return True


def init_first_population(population_number: int,
                          chromosome_length: int) -> list:
    """
    this function initialize the initial population of chromosomes in binary strings
        the behavior of the function is completely randomly with no control of
        the randomness
        the range of number is 0~9, and it encodes it with 4bit binary string
    :param population_number: int, the number of chromosome in population
    :param chromosome_length: int, the number of genes in single chromosome
    :return: list of string: contains the population of chromosomes
    """
    result: list = list()
    for i in range(population_number):
        temp_chromosome: str = ""
        for j in range(0, chromosome_length, 4):
            random_number: int = random.randint(0, 9)
            random_number_binary: str = "{0:04b}".format(random_number)
            temp_chromosome = temp_chromosome + random_number_binary
        result.append(temp_chromosome)

    return result


def crossover(chromosome0: str, chromosome1: str, chromosome_length: int) -> list:
    """
    In crossover, child chromosomes are produced by aligning two parents,
    picking a random position along their length, and swapping the tails with a
    probability Pc, known as the crossover probability.

    :param chromosome0: binary string of the first chromosome
    :param chromosome1: binary string of the second chromosome
    :param chromosome_length: number of genes in the chromosome
    :return:
    """
    cross_point: int = random.randint(0, chromosome_length)
    temp0: str = chromosome0[cross_point:]
    temp1: str = chromosome1[cross_point:]

    # swap
    temp_chrom_0: str = chromosome0[:cross_point] + temp1
    temp_chrom_1: str = chromosome1[:cross_point] + temp0

    if not is_valid_chromosome(temp_chrom_1) and not is_valid_chromosome(temp_chrom_0):
        crossover(chromosome0, chromosome1, chromosome_length)

    result: list = list()
    result.append(temp_chrom_0)
    result.append(temp_chrom_1)
    return result


def mutation(chromosome: str, length) -> str:
    """
    Unlike crossover, mutation involves altering the values of one or more loci. This
    technique creates new possibilities for the gene combinations that can be generated
    by crossover.
    Mutation can be carried out at either the gene level or the locus level:
	    1) At the gene level, a randomly selected gene can be replaced by a randomly
        generated allele.
	    2) At the locus level, where values are binary, randomly selected loci can be
	    toggled so that 1 becomes 0 and 0 becomes 1.

    :param chromosome: the chromosome will change it
    :param length: the number of genes
    :return:
    """
    result: list = list(chromosome)
    random_mutation_index: int = random.randint(0, length - 1)
    if result[random_mutation_index] == "1":
        result[random_mutation_index] = "0"
    else:
        result[random_mutation_index] = "1"
    return "".join(result)


def roulette_wheel_selection(population: list) -> str:
    """
    allocate segments of the wheel,
    first it calculate total fitness and normalise, then derive cumulative values
    second in part two: spinning the wheel to select the chromosome
    :param population: list contents of the chromosome in the
    :return: selected chromosome as a str
    """
    # part one: scale the values and calculate the normalization values
    fitness_data: list = [fitness_function(i) for i in population]
    min_value: int = min(fitness_data)
    max_value: int = max(fitness_data)
    range_value: int = max_value - min_value
    scaled_data: list = [(x - min_value) / range_value for x in fitness_data]
    selection_probs: list = [x / sum(scaled_data) for x in scaled_data]

    # part two: selection of two the parents:

    return population[npr.choice(len(population), p=selection_probs)]


def decode_binary_string(binary: str) -> list:
    """
    decode the binary string into a decimal value
     ie 0001 0100 1001 0111 1001 0100 0101 0011 --> [1, 4, 9, 7, 9, 4, 5, 3]
        which is the values of 'a' through 'h'.
    :param binary: string (just one chromosome in the population).
    :return: list of the values in chromosome and decoded genes.
    """
    result: list = []
    for i in range(0, len(binary), 4):
        x = int(binary[i: i + 4], 2)
        result.append(x)
    return result


def chose_best_result(population: list) -> list:
    """
    this function choose the minimum chromosome who has a minimum fitness function
    :param population: list of chromosomes
    :return: list, minimum chromosome who minimum fitness function
    """
    fitness_data: list = [decode_binary_string(i) for i in population]
    minimum_data: list = fitness_data[0]
    for i in fitness_data:
        if sum(i) < sum(minimum_data):
            minimum_data = i

    return minimum_data


def main() -> None:
    """
    main function which has the loop
    :return:
    """
    # genetic algorithm parameters
    crossover_probability: float = 0.7
    mutation_probability: float = 0.01
    iterations_number: int = 100
    population_number: int = 5
    chromosome_length: int = 32

    # initial population
    population: list = init_first_population(population_number, chromosome_length)
    print("the initial population is")
    for i in population:
        print("\tchromosome: " + i + f"\thas fitness function = {fitness_function(i):3.1f} decoded string\t",
              decode_binary_string(i))

    print('\n')

    # main loop
    for iteration in range(iterations_number):
        current_population: list = population
        selected_chromosomes: list = []
        count: int = 0

        # this loop for selected the best chromosome with minimum fitness function
        while count / len(population) < crossover_probability:
            temp_parent: str = roulette_wheel_selection(population)
            if temp_parent not in selected_chromosomes:
                selected_chromosomes.append(temp_parent)
                count += 1

        # creating the new generation of cressover
        new_generation: list = []
        for i in range(0, len(selected_chromosomes) - 1, 2):
            cross_over_result = crossover(selected_chromosomes[i],
                                          selected_chromosomes[i + 1],
                                          len(population[i]))
            for j in cross_over_result:
                if is_valid_chromosome(j):
                    new_generation.append(j)

        for i in current_population:
            if i not in selected_chromosomes:
                new_generation.append(i)

        # make mutation on a random gene of random chromosomes
        while True:
            # mutation
            random_selection = random.randint(0, len(new_generation) - 1)
            mutated_chromosome = mutation(new_generation[random_selection], chromosome_length)
            if is_valid_chromosome(mutated_chromosome):
                new_generation[random_selection] = mutated_chromosome
                break

        current_population = new_generation

    # final results printed
    best_solution: list = chose_best_result(current_population)
    print("best solution is:")
    print(best_solution)

    return None


if __name__ == '__main__':
    print("*---------Genetic Algorithm implementation -------*\n"
          "Coded By: Mohammed S. Abu-daf\n"
          "ID: 120190917\n"
          "about:\n"
          "\tthis programs implement the genetic algorithm to minimize the result of fitness"
          "function -attached in info-, for the detail of the program open the file as .txt\n"
          "info:\n"
          "\tthe number of iteration is 50\n"
          "\tfitness function is f = (a+b) - (c+d) + (e+f) - (g+h)\n"
          "\tcrossover population is 0.7\n"
          "\tmutation population is 0.01\n"
          "requirments:\n"
          "\tnumpy lib to run correctly\n")
    main()
    input('Press ENTER to exit')
