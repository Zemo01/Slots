import random #For random number generation



MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3 

symbol_count = {  #created a dictionary here
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] #list 
    for symbol, symbol_count in symbols.items(): #adds the number of symbols into the symbols list // .items gives key and value associated with a dictionary 
        for _ in range(symbol_count): # _ in python is an anon variable. Used for to not have an unsued variable if the count or itteration is not of importance 
            all_symbols.append(symbol)

    columns = [] #nested list // columns = [ [], [], [] ]
    for _ in range(cols): # _ in this case is col
        column = []
        current_symbols = all_symbols[:] # [:] to copy a list; aka "slice" operator
        for _ in range(rows): #in this case is row
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): #loops thru each row
        for i, column in enumerate(columns): #loop thru each column, only print the current row we are on. (this transposes out horizontal array into a vertical one)
            if i != len(columns) - 1:
                print(col[row], "|")
            else:
                print(column[row])

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
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient balance. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")



main()
