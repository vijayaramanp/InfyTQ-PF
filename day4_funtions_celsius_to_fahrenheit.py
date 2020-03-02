#goal of this tryout is to create a function from scratch and invoke it for the given problem
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*(5/9)
    return celsius
c=1.0
f=celsius_to_fahrenheit(c)
print("%.2f Celsius is %0.2f Fahrenheit " %(c,f))

f=1.0
c=fahrenheit_to_celsius(f)
print('%.2f Fahrenheit is %0.2f Celsius ' %(f,c))


#Courtesy: https://beginnersbook.com/2019/05/python-program-to-convert-celsius-to-fahrenheit-and-vice-versa/
