# Ultimate sort method that takes forever to run take one
import random

def sorted(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True

def randomize(a):
    for i in range(0,len(a)):
        temp = a[i]
        rand = random.randrange(0,len(a))
        a[i] = a[rand]
        a[rand] = temp

def main():
    a = []
    n = 10
    for i in range(0,n):
        a.append(random.randrange(0,n))
    while(not sorted(a)):
        randomize(a)
        print a
    print a

main()


'''
    If the list is somewhat sorted at point don't switch?
    break up the sorts into smaller randomize sections
    determine if sorted. if not, stop

'''
