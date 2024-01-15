def happy_num(num):
    seen = set()
    while (num != 1) and (num not in seen):
        seen.add(num)
        l = sum([int(x)**2 for x in str(num)])
    return l == 1

#input num
#sum