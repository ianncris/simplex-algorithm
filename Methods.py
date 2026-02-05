from FractionNumber import FractionNumber

def build_matrix(matrix, lines, columns):

    # Print the current number of the line.
    for num_line in range(lines):
        print("Line n'"+str(num_line+1))
        for num_column in range(columns):

            # Get the fraction in input.
            number = int(input("Numerator n' "+str(num_column+1)+": "))
            if number != 0:
                denominator = int(input("Denominator n' "+str(num_column+1)+": "))
                matrix[num_line][num_column] = FractionNumber(number, denominator)
            else:
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
                print(matrix[x][y].print_number())
    print("\n")

def fix_matrix(matrix, line, column):
    number = int(input("Numerator: "))
    if number != 0:
        denominator = int(input("Denominator: "))
        matrix[line-1][column-1] = FractionNumber(number, denominator)
    else:
        matrix[line-1][column-1] = FractionNumber(number, 1)

def primal_pivot(matrix, lines, columns, l):

    f1: FractionNumber = None
    t = 1

    # Calculate the pivot row for the primal simplex.
    for i in range(1, lines):
        if matrix[i][l].numerator() > 0 and matrix[i][l].denominator() > 0:
            f2: FractionNumber = matrix[i][columns - 1].division(matrix[i][l])
            if f1 == None or f2.minor_major(f1):
                f1 = f2
                t = i

    print("t calculated: " + str(t) + "\n")
    return t

def dual_pivot(matrix, columns, c):

    f1: FractionNumber = None
    h = 0
    for i in range(columns - 1):

        # Calculate the column pivot for the dual simplex.
        if matrix[c][i].numerator() < 0:
            abs_val = FractionNumber(-matrix[c][i].numerator(), matrix[c][i].denominator())
            f2: FractionNumber = matrix[0][i].division(abs_val)
            if f1 == None or f2.minor_major(f1):
                f1 = f2
                h = i

    print("h calculated: " + str(h + 1) + "\n")
    return h

def pivot_new_matrix(pivot_matrix, t, h):

    line_t = pivot_matrix[t]
    pivot_element = line_t[h]
    new_matrix = [[None for _ in range(len(pivot_matrix[0]))] for _ in range(len(pivot_matrix))]

    # Calculate the new matrix with the operation of the pivot.
    for i in range(len(pivot_matrix)):
        if i == t:
            for j in range(len(pivot_matrix[0])):
                new_matrix[i][j] = pivot_matrix[i][j].division(pivot_element)
        else:
            coeff = pivot_matrix[i][h]
            for j in range(len(pivot_matrix[0])):
                new_matrix[i][j] = pivot_matrix[i][j].subtraction((coeff.division(pivot_element)).multiplication(line_t[j]))

    return new_matrix