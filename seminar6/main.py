def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Пример использования
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18]
x = 12
result = binary_search(arr, x)
if result != -1:
    print(f"Элемент найден в индексе {result}")
else:
    print("Элемент не найден")