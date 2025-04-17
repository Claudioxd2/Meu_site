from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    lista_projetos = [
        {'titulo': 'Projeto 1', 'descricao': 'Uma breve descrição do Projeto 1.'},
        {'titulo': 'Projeto 2', 'descricao': 'Detalhes interessantes sobre o Projeto 2.'},
        {'titulo': 'Projeto 3', 'descricao': 'Este é um exemplo do Projeto 3.'}
    ]
    return render_template('projetos.html', projetos=lista_projetos)

if __name__ == '__main__':
    app.run(debug=True)