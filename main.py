import numpy as np, os

def encrypt(message, row, column, cell_totals):
    message_list = list(message)
    for i in range(cell_totals):
        if len(message_list) < cell_totals:
            message_list += '_'

    save_file =  input("Save file to txt? [y/n]: ")
    if save_file == 'y':
        os.system("cls")
        with open(f"encrypt.txt", 'w') as f:
            try:
                reshape = (np.array(message_list).reshape(column, row))
                transpose = (reshape.T).reshape(cell_totals)
                
                f.write(f"Row: {row}\n")           
                f.write(f"Column: {column}\n")
                f.write(f"Cell totals: {cell_totals}\n")
                
                f.write(f'\nNormal Text: {message}\n{reshape}')
                f.write(f'\nTransposes Text:\n{reshape.T}\n')
                
                f.write(f'\nCipher text: {"".join(transpose)}')
            except:
                print("Cell totals to short")
                
    elif save_file == 'n':
        os.system("cls")
        try:
            reshape = (np.array(message_list).reshape(column, row))
            transpose = (reshape.T).reshape(cell_totals)
            
            print(f"Row: {row}")           
            print(f"Column: {column}")
            print(f"Cell totals: {cell_totals}")
            
            print(f'\nNormal Text: {message}\n{reshape}')
            print(f'\nTransposes Text:\n{reshape.T}')
            
            print(f'\nCipher text: {"".join(transpose)}\n')
        except:
            print("Cell totals to short")
    
    
def decrypt(message, row, column, cell_totals):
    message_list = list(message)
    for i in range(cell_totals):
        if len(message_list) < cell_totals:
            message_list += '_'
    
    save_file =  input("Save file to txt? [y/n]: ")
    if save_file == 'y':
        os.system("cls")
        with open("decrypt.txt", 'w') as f:
            try:
                reshape = (np.array(message_list).reshape(row, column))
                transpose = (reshape.T).reshape(cell_totals)
                
                f.write(f"Row: {row}\n")           
                f.write(f"Column: {column}\n")
                f.write(f"Cell totals: {cell_totals}\n")
                
                f.write(f'\nNormal Text: {message}\n{reshape}')
                f.write(f'\nTransposes Text:\n{reshape.T}\n')
                
                f.write(f'\nCipher text: {"".join(transpose)}')
            except:
                print("Cell totals to short")
            
    elif save_file == 'n':
        os.system("cls")
        try:
            reshape = (np.array(message_list).reshape(row, column))
            transpose = (reshape.T).reshape(cell_totals)
            
            print(f"Row: {row}")           
            print(f"Column: {column}")
            print(f"Cell totals: {cell_totals}")
            
            print(f'\nNormal Text: {message}\n{reshape}')
            print(f'\nTransposes Text:\n{reshape.T}')
            
            print(f'\nCipher text: {"".join(transpose)}\n')
        except:
            print("Cell totals to short")
            

message = input("Input message: ")
row = int(input("Input row: "))
column = int(input("Input column: "))
cell_totals = row * column
method = input("Select method: [e/d]: ").lower()

if method == "e":
    encrypt(message, row, column, cell_totals)
elif method == "d":
    decrypt(message, row, column, cell_totals)