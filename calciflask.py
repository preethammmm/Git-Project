from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def power(a, b):
    return math.pow(a, b)

def sqrt(a):
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    if request.method == 'POST':
        op = request.form.get('operation')
        try:
            if op in ['+', '-', '*', '/', 'power']:
                a = float(request.form.get('a'))
                b = float(request.form.get('b'))
                if op == '+':
                    result = add(a, b)
                elif op == '-':
                    result = subtract(a, b)
                elif op == '*':
                    result = multiply(a, b)
                elif op == '/':
                    result = divide(a, b)
                elif op == 'power':
                    result = power(a, b)
            elif op in ['sqrt', 'sin', 'cos', 'tan']:
                a = float(request.form.get('a'))
                if op == 'sqrt':
                    result = sqrt(a)
                elif op == 'sin':
                    result = sin(a)
                elif op == 'cos':
                    result = cos(a)
                elif op == 'tan':
                    result = tan(a)
        except Exception as e:
            result = f"Error: {e}"

    return render_template_string('''
        <h1>Scientific Calculator</h1>
        <form method="post">
            Number A: <input type="text" name="a"><br>
            Number B (if required): <input type="text" name="b"><br>
            Operation: 
            <select name="operation">
                <option value="+">Addition</option>
                <option value="-">Subtraction</option>
                <option value="*">Multiplication</option>
                <option value="/">Division</option>
                <option value="power">Power</option>
                <option value="sqrt">Square Root</option>
                <option value="sin">Sine</option>
                <option value="cos">Cosine</option>
                <option value="tan">Tangent</option>
            </select><br>
            <input type="submit" value="Calculate">
        </form>
        <h2>Result: {{ result }}</h2>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
