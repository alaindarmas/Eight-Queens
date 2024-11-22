#Checks if placing a queen is valid
def isValid(queens):
   
    #Stores number of queens placed
    n = len(queens)  
    for i in range(n):
        for j in range(i + 1, n):
            #Checks if the queens are in the same column or on the same diagonal
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                #Returns False if there is a conflict
                return False
    #Returns True if no conflicts are found
    return True

#Solves the Eight Queens Problem using brute force
def bruteForce8Queens():
    
    #List used to store the valid solutions
    solutions = []

    #Step counter used to count the number of placement attempts
    stepCounter = 0

    #Nested loops to generate all configurations
    for q1 in range(8):
        for q2 in range(8):
            for q3 in range(8):
                for q4 in range(8):
                    for q5 in range(8):
                        for q6 in range(8):
                            for q7 in range(8):
                                for q8 in range(8):
                                    #Increments the step counter for each configuration
                                    stepCounter += 1

                                    #Creates the current configuration
                                    queens = [q1, q2, q3, q4, q5, q6, q7, q8]

                                    #Checks if the configuration is valid
                                    if isValid(queens):
                                        #Adds a copy of the valid solution to the solutions list
                                        solutions.append(queens[:])

    #Returns the list of valid solutions and the step counter
    return solutions, stepCounter

#Solves the Eight Queens Problem using brute force with pruning (2D board)
def bruteForceWithPruning():

    #Initializes an empty 8x8 chessboard
    board = [[0 for _ in range(8)] for _ in range(8)]
    
    #List used to store the valid solutions
    solutions = []
    
    #Step counter used to count the number of placement attempts
    stepCounter = 0

    def canPlaceQueen(board, row, col):
        
        for i in range(row):
            #Checks column
            if board[i][col] == 1:
                return False
            #Checks left diagonal
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
                return False
            #Checks right diagonal
            if col + (row - i) < 8 and board[i][col + (row - i)] == 1:
                return False
        return True

    def solve(row):
        nonlocal stepCounter
        if row == 8:
            solution = [row.index(1) for row in board]
            solutions.append(solution)
            return

        for col in range(8):
            stepCounter += 1
            if canPlaceQueen(board, row, col):
                #Places the queen
                board[row][col] = 1
                #Recurse to the next row
                solve(row + 1)
                #Backtracks and removes the queen
                board[row][col] = 0

    #Starts solving from the first row
    solve(0)

    #Returns the list of valid solutions and the step counter
    return solutions, stepCounter

#Prints a solution in a readable chessboard format
def printBoardToConsole(solution, count):
    
    #Prints the solution number
    print(f"Solution #{count}")

    #Iterates through each row in the solution
    for i in range(len(solution)):
        #Initializes a row with empty squares
        row = ['**'] * len(solution)

        #Places a queen in the appropriate column
        row[solution[i]] = "Q "

        #Prints the row as a space-separated string
        print(" ".join(row))

    #Adds a blank line for readability
    print()

#Executes the program
def main():
    """
    Main function to handle user interaction, execute the selected algorithm,
    and display the results.
    """
    while True:
        #Displays a welcome message
        print("Welcome to the Eight Queens Problem")

        #Displays menu options
        print("1. Brute Force")
        print("2. Brute Force with Pruning")
        print("3. End Program")

        #Prompts the user to enter their choice
        choice = input("Enter your choice (1-3): ").strip()

        #If the user selects brute force
        if choice == '1':
            #Informs the user that the brute force solution is running
            print("Running Brute Force Solution...")

            #Executes the brute force algorithm
            solutions, steps = bruteForce8Queens()

            #Displays each valid solution
            print(f"Displaying solutions for Brute Force:")
            for count, solution in enumerate(solutions, 1):
                #Prints each solution in a chessboard format
                printBoardToConsole(solution, count)

            #Displays the total number of steps taken
            print(f"The end\nBrute Force\nNumber of steps: {steps}")

            #Displays the total number of valid solutions found
            print(f"Number of solutions found: {len(solutions)}")

        #If the user selects brute force with pruning
        elif choice == '2':
            #Informs the user that the brute force with pruning solution is running
            print("Running Brute Force with Pruning Solution...")

            #Executes the brute force with pruning algorithm
            solutions, steps = bruteForceWithPruning()

            #Displays each valid solution
            print(f"Displaying solutions for Brute Force with Pruning:")
            for count, solution in enumerate(solutions, 1):
                #Prints each solution in a chessboard format
                printBoardToConsole(solution, count)

            #Displays the total number of steps taken
            print(f"The end\nBrute Force with Pruning\nNumber of steps: {steps}")

            #Displays the total number of valid solutions found
            print(f"Number of solutions found: {len(solutions)}")

        #If the user selects to end the program
        elif choice == '3':
            #Displays a goodbye message
            print("Did I get an A? :)")
            #Exits the loop to end the program
            break  

        #If the user enters an invalid choice
        else:
            #Displays an error message and ask the user to restart
            print("Invalid choice. Please select a valid option.")

#Entry point of the program
if __name__ == "__main__":
    #Calls the main function to start the program
    main()
