from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Create a dictionary of allowed names from math and additional functions
allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
allowed_names['abs'] = abs
allowed_names['fact'] = math.factorial  # alias for factorial

def safe_eval(expr):
    try:
        # Evaluate the expression safely using the allowed names.
        result = eval(expr, {"__builtins__": None}, allowed_names)
        return result
    except Exception as e:
        return f"Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    expression = ""
    if request.method == 'POST':
        expression = request.form.get('expression', "")
        result = safe_eval(expression)
    return render_template('index03.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
