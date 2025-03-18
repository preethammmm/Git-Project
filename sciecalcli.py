from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate(operation, a, b=None):
    try:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b if b != 0 else "Error: Division by zero"
        elif operation == 'power':
            return math.pow(a, b)
        elif operation == 'sqrt':
            return math.sqrt(a)
        elif operation == 'sin':
            return math.sin(math.radians(a))
        elif operation == 'cos':
            return math.cos(math.radians(a))
        elif operation == 'tan':
            return math.tan(math.radians(a))
        elif operation == 'log':
            return math.log(a)
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    a_value = ""
    b_value = ""
    
    if request.method == 'POST':
        op = request.form.get('operation')
        # Get first operand; required for all operations.
        a_str = request.form.get('a')
        try:
            a_value = float(a_str)
        except (TypeError, ValueError):
            return render_template('index.html', result="Error: Please enter a valid number for A", a=a_str, b=request.form.get('b'))
        
        # For binary operations, try to get second operand.
        if op in ['+', '-', '*', '/', 'power']:
            b_str = request.form.get('b')
            b_value = b_str
            try:
                b = float(b_str)
            except (TypeError, ValueError):
                return render_template('index.html', result="Error: Please enter a valid number for B", a=a_str, b=b_str)
            result = calculate(op, a_value, b)
        else:
            # Unary operations: sqrt, sin, cos, tan, log.
            result = calculate(op, a_value)
    
    return render_template('index02.html', result=result, a=a_value, b=b_value)

if __name__ == '__main__':
    app.run(debug=True)
