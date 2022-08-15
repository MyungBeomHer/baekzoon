list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]

arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    arr_Set = set(arr[i])
    count = set(list1) - arr_Set
    print(count)
    print(set(list1) - arr_Set)
    print(len(set(list1) - arr_Set))