from flask import Flask, jsonify, render_template
valor = 0

#Criar uma instancia do aplicativo
app = Flask(__name__)

#Definir rotas e funcoes
@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api/valor')
def get_valor():
    # Realize algum processamento ou lógica para obter o novo valor
    global valor
    valor += 1
    return jsonify({'valor': str(valor)})  # Converter o valor para string

#Executar o aplicativo
if __name__ == '__main__':
    app.run()