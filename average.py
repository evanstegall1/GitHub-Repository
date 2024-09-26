def average(int_arr):
    return sum(int_arr) / len(int_arr)

def get_user_input(msg: str):
    int_arr = [int(num) for num in input(msg).split()]
    return int_arr

def run():
    int_arr = get_user_input("Enter a list of integers separated by spaces: ")
    avg = average(int_arr)
    print(f"The average of these numbers is {avg}")

if __name__ == '__main__':
    run()

    