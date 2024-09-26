def fibonacci(n): 
    a = 0 
    b = 1 
    if n < 0: 
        print("Incorrect input")
    elif n == 0: return a 
    elif n == 1: return b 
    else: 
        for i in range(2, n): 
            c = a + b 
            a = b 
            b = c
        return b

def get_user_input():
    n = int(input())
    return n

def run():
    print("Enter an integer n to return the nth fibonacci value: ")
    n = get_user_input()
    print(f"The {n}th fibonacci value is {fibonacci(n)}")

if __name__ == '__main__':
    run()
    