import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: py gcd_solver.py <number1> <number2>")
        return

    try:
        a = int(argv[0])
        b = int(argv[1])
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    
    assert a > b

    result = euclidian_algorithm(a, b)
    result_chatGPT = euclidian_algorithm_chatGPT(a, b)

    print("My result: {}".format(result))
    print("ChatGPT's result: {}".format(result_chatGPT))

# My implementation based on this doc: https://math.fel.cvut.cz/cz/lide/habala/teaching/dma/dmap01.pdf
def euclidian_algorithm(a, b):
    r = [a, b]
    A = [1, 0]
    B = [0, 1]

    k = 0
    while r[k + 1] > 0:
        k += 1
        q = r[k - 1] // r[k]
        r.append(r[k - 1] - q * r[k])
        A.append(A[k - 1] - q * A[k])
        B.append(B[k - 1] - q * B[k])
    return r[k]

# ChatGPT's implementation :(
def euclidian_algorithm_chatGPT(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
   main(sys.argv[1:])