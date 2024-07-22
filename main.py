from linear_fibonacci import linear_fibonacci
from linear_prime import linear_prime
from recursive_fibonacci import recursive_fibonacci
from recursive_prime import recursive_prime


def main():
    while True:
        number = input("Choose a natural number. I can calculate its fibonacci or show you all the prime numbers from 2 to it (or enter nothing to finish the execution): \n")
        if number == '':
            break
        if not number.isdecimal():
            print("You haven't chosen a natural number. Please, try again.\n")
            continue    
        option = int(input("Do you want me to calculate fibonacci (option 1) or prime sequence (option 2)? Enter the corresponding option number: \n"))
        mode = int(input("Do you want it to use the linear (option 1) or recursive (option 2) function? Enter the corresponding option number: \n"))
        if option == 1:
            if mode == 1:
                print(f"Using linear function. Fibonacci of {number} is {linear_fibonacci(int(number))}\n")
                continue
            elif mode == 2:
                print(f"Using recursive function. Fibonacci of {number} is {recursive_fibonacci(int(number))}\n")
                continue
        if option == 2:
            if int(number) < 2:
                print("For calculating the prime numbers, choose a greater number.\n")
                continue
            if mode == 1:
                print(f"Using linear function. The prime numbers from 2 to {number} are: {linear_prime(int(number))}\n")
                continue
            elif mode == 2:
                print(f"Using recursive function. The prime numbers from 2 to {number} are: {recursive_prime(int(number))}\n")
                continue

if __name__ == "__main__":
    main()
