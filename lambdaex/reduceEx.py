
from functools import reduce
def acculateValue(num1, num2):
    result = num1 + num2 

    return result

single_Element=reduce(acculateValue, [1,2,3,4,5])
print(single_Element)

