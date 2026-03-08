from FractionNumber import FractionNumber

def initialize_matrix(matrix, lines, columns):

    # Print the current number of the line.
    for num_line in range(lines):
        print("Line n'"+str(num_line+1))
        for num_column in range(columns):

            # Get the fraction in input.
            number = int(input("Numerator n' "+str(num_column+1)+": "))
            if number != 0:
                denominator = int(input("Denominator n' "+str(num_column+1)+": "))
                matrix[num_line][num_column] = FractionNumber(number, denominator)
            elif number == 0:
                matrix[num_line][num_column] = FractionNumber(number, 1)

        # After every line the program print the current matrix.
        print_matrix(matrix, lines, columns)
    return matrix

def print_matrix(matrix, lines, columns):
    for x in range(lines):
        print("Line n'"+str(x+1) + "\n")
        for y in range(columns):

            # If the cell of the matrix does not have already the number, print a dash.
            if matrix[x][y] is None:
                matrix[x][y] = '-'
                print(matrix[x][y])
            else:
                print(matrix[x][y].printnum())
    print("\n")

def fix_matrix(matrix, line, column):
    number = int(input("Numerator: "))
    if number != 0:
        denominator = int(input("Denominator: "))
        matrix[line-1][column-1] = FractionNumber(number, denominator)
    else:
        matrix[line-1][column-1] = FractionNumber(number, 1)

def simplex_primal(matrix, lines, columns):

    # Find the pivot in the matrix and update it.
    num_value = FractionNumber(0)
    index_column = 0
    for i in range(columns - 1):
        if num_value.compare(matrix[0][i]):
            num_value = matrix[0][i]
            index_column = i
    index_line = primal_pivot(matrix, lines, columns, index_column)
    result = pivot_new_matrix(matrix, index_line, index_column)
    print_matrix(result, lines, columns)
    return result

def primal_pivot(matrix, lines, columns, l):

    f1: FractionNumber = None
    t = 1

    # Calculate the pivot row for the primal simplex.
    for i in range(1, lines):
        if matrix[i][l].num > 0 and matrix[i][l].den > 0:
            f2: FractionNumber = matrix[i][columns - 1].divide(matrix[i][l])
            if f1 == None or f2.compare(f1):
                f1 = f2
                t = i

    print("pivot row calculated: " + str(t) + "\n")
    return t

def simplex_dual(matrix, lines, columns):

    # Find the pivot in the matrix and update it.
    num_value = FractionNumber(0)
    index_line = 0
    for i in range(1, lines):
        if num_value.compare(matrix[i][columns - 1]):
            num_value = matrix[i][columns - 1]
            index_line = i
    index_column = dual_pivot(matrix, columns, index_line)
    result = pivot_new_matrix(matrix, index_line, index_column)
    print_matrix(result, lines, columns)
    return result

def dual_pivot(matrix, columns, c):

    f1: FractionNumber = None
    column_pivot = 0
    for i in range(columns - 1):

        # Calculate the column pivot for the dual simplex.
        if matrix[c][i].num < 0:
            abs_val = FractionNumber(-matrix[c][i].num, matrix[c][i].den)
            f2: FractionNumber = matrix[0][i].div(abs_val)
            if f1 == None or f2.compare(f1):
                f1 = f2
                column_pivot = i

    print("pivot column calculated: " + str(column_pivot + 1) + "\n")
    return column_pivot

def pivot_new_matrix(pivot_matrix, row_pivot, column_pivot):

    line_t = pivot_matrix[row_pivot]
    pivot_element = line_t[column_pivot]
    new_matrix = [[None for _ in range(len(pivot_matrix[0]))] for _ in range(len(pivot_matrix))]

    # Calculate the new matrix with the operation of the pivot.
    for i in range(len(pivot_matrix)):
        if i == row_pivot:
            for j in range(len(pivot_matrix[0])):
                new_matrix[i][j] = pivot_matrix[i][j].divide(pivot_element)
        else:
            coeff = pivot_matrix[i][column_pivot]
            for j in range(len(pivot_matrix[0])):
                new_matrix[i][j] = pivot_matrix[i][j].subtract((coeff.divide(pivot_element)).multiply(line_t[j]))

    return new_matrix