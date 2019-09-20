# Kelvin modified on Sep 20, 2019
#
# If a recursive call starts at most one other, 
# we call this a linear recursion.
#

# Summing the elements of a sequence recursively
def linear_sum(S, n):
    """ Return the sum of the first n numbers of sequence S. """
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

# Reversing a sequence with recursion
def reverse(S, start, stop):
    """ Reverse elements in implicit slice S[start:stop]. """
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1) 

if __name__ == '__main__':

        data1 = [4, 3, 6, 2, 8]
        data2 = [1, 2, 3, 4, 5, 6]
        print('original data: ', data2)

        linear_sum_result = linear_sum(data1, 5)          # 4+3+6+2+8 
        # result = linear_sum(data1, 4)          # 4+3+6+2
        # result = linear_sum(data1, 3)          # 4+3+6
        print('linear_sum result: ', linear_sum_result)

        reverse(data2, 0, 6)
        print('reverse data: ', data2)
        


        


        


      
