import random


def get_random_number_with_desired_sum(sum):
    while sum > 0:
        num = random.randint(1, sum)
        yield num, x
        sum -= num


def get_weighted_spl_random_numbers_list(input_dict, desired_weight):
    """
        This function will return a list of random items
        having total sum is equal desired_weight
    """
    number_to_pick = input_dict.keys()
    solution_list = []
    current_weight = 0
    while current_weight != desired_weight:
        a_random_number = random.choice(number_to_pick)
        solution_list.append(a_random_number)
        number_to_pick.remove(a_random_number)
        current_weight = current_weight + input_dict[a_random_number]
        if current_weight > desired_weight:
            current_weight = 0
            solution_list = []
            number_to_pick = input_dict.keys()
    return solution_list
