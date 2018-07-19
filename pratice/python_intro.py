print('Hello, Jiwon! Welcome to Django:)')

if 3>2 : 
    print('True! It works:)')


if 5 > 2 :
    print("5가 2보다 크다")
else : 
    print("5가 2보다 작다")

name = 'ITKOO'

if name == 'ITKOO' : 
    print('Hello ITKOO')
elif name == 'Sonia' : 
    print("Hello Sonia")
else : 
    print("Hello Everyone!")

def hi() : 
    print('Hi Im made by Jiwon')
    print('How are you today')

hi()   



def hi(name) :
    print('Hi '  + name + '!')

girls = ['Jimin', 'Jiwon', 'Tae' , 'Yeo']

for name in girls :
    hi(name)
    print('Next Girl')

for i in range(1,6):
    print(i)