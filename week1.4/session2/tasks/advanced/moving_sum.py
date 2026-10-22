"""
    THIS IS NOT FOR BEGINNER, PLEASE IGNORE THIS TASK IF YOU ARE
    NEW TO PROGRAMMING.

    Write a recursive function moving_cummulative_sum() that calculate the
    moving cummulative sum of integer values in a list and returns the
    new list. For example, given a list [5,6,7,1,2,3], the resulting list
    is [5,11,18,19,21,24].

    This is an open-ended question in which you are free to determine
    the number of parameters for the function, with the first argument is
    for the list such as moving_cummulative_sum(x) with x being the
    list to be operated on.
"""
def moving_cummulative_sum(lst):
    """
    This recursive function calculates the moving cumulative sum of integer
    values in a list and returns the new list.

    Args:
        lst (list): A list of integers.
    Returns:
        list: A new list containing the moving cumulative sum of the input list.
    """         
    # Base case: if the list is empty, return an empty list
    if not lst:
        return []
    # Recursive case: calculate the moving cumulative sum
    else:
        # Get the moving cumulative sum of the rest of the list
        rest_sum = moving_cummulative_sum(lst[:-1])
        # Calculate the current cumulative sum
        current_sum = lst[-1] + (rest_sum[-1] if rest_sum else 0)
        # Return the new list with the current cumulative sum appended
        return rest_sum + [current_sum]
print(moving_cummulative_sum([5, 6, 7, 1, 2, 3]))  # Output: [5, 11, 18, 19, 21, 24]