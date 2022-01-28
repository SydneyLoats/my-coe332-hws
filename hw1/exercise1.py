#even or odd

my_list = [3, 7, 12, 14, 5, 8, 19, 4, 11, 16]

def even_or_odd(list_in):
    for x in list_in:
        if (x%2 == 1):
            print("odd")
        else:
            print("even")

even_or_odd(my_list)
