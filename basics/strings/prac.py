# Reversing an array
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


A = [13, 56, 565, 34, 67, 45, 67, 4]
print(A)

reverse_array(A, 0, len(A) - 1)
print(A)
