from flask import Blueprint,request, flash, redirect, render_template, url_for
from Blue.sql import insert
bp: Blueprint = Blueprint('register', __name__, url_prefix='/register')

@bp.route('', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        if not user_name or not password:
            flash('无效输入')
            return redirect(url_for('register.register'))

        answer = insert('insert into users(username,PASSWORD) values(%s,%s);', [user_name, password])
        if answer:
            flash('用户名已存在')
            return redirect(url_for('register.register'))

        flash('注册成功，请重新登录')
        return redirect(url_for('login.login'))


    return render_template('register.html')
