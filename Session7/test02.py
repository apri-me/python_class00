import random

my_list = ['mohsen', 'radmehr', 'alireza', 'mahdi']
# random.shuffle(my_list)
new_list = random.sample(my_list, len(my_list))
print(my_list)
print(new_list)
