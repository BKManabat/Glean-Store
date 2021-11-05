from flask import Flask, request, jsonify, redirect, render_template, session, url_for
from API.api_users import register_route

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gleandb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'OurSecretKey'

# db.session.query(UserModel).delete()
# db.session.commit()

register_route(app)

@app.route('/')
def index():
  print("session_main:",session)
  if 'username' in session:
    print("if")
    return redirect(url_for('home'))
  else:
    print('else')
    return render_template("index.html")

@app.route('/home')
def home():
  print("session_home:",session)
  if 'username' not in session:
    return redirect(url_for('index'))
  else:
    return render_template("home.html", username = session['username'])

@app.route('/logout')
def logout():
  session.pop('username',None)
  return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(host="0.0.0.0")