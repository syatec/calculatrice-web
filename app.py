from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculatrice():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            operation = request.form['operation']

            if operation == 'add':
                num2 = float(request.form['num2'])
                result = num1 + num2
            elif operation == 'subtract':
                num2 = float(request.form['num2'])
                result = num1 - num2
            elif operation == 'multiply':
                num2 = float(request.form['num2'])
                result = num1 * num2
            elif operation == 'divide':
                num2 = float(request.form['num2'])
                result = num1 / num2 if num2 != 0 else "Erreur: Division par zéro"
            elif operation == 'square':
                result = num1 ** 2  # Carré
            elif operation == 'sqrt':
                result = math.sqrt(num1) if num1 >= 0 else "Erreur: Nombre négatif"  # Racine carrée
        except ValueError:
            result = "Erreur: Entrée invalide"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
