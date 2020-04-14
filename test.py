list1 = [1, 2, 3]
list2 = [1, 3, 4]
sum_list = []


for (item1, item2) in zip(list1, list2):
    sum_list.append(item1-item2)

print(sum_list)