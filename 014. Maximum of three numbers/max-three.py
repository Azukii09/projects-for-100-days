#define function for determine max number from 3 number
def max_three(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 > num3:
        return num2
    else:
        return num3

#user input
nums1 = int(input("Input numbers 1: "))
nums2 = int(input("Input numbers 2: "))
nums3 = int(input("Input numbers 3: "))
# Print output to the standard output device.
#with calling the function
print(max_three(nums1, nums2, nums3))