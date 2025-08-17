def sum_negatives_between_min_max(arr):
    if len(arr) == 0:
        return 0
    
    min_val = min(arr)
    max_val = max(arr)
    min_index = arr.index(min_val)
    max_index = arr.index(max_val)
    
    start = min(min_index, max_index)
    end = max(min_index, max_index)
    
    sum_neg = 0
    for num in arr[start + 1 : end]:
        if num < 0:
            sum_neg += num
    
    return sum_neg

# Пример использования
A = [3, -2, -5, 7, -1, 8, -4, 2]
result = sum_negatives_between_min_max(A)
print("Сумма отрицательных элементов между min и max:", result)