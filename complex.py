import tkinter as tk

# submit values from tkinter window
def submit(choose):
    try:
        # get each value
        a1_value = float(a1_entry.get())
        a2_value = float(a2_entry.get())
        b1_value = float(b1_entry.get())
        b2_value = float(b2_entry.get())
        match choose:
            case 'sum':
                choose = 1
            case 'sub':
                choose = 2
            case 'mul':
                choose = 3
            case 'div':
                choose = 4
                
        
        status_label.config(text="All values are valid!", fg="green") # change status in window text
        main(a1_value, a2_value, b1_value, b2_value, choose)
    except ValueError:
        print("Please enter valid numbers.")
        status_label.config(text="Please enter valid numbers.", fg="red")

# function to change type
def format_number(num):
    # if number is not rational do int type
    return int(num) if num.is_integer() else round(num, 2)


def complex_sum(a1, a2, b1, b2):
    # z1 + z2
    imaginary_part = b1 + b2
    print(f'z1 + z2 = {format_number(a1 + a2)} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    result_label.config(text=f'z1 + z2 = {format_number(a1 + a2)} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return
  
    
def complex_sub(a1, a2, b1, b2):
    # z1 - z2
    imaginary_part = b1 - b2
    print(f'z1 - z2 = {format_number(a1 - a2)} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    result_label.config(text=f'z1 - z2 = {format_number(a1 - a2)} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return
   
    
def complex_mult(a1, a2, b1, b2):
    # z1 * z2
    imaginary_part = (a1 * b2) + (b1 * a2)
    print(f'z1 * z2 = {format_number((a1 * a2) - (b1 * b2))} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    result_label.config(text=f'z1 * z2 = {format_number((a1 * a2) - (b1 * b2))} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return
  
    
def complex_div(a1, a2, b1, b2):
    # z1 : z2
    imaginary_part = (b1 * a2 - a1 * b2) / (a2**2 + b2**2)
    print(f'z1 : z2 = {format_number((a1 * a2 + b1 * b2) / (a2**2 + b2**2))} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    result_label.config(text=f'z1 : z2 = {format_number((a1 * a2 + b1 * b2) / (a2**2 + b2**2))} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return


# user make a choose of operations
def choose():
    print('1 = z1 + z2, 2 = z1 - z2,\n3 = z1 * z2, 4 = z1 : z2')
    index = int(input('Enter option: '))
    if index >= 1 and index <= 5:
        return [True, index]
    return [False, 'Error']


# main work function
def main(a1, a2, b1, b2, choose):
    match choose:
        case 1:
            # z1 + z2
            complex_sum(a1, a2, b1, b2)
            return
        
        case 2:
            # z1 - z2
            complex_sub(a1, a2, b1, b2)
            return
        
        case 3:
            # z1 * z2
            complex_mult(a1, a2, b1, b2)
            return
        
        case 4:
            # z1 : z2
            complex_div(a1, a2, b1, b2)
            return
    

#! TKINTER =====================================================================
window = tk.Tk()

# window.geometry('200x500') # window size (width x height)
window.title('Complex numbers') # window title
window.iconphoto(True, tk.PhotoImage(file='function.png')) # change window icon

header = tk.Frame(window, background='red')
header.pack(fill='both', expand=True)

label = tk.Label(header, text='3.5. Complex numbers solving.', font=('Roboto', 18),  foreground='#fff', background='red') # create text in window with font settings
label.pack(pady=10) # pack the text with _y_ paddings into window

container = tk.Frame(window) # container for our complex numbers with background
container.pack(fill='both', expand=True, pady=15, padx=20) # pack the container into window

# a1
label_a1 = tk.Label(container, text='Enter a1')
label_a1.grid(row=0, column=0, pady=5, padx=5)
a1_entry = tk.Entry(container)
a1_entry.grid(row=1, column=0, pady=5, padx=5)

#a2
label_a2 = tk.Label(container, text='Enter a2')
label_a2.grid(row=0, column=1, pady=5, padx=5)
a2_entry = tk.Entry(container)
a2_entry.grid(row=1, column=1, pady=5, padx=5)

#b1
label_b1 = tk.Label(container, text='Enter b1')
label_b1.grid(row=2, column=0, pady=5, padx=5)
b1_entry = tk.Entry(container)
b1_entry.grid(row=3, column=0, pady=5, padx=5)

#b2
label_b2 = tk.Label(container, text='Enter b2')
label_b2.grid(row=2, column=1, pady=5, padx=5)
b2_entry = tk.Entry(container)
b2_entry.grid(row=3, column=1, pady=5, padx=5)

#submit buttons
btn_plus = tk.Button(container, text='Sum (+)', background='aliceblue', relief='groove', foreground='black', activeforeground='blue', pady=5, padx=6, command=lambda: submit(choose='sum'))
btn_plus.grid(row=4, column=0, columnspan=1, pady=15)

btn_sub = tk.Button(container, text='Sub (-)', background='aliceblue', relief='groove', foreground='black', activeforeground='blue', pady=5, padx=6, command=lambda: submit(choose='sub'))
btn_sub.grid(row=4, column=1, columnspan=1, pady=15)

btn_mult = tk.Button(container, text='Mul (*)', background='aliceblue', relief='groove', foreground='black', activeforeground='blue', pady=5, padx=6, command=lambda: submit(choose='mul'))
btn_mult.grid(row=5, column=0, columnspan=1, pady=15)

btn_div = tk.Button(container, text='Div (:)', background='aliceblue', relief='groove', foreground='black', activeforeground='blue', pady=5, padx=6, command=lambda: submit(choose='div'))
btn_div.grid(row=5, column=1, columnspan=1, pady=15)

# status block
status_label = tk.Label(container, text="Status: no response", font=('Roboto', 12), bg='lightgray', fg='black')
status_label.grid(row=6, column=0, columnspan=2, pady=10)

# result block
result_label = tk.Label(container, text="Update Result", font=("Roboto", 12), bg="#4CAF50", fg="white", relief="groove", bd=2, padx=10, pady=5)
result_label.grid(row=7, column=0, columnspan=2, pady=10)

window.mainloop() # starts the window loop



# foreground - text color
# relife='groove' - border
# active - onclick
# bd - border width
# lambda: f(x) - to allow send arguments x
# Frame - container
# expand - get all container size
# fill='both' - stretches vertically and horizontally