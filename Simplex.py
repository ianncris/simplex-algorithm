from Methods import *

def main():
    
    print("Simplex calculator:")
    print("- Every denominator equals to 0 will be converted to 1.")
    print("- The numbers of lines and columns must be at least 2.")
    print("- The calculator works for primal simplex or dual. \n")
        
    # Let the user choose between primal simplex or dual.
    simplex_choice = input("Choose primal simplex or dual: (p/d) ").lower()

    # Get the number of lines and columns of the matrix.
    lines = int(input("Select the numbers of lines: "))
    columns = int(input("Select the numbers of columns: "))
    print()

    # Create the initial matrix and invoce the method to allocate the numbers.
    matrix = [[None for _ in range(columns)] for _ in range(lines)]
    matrix = initialize_matrix(matrix, lines, columns)

    choice = input("The matrix is correct? (y/n) ").lower()
    while choice == 'n':

        line = int(input("Number of line: "))
        column = int(input("Number of column: "))
        fix_matrix(matrix, line, column)
        print_matrix(matrix, lines, columns)
        choice = input("The matrix is correct? (y/n) ").lower()
    
    if simplex_choice == 'p' and lines >= 2 and columns >= 2:
        while simplex_choice == 'p':

            result = simplex_primal(matrix, lines, columns)
            
            # If the matrix not upgrade anymore, we can shut down the program.
            simplex_choice = input("Do you want to continue? (y/n) ").lower()
            matrix = result
            if simplex_choice == 'y':
                simplex_choice = 'p'
    elif simplex_choice == 'd' and lines >= 2 and columns >= 2:
        while simplex_choice == 'd':

            result = simplex_dual(matrix, lines, columns)

            # If the matrix not upgrade anymore, we can shut down the program.
            simplex_choice = input("Do you want to continue? (y/n) ").lower()
            matrix = result
            if simplex_choice == 'y':
                simplex_choice = 'd'
    else:
        print("Invalid choice, closing...")
    print("End of the program.")
main()