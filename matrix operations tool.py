import numpy as np

def input_matrix(size):
    """Function to input a matrix from the user"""
    print(f"\nEnter {size}x{size} matrix:")
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            while True:
                try:
                    value = float(input(f"Enter element at position ({i+1},{j+1}): "))
                    row.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number!")
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, title="Matrix"):
    """Function to display a matrix in a formatted way"""
    print(f"\n{title}:")
    for row in matrix:
        print("|", end=" ")
        for element in row:
            print(f"{element:8.2f}", end=" ")
        print("|")

def matrix_operations_tool():
    """Main function for the Matrix Operations Tool"""
    print("\n" + "="*50)
    print("MATRIX OPERATIONS TOOL".center(50))
    print("="*50)
    
    while True:
        print("\nMain Menu:")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Matrix Transpose")
        print("5. Matrix Determinant")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '6':
            print("\nThank you for using the Matrix Operations Tool!")
            break
            
        if choice in ['1', '2', '3']:
            try:
                size = int(input("Enter the size of square matrices (e.g., 2 for 2x2): "))
                if size < 1:
                    print("Size must be at least 1!")
                    continue
                    
                print("\nMatrix A:")
                A = input_matrix(size)
                display_matrix(A, "Matrix A")
                
                print("\nMatrix B:")
                B = input_matrix(size)
                display_matrix(B, "Matrix B")
                
                if choice == '1':
                    result = np.add(A, B)
                    display_matrix(result, "Addition Result (A + B)")
                elif choice == '2':
                    result = np.subtract(A, B)
                    display_matrix(result, "Subtraction Result (A - B)")
                elif choice == '3':
                    result = np.matmul(A, B)
                    display_matrix(result, "Multiplication Result (A × B)")
                    
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                
        elif choice == '4':
            try:
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                if rows < 1 or cols < 1:
                    print("Rows and columns must be at least 1!")
                    continue
                    
                matrix = []
                print(f"\nEnter {rows}x{cols} matrix:")
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        while True:
                            try:
                                value = float(input(f"Enter element at position ({i+1},{j+1}): "))
                                row.append(value)
                                break
                            except ValueError:
                                print("Please enter a valid number!")
                    matrix.append(row)
                
                matrix = np.array(matrix)
                display_matrix(matrix, "Original Matrix")
                result = np.transpose(matrix)
                display_matrix(result, "Transposed Matrix")
                
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                
        elif choice == '5':
            try:
                size = int(input("Enter the size of square matrix (e.g., 2 for 2x2): "))
                if size < 1:
                    print("Size must be at least 1!")
                    continue
                    
                matrix = input_matrix(size)
                display_matrix(matrix, "Input Matrix")
                
                if size == 1:
                    det = matrix[0][0]
                else:
                    det = np.linalg.det(matrix)
                
                print(f"\nDeterminant of the matrix: {det:.2f}")
                
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if _name_ == "_main_":
    matrix_operations_tool()