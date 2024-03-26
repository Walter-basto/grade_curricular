from flask import Flask, render_template, request,redirect

app=Flask(__name__)
@app.route('/formulario', methods=['GET','POST'])
def formulario():
    if request.method == 'POST':
        req = request.form

        nome = req['nome']
        email = req.get('email')
        senha = request.form['senha']

        print(nome,email,senha)

        return redirect(request.url)

    return render_template('formulario.html')

if __name__=="__main__":
    app.run()
