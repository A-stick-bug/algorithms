# difficulty: 2/5
# question source: https://www.geeksforgeeks.org/minimum-cost-to-convert-str1-to-str2-with-the-given-operations/

def find_cost(str1, str2):
    """
    :return: cost to convert str1 into str 2, cost of changing a to b is 1, cost of swapping 2 elements is abs(i-j)
            therefore, the swap operation should only be used if 2 letters next to each need to be switched, otherwise,
            just change it
    """
    str1 = list(str1)
    cost = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            # both i and the letter after it need to be switched
            if i < len(str1)-1 and str1[i+1] != str2[i+1]:
                cost += 1
                i += 1
            else:
                cost += 1
    return cost


print(find_cost("abb","bba"))