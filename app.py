from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RespostaForm, MensagemForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "segredo_nao_me_contes"

respostas = (
    "avestruz",
    "sete",
    "seis",
    "lua",
    "h2o",
)

# mensagens = []


@app.route("/", methods=["GET", "POST"])
def home():
    form = RespostaForm()
    return render_template("home.html", form=form)


@app.route("/pergunta1", methods=["GET", "POST"])
def pergunta1():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[0]:
            return redirect(url_for("pergunta2"))
        else:
            flash("Resposta incorreta. Tenta novamente.", "error")
    return render_template("pergunta1.html", form=form)


@app.route("/pergunta2", methods=["GET", "POST"])
def pergunta2():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[1]:
            return redirect(url_for("pergunta3"))
        else:
            flash("Resposta incorreta. Tenta novamente.", "error")
    return render_template("pergunta2.html", form=form)


@app.route("/pergunta3", methods=["GET", "POST"])
def pergunta3():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[2]:
            return redirect(url_for("pergunta4"))
        else:
            flash("Resposta incorreta. Tenta novamente.", "error")
    return render_template("pergunta3.html", form=form)


@app.route("/pergunta4", methods=["GET", "POST"])
def pergunta4():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[3]:
            return redirect(url_for("pergunta5"))
        else:
            flash("Resposta incorreta. Tenta novamente.", "error")
    return render_template("pergunta4.html", form=form)


@app.route("/pergunta5", methods=["GET", "POST"])
def pergunta5():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[4]:
            return redirect(url_for("vitoria"))
        else:
            flash("Resposta incorreta. Tenta novamente.", "error")
    return render_template("pergunta5.html", form=form)


@app.route("/vitoria", methods=["GET", "POST"])
def vitoria():
    form = MensagemForm()
    # if form.validate_on_submit():
    #     mensagem = form.mensagem.data
    #     mensagens.append(mensagem)
    #     print(f"Mensagem recebida: {mensagem}")
    #     flash(
    #         f"Mensagem enviada com sucesso! Já existem {len(mensagens)} mensagem(s).",
    #         "success",
    #     )
    return render_template("vitoria.html", form=form)


@app.route("/desistir", methods=["GET", "POST"])
def desistir():
    form = RespostaForm()
    return render_template("desistir.html", form=form)


# @app.route("/mensagens")
# def ver_mensagens():
#     return render_template("mensagens.html", mensagens=mensagens)


if __name__ == "__main__":
    app.run()
