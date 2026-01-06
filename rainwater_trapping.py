def trapping_rainwater(array):
    left = 0
    max_left_value = array[left]
    right = len(array)-1
    max_right_value = array[right]
    total = 0
    while left != right:
        if max_left_value <= max_right_value:
            left+=1
            max_left_value = max(max_left_value,array[left])
            water = max_left_value-array[left]
            total += water
            
        if max_right_value < max_left_value:
            right-=1
            max_right_value = max(max_right_value,array[right])
            water = max_right_value-array[right]
            total+=water
            
    return total

print(trapping_rainwater([0,1,0,2,1,0,1,3,2,1,2,1]))