from flask import Blueprint, request, flash, redirect, url_for, render_template, session
from Blue.sql import execute,update
bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        if not user_name or not password:
            flash('无效输入')
            return redirect(url_for('login.login'))

        user = execute('select * from users where username=%s and PASSWORD=%s',[user_name,password])
        if user:
            session['user_info'] = {'username':user[0],'password':user[1]}
            return redirect(url_for('index.index'))

        flash('用户名或密码有误')
        return redirect(url_for('login.login'))

    return render_template('login.html')

#修改用户密码
@bp.route('/change/password',methods=['POST','GET'])
def pwd():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        new_password = request.form.get('new_password')
        if not user_name or not new_password:
            flash('无效输入')
            return redirect(url_for('login.pwd'))

        answer = update('update users set PASSWORD = %s where username = %s;', [new_password, user_name])
        if answer:
            flash('修改成功，重新登陆')
            return redirect(url_for('login.login'))

    return render_template('pwd_change.html')


