def merge_sort(arr):
    if len(arr) > 1:
        result = []
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        while len(left) > 0 or len(right) > 0:
            if len(left) == 0:
                result.extend(right)
                break
            elif len(right) == 0:
                result.extend(left)
                break
            
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        return result
    else:
        return arr

arr = [2, 6, 3, 4, 1, 5]

print(merge_sort(arr))
