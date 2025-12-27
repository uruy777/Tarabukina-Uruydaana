# 1
"""def function(x, y):
    if x > 12:
        return 0
    if x == 12:
        if y:
            return 1
        else:
            return 0
    if x == 10:
        y = True
    return function(x + 1, y) + function(x + 2, y) + function(x * 2, y)
print(function(3, False))"""
# 2
"""def function(x):
    if x > 27 or x == 26:
        return 0
    if x == 27:
        return 1
    return function(x + 1) + function(2 * x + 1)
print(function(1))"""
# 3
"""def function(x):
    if x > 9:
        return 0 
    if x == 9:
        return 1 
    return function(x + 1) + function(x + 2)

print(function(1))"""