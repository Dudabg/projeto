from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import LoginManager
from flask import flash



app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://duda:63524178@127.0.0.1:3306/user'

app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(512))


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)


    def verify_password(self, password):
            return check_password_hash(self.password, password)


    def get_id(self):
        return str(self.iduser)  
        # Convertendo o ID para string



@app.route('/login', methods=['GET', 'POST'])
@login_required
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('produto'))  # Redireciona para a página de produtos após o login
        else:
            flash('Credenciais inválidas. Por favor, verifique seu email e senha e tente novamente.', 'error')
            
            return render_template('login.html', current_user=current_user)  # Redireciona de volta para a página de login em caso de falha no login
    return render_template('produto.html', current_user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html', current_user=current_user)





class Produto(db.Model):
    idproduto = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80))
    descricao = db.Column(db.Text)
    preco= db.Column(db.Integer)

    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco



@app.route("/produto", methods=["GET", "POST"])
@login_required
def produto():
    produtos = Produto.query.all() 
    return render_template("produto.html", produtos=produtos)




@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(password):
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('produto'))  # Redirecionar para a página de produtos após o login
    return render_template('login.html', current_user=current_user)






@app.route("/criar", methods=["POST", "GET"])
def criar():
    if request.method == "POST":
        
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = request.form["preco"]

        # Verifica se os campos estão vazios
        if not nome or not descricao or not preco:
            mensagem = "Por favor, preencha todos os campos antes de enviar."
            return render_template("criar.html", mensagem=mensagem)

        produto = Produto(nome, descricao, preco)
        db.session.add(produto)  
        db.session.commit()  
     
        return redirect(url_for('produto'))  
    return render_template("criar.html")




@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    produto = Produto.query.get(id)
    
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']

        if not nome or not descricao or not preco:
            mensagem = "Por favor, preencha todos os campos antes de enviar."
            return render_template('/editar.html', produto=produto, produto_id=id, mensagem=mensagem)

        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco    
        db.session.add(produto)
        db.session.commit()
        url=url_for
        return redirect(url_for('produto'))  # redirecionar para a rota 'produto' após a atualização
    return render_template('/editar.html', produto=produto, produto_id=id)




@app.route('/deletar_produto/<int:idproduto>')
def deletar(idproduto):
    produto = Produto.query.get(idproduto)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('produto'))






#colocar site no ar
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)



