from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']
        result = 0

        if operator == 'add':
            result = num1 + num2
        elif operator == 'sub':
            result = num1 - num2
        elif operator == 'mul':
            result = num1 * num2
        elif operator == 'div':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Cannot divide by zero."

        return render_template('index.html', result=result, num1=num1, num2=num2, operator=operator)

    except ValueError:
        return "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)