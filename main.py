def rightmost_set_bit(n):
    return n & -n

num = 14  # Example number
print(f"Rightmost set bit of {num} is: {rightmost_set_bit(num)}")