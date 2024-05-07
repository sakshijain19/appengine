def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    pos = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            pos = mid
            break
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return pos

if __name__ == "__main__":
    n = int(input("Enter the size of array => "))
    arr = []
    print(f"Enter {n} Integers in ascending order =>")
    for _ in range(n):
        arr.append(int(input()))

    target = int(input("Enter the number you want to search => "))

    pos = binary_search(arr, target)

    if pos == -1:
        print(f"{target} is not present in the array")
    else:
        print(f"{target} is present in the array at position {pos}")
