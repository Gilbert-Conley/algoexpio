def sum_lists(list1,list2):
    list1_sum = sum_list(list1)
    list2_sum = sum_list(list2)
    return list1_sum, list2_sum

def sum_list(lst):
    total = 0
    for num in lst:
        total+= num
    
    return total

sum1, sum2 = sum_lists([1,2,3,4],[-1,-2,-3,-4])
print(sum1,sum2)

