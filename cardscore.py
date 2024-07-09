def maxScore(cardPoints, k):
    n = len(cardPoints)
    total_points = sum(cardPoints)
    if k == n:
        return total_points
    
    subarray_length = n - k
    min_subarray_sum = float('inf')
    current_subarray_sum = 0
    
    for i in range(subarray_length):
        current_subarray_sum += cardPoints[i]
    
    min_subarray_sum = current_subarray_sum
    
    for i in range(subarray_length, n):
        current_subarray_sum += cardPoints[i] - cardPoints[i - subarray_length]
        min_subarray_sum = min(min_subarray_sum, current_subarray_sum)
    
    return total_points - min_subarray_sum

cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(maxScore(cardPoints, k)) 
