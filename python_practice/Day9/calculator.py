from flask import Flask

calculator=Flask(__name__)

@calculator.route("/")
def home():
    return "This is calculator"

@calculator.route('/add/<int:num1>/<int:num2>')

def add(num1,num2):
    return f"Sum is {num1 + num2}"

@calculator.route('/sub/<int:num1>/<int:num2>')

def sub(num1,num2):
    return f"Subtraction is {num1 - num2}"

@calculator.route('/mul/<int:num1>/<int:num2>')

def mul(num1,num2):
    return f"Multiplication is {num1 * num2}"

@calculator.route('/div/<int:num1>/<int:num2>')

def div(num1,num2):
    if num2==0:
        return "The denominator cant be 0"
    return f"Division is {num1 / num2}"

if __name__== '__main__':
    calculator.run(debug=True)

