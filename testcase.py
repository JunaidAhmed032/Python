import random

if __name__ == '__main__':
    check = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(3):
        instance = []
        for x in range(3):
            instance.append(random.randint(1,9))
        if instance not in check:
            print("added")
            check.append(instance)
        else:
            print(instance )
            print("already exists")
    print(check)

