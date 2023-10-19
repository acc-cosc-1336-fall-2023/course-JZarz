def create_tuples(num):
    num = (1, 2, 3, 4, 5) # tuple
    print (num)

    for i in num:
        print (i)

    for i in range(0, len(num)):
        print(num[i])

def create_list_w_tuple():
    nums = (1,2,3,4)
    create_list = list(nums)
    print(create_list)