def reverse_list(list):
    reverse_list = []
    boyut = len(list)
    for i in range(0,boyut):
        reverse_list.append(list[boyut-i-1][::-1])
    return reverse_list
list =  [[1, 2], [3, 4], [5, 6, 7]]
print (reverse_list(list))
