#----------Calculator Program----------
def calculator():
    print("*****CALCULATOR PROGRAM*****")
    print("Enter expressions like (1 + 2 - 3): ")
    print("Enter your expression: ")
    while True:
        user_data = input("Enter preferred expression or 'q' to quit : ")

        if user_data == 'q'.lower():
            print("Thanks for using this calculator app")
            break

        try:
            answer = eval(user_data)
            print(f"Result: {answer}")
        except Exception as e:
            print(f"Invalid expression. Error: {e}")


def main():

    calculator()

if __name__ == "__main__":
        main()