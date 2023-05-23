def solution(arr1, arr2):
    행 = len(arr1)
    열 = len(arr1[0])
    arr3 = arr1.copy()
    
    for i in range(행):
        for j in range(열):
            arr3[i][j] = arr1[i][j] + arr2[i][j]

    return arr3    
