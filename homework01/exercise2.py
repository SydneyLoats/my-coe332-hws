def prime_num():
    for x in range(3, 100):
        
        for y in range(2, (int(x/2)+1)):
            if((x%y) == 0):
                break
        else:
            print(x)

prime_num()
