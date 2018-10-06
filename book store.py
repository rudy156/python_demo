bn=input('enter book name:')
bc=int(input('enter book code:'))
bp=int(input('enter book price:'))
if (bn=='python_programing')and (bp>800):
    d_price= 20/100*bp
    print('the total price of the book is:', float(bp)-float(d_price))
elif(bn=='linux_shell_scripting')and (500>bp<800):
    d_price=15/100*bp
    print('the total price of the book is:',float(bp)-float(d_price))
elif (bp<500):
    d_price=10/100*bp
    print('the total price of the book is:',float(bp)-float(d_price))
else:
    d_price=5/100*bp
    print('the total price of the book is:',float(bp)-float(d_price))
