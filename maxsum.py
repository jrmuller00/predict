#
# test code for finding the max sum
# of contiguous integers in a list
# 
# python 2.7.4

import sys

def maxListSum(intList):
    """
    maxListSum will return the maximum sum 
    of two contiguous intergers in the 
    input list 'intList'.  
    """
    #
    # check that the list has more than two 
    # values, if not return 0 otherwise
    # proceed to find max
    if len(intList) < 2:
        maxSum = 0
    else:
        #
        # set the value for maxSum to the 
        # first sum in the list

        maxSum = intList[0] + intList[1]

        #
        # create a running sum starting from each 
        # value in the list and compare to 
        # maxSum value

        for i in range(1, len(intList) -1):
            runningSum = intList[i] + intList[i-1]
            if maxSum < runningSum:
                maxSum = runningSum
            for j in range(i+1,len(intList)):
                runningSum = runningSum + intList[j]
                if maxSum < runningSum:
                    maxSum = runningSum
        
    return maxSum


def main():
#
# set the list as in the example
    myList = [-10,2,3,-2,5,-15]
    print maxListSum(myList)


if __name__ == '__main__':
    main()

