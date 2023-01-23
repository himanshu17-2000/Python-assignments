import random
  
def random_num_from_list(list):
    print(random.choice(list))

def random_num_between_range(start , end):
    print(random.randint(start, end))

def random_shuffling_of_iterabel(itrr):
    random.shuffle(itrr)
    print(itrr)

list = [1, 2, 3, 4, 5, 6]
random_num_from_list(list)

random_num_between_range(10 , 150)

random_shuffling_of_iterabel(list)