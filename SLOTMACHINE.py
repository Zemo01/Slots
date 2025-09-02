
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") # Concatenation done here // str(MAX_LINES) converts the max lines to a string for this user prompt // imbeds values into strings
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #one way of comparing values. Check if a vaule is inbetween two values this way.
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on EACH line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") #f string ( ${var} ) allows for variables in a string. // second way to imbed values into a string
        else:
            print("Please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")



main()
