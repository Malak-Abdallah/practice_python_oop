
# throw an error when a certain condition occurs using raise
'''
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
'''


#assertion error:
'''
name='ahmad'
assert (name=='malak'), f'name is {name} and it should be malak'  #if the assertion happened this sentence will be printed
# if we pass the assertion(assertion=True), the code will continue
print(f'your name is {name}')

'''

#try...except:
# x=1
#x=0
x='malk'
try:
    answer=1/x
except ZeroDivisionError:
    answer='undefined'
except TypeError:
    answer='meaningless'
else: #when no error occurs
    print(f'the answer is {answer}')
finally: #this block will always run
    print(f'the answer is {answer}')
    print('done')




