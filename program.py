def find_roots(coefficients, accuracy):
    if len(coefficients) > 2:
        search_in = find_roots(derivate(coefficients), accuracy)
    else:
        search_in = []

    search_in.insert(0, -10)
    search_in.append(10)

    results = []
    for i in range(len(search_in) - 1):
        start = search_in[i]
        end = search_in[i+1]
        if f_x(coefficients, start) > 0: start, end = end, start
        while True:
            pos = (start + end)/2
            result = f_x(coefficients, pos)

            if result < 0: start = pos
            else: end = pos
            
            if abs(end - start) < 1/pow(10, accuracy):
                break
        if abs(f_x(coefficients, end)) < 0.001:
            results.append(round(end, accuracy))
    return results
            
def derivate(coefficients):
    result = []
    for i in range(1, len(coefficients)):
        result.append(coefficients[i]*i)
    return result

def f_x(coefficients, x):
    result = 0
    for i in range(0, len(coefficients)):
        result += pow(x, i)*coefficients[i]
    return result

print(find_roots([-14, 11, -30, 1, -12, 4], 10))
#print(find_roots([-10, 1, -3, 1, -3, 1], 0.00000001))
#print(find_roots([6, -72, 60], 0.00000001))
