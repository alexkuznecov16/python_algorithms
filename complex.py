# function to change type
def format_number(num):
    # if number is not rational do int type
    return int(num) if num.is_integer() else round(num, 2)


def complex_sum(a1, a2, b1, b2):
    # z1 + z2
    imaginary_part = b1 + b2
    print(f'z1 + z2 = {format_number(a1 + a2)} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return
  
    
def complex_sub(a1, a2, b1, b2):
    # z1 - z2
    imaginary_part = b1 - b2
    print(f'z1 - z2 = {format_number(a1 - a2)} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return
   
    
def complex_mult(a1, a2, b1, b2):
    # z1 * z2
    imaginary_part = (a1 * b2) + (b1 * a2)
    print(f'z1 * z2 = {format_number((a1 * a2) - (b1 * b2))} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return
  
    
def complex_div(a1, a2, b1, b2):
    # z1 : z2
    imaginary_part = (b1 * a2 - a1 * b2) / (a2**2 + b2**2)
    print(f'z1 : z2 = {format_number((a1 * a2 + b1 * b2) / (a2**2 + b2**2))} {'+' if imaginary_part > 0 else '-'} {abs(format_number(imaginary_part))}i')
    return


# user make a choose of operations
def choose():
    print('1 = z1 + z2, 2 = z1 - z2,\n3 = z1 * z2, 4 = z1 : z2\n5 = each')
    index = int(input('Enter option: '))
    if index >= 1 and index <= 5:
        return [True, index]
    return [False, 'Error']


# main work function
def main():
    try:
        # get user values
        a1 = float(input('Enter a1: '))
        a2 = float(input('Enter a2: '))
        b1 = float(input('Enter b1: '))
        b2 = float(input('Enter b2: '))
        
        z1 = f'{a1} + {b1}i'
        z2 = f'{a2} + {b2}i'
        print(f'z1 = {z1}')
        print(f'z2 = {z2}')
        
        user_choice = choose() # user makes choice
        if user_choice[0] == False:
            # failed choice
            return 'Enter correct option'
        
        match user_choice[1]:
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
            
            case 5:
                # each operation
                complex_sum(a1, a2, b1, b2)
                complex_sub(a1, a2, b1, b2)
                complex_mult(a1, a2, b1, b2)
                complex_div(a1, a2, b1, b2)
                return
            
    except ValueError:
        # wrong input values
        print('Error: enter correct numbers.')
        return
    
    
if __name__ == "__main__":
    main()