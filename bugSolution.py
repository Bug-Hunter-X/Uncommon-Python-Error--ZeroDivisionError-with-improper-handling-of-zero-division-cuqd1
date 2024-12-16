def function_with_uncommon_error_solution(a, b):
    if b == 0:
        return float('inf') if a > 0 else float('-inf') if a < 0 else 0
    else:
        return a / b

result = function_with_uncommon_error_solution(10, 0) 
print(result)