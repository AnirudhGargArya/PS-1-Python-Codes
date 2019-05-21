# def num_except(array_int):
#     max_arr_row = [0]*len(array_int[0])
#     for j in range(0, len(array_int[0])):
#         # for i in array_int[0:j+1]:
#         #     max_arr_row[j] = max
#         max_arr_row[j] = max(array_int[0:j,j+1][0])
#
#     print(max_arr_row)
#
# arr1 = [[1, 2, 3, 4], [5,7,9,0], [4,3,7,8], [4, 5, 6, 7]]
# print(arr1[:])
# print(max(j[0] for j in arr1))
# for i in range(1, 10):
#     print(i)
#
# num_except(arr1)


def num_except(int_arr):
    x=0
    for j in int_arr:
        x+=1
    int_max_row = [0]*x
    for i in int_arr:
        int_max_row[int_arr.index(i)] = max(i)
    print("The list of row maxes is : " + str(int_max_row))


    x=0
    for j in int_arr:
        x+=1
    int_min_row = [0]*x
    for i in int_arr:
        int_min_row[int_arr.index(i)] = min(i)
    print("The list of row mins is : " + str(int_min_row))

    int_max_col = [0]*len(int_arr[0])
    j=0
    for i in int_arr[0]:
        int_max_col[j] = max([_[j] for _ in int_arr])
        j+=1
    print("The list of column maxes is : " + str(int_max_col))

    int_min_col = [0]*len(int_arr[0])
    j=0
    for i in int_arr[0]:
        int_min_col[j] = min([_[j] for _ in int_arr])
        j+=1
    print("The list of column mins is : " + str(int_min_col))

    print("The largest element is : " + str(max(int_max_row)))
    print("The smallest element is : " + str(min(int_min_row)))


arr2 = [[99,1,2,3,5], [3,4,5,5,14], [6,7,8,8,3], [9,0,1,9,67]]
num_except(arr2)
