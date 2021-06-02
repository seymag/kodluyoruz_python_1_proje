def flatten_func(liste):
    flat_liste = []
    for i in liste:
        if type(i) is list:
            flat_liste.extend(flatten_func(i))
        else:
            flat_liste.append(i)
    return flat_liste

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_func(liste))
