from FractionNumber import FractionNumber
from Methods import *

def main():
    
    print("Simplex calculator.")
    print("- Every denominator equals to 0 will be converted to 1.")
    print("- The calculator works for primal simplex or dual. \n")

    # Get the number of lines and columns of the matrix.
    lines = int(input("Select the numbers of lines: "))
    columns = int(input("Select the numbers of columns: "))
    print()

    # Create the initial matrix and invoce the method to allocate the numbers.
    matrix = [[None for _ in range(columns)] for _ in range(lines)]
    matrix = build_matrix(matrix, lines, columns)

    # Let the user verify the correct matrix
    choice = input("The matrix is correct? (y/n)")
    while choice == 'n':

        line = int(input("Number of line: "))
        column = int(input("Number of column: "))
        fix_matrix(matrix, line, column)
        print_matrix(matrix, lines, columns)
        choice = input("The matrix is correct? (y/n)")
        
    # Let the user choose between primal simplex or dual.
    choice = input("Choose primal simplex or dual: (p/d) ")
    
    if choice == 'p':
        while choice == 'p':

            # Find the pivot in the matrix and update it.
            num_value = FractionNumber(0)
            index_column = 0
            for i in range(columns - 1):
                if num_value.minor_major(matrix[0][i]):
                    num_value = matrix[0][i]
                    index_column = i
            index_line = primal_pivot(matrix, lines, columns, index_column)
            result = pivot_new_matrix(matrix, index_line, index_column)
            print_matrix(result, lines, columns)
            
            # If the matrix not upgrade anymore, we can shut down the program.
            choice = input("Do you want to continue? (y/n)").lower()
            matrix = result
            if choice == 'y':
                choice = 'p'
    elif choice == 'd':
        while choice == 'd':

            # Find the pivot in the matrix and update it.
            num_value = FractionNumber(0)
            index_line = 0
            for i in range(1, lines):
                if num_value.minor_major(matrix[i][columns - 1]):
                    num_value = matrix[i][columns - 1]
                    index_line = i
            index_column = dual_pivot(matrix, columns, index_line)
            result = pivot_new_matrix(matrix, index_line, index_column)
            print_matrix(result, lines, columns)

            # If the matrix not upgrade anymore, we can shut down the program.
            choice = input("Do you want to continue? (y/n)").lower()
            matrix = result
            if choice == 'y':
                choice = 'd'
    else:
        print("Invalid choice, closing...")
main()