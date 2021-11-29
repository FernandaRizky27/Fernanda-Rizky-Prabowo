#random string
def randomString(x,n):
    for i in range(n):
        import random
        print(''.join(random.sample(x,len(x))))
randomString('hello', 8)