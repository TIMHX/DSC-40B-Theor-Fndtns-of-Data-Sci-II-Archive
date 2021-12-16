def balance(left, right):

    # The worst complexity should be theta(m + n) = theta(n)
    # Look for a - b = (sum(left) - sum(right))/ 2
    sum1 = sum(left)
    sum2 = sum(right)

    target = (sum1 - sum2) / 2
    
    i, j = 0, 0
    diff_middle = float('inf')
    min_pair = (0, 0)
    while (i < len(left) and j < len(right)):
        diff = left[i] - right[j]
        
        # Save the closest result
        if diff_middle > abs(diff - target):
            diff_middle = abs(diff - target)
            min_pair = (i, j)
        if diff == target:
            return (i, j)
        # Look for a greater value in left
        elif diff < target:
            i += 1
        # Look for a greater value in right
        else:
            j += 1
    return min_pair
