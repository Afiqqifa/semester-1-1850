
def func_1(lst_value): 
    '''
    takes a list of numbers as a parameter and each number at every index is addded. Then finds the average
    write your docstring to explain the function 
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value

print(func_1([1,2,3,4]))