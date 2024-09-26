def sum(a: int, b: int):
    return a + b

def get_user_input(msg: str) -> tuple[int, int]:
    a, b = map(int, input(msg).split())
    return a, b

def run():
    a, b = get_user_input("Enter two integers separated by a space: ")
    print(f"Sum is: {sum(a, b)}")

if __name__ == '__main__':
    run()
    
