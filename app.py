from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'secreto123'  # Necesario para usar sesiones

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'numero' not in session:
        session['numero'] = random.randint(1, 100)
        session['intentos'] = 0

    mensaje = ''

    if request.method == 'POST':
        try:
            numero_usuario = int(request.form['numero'])
            session['intentos'] += 1
            numero_secreto = session['numero']

            if numero_usuario < numero_secreto:
                mensaje = 'Demasiado bajo'
            elif numero_usuario > numero_secreto:
                mensaje = 'Demasiado alto'
            else:
                mensaje = f'¡Correcto! Lo adivinaste en {session["intentos"]} intentos.'
                session.pop('numero')
                session.pop('intentos')
        except ValueError:
            mensaje = 'Por favor, ingresa un número válido.'

    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
