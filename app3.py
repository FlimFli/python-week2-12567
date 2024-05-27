num_string = '12'
num_integer = 23

print('Data type Casting:',type(num_string))
#explicit type conversion
num_string = float(num_string)
print(f'Data type Casting: {num_string}',type(num_string))

num_sum = num_string + num_integer
print(f'Sum: {num_sum}',type(num_sum))
