import timeit
def count_letters(s,c):
    sum = 0
    i = s.find(c,0)
    while i >=0 :
        sum += 1
        i = s.find(c,i+1)
    return sum

def  print_count_letter(s,c):
    print("Total letter {} in words {} : {}".format(c,s,count_letters(s,c)))

timeit.timeit('''count_letters("banana","a")''')