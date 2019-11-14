import re
from flask import Flask, session, escape, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'you dawn {0}'.format(escape(session['username']))
    return 'noooo'
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {0}'.format(post_id)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return 'html FORM'

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
app.secret_key='dsfdsfsdfsdf'

if __name__ =="__main__":
    app.run(debug=True)
