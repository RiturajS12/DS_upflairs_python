list = [10,22,88,2,36,6,2,45,75,37]

def avg_finder(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

def even_finder(list):
    container = []
    for i in list:
        if i % 2 == 0:
            container.append(i)
    return container

def avg_even_finder(container):
    sum = 0
    for i in container:
        sum += i
    return sum/len(container)

def my_min(list):
    min = None
    for i in list:
        if min is None or i < min:
            min = i
    return min

def my_max(list):
    max = None
    for i in list:
        if max is None or i > max:
            max = i
    return max

print("Average: ",avg_finder(list))
print("Even in the list: ",even_finder(list))
print("Average of even: ",avg_even_finder(even_finder(list)))
print("Min: ",my_min(list))
print("Max: ",my_max(list))