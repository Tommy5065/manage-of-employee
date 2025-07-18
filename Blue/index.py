from flask import Blueprint, render_template, redirect, url_for, request, flash
from Blue.sql import select, insert_emp, delete_emp, update
bp = Blueprint('index',__name__,url_prefix='/index')


@bp.route('',methods=['POST','GET'])
def index():
    employee = select()
    return render_template('index.html', employee=employee)

@bp.route('/add',methods=['POST','GET'])
def add():
    if request.method == 'POST':
        id_number = request.form.get('id_number')
        user_name = request.form.get('name')
        user_age = request.form.get('age')
        user_sex = request.form.get('sex')
        user_job = request.form.get('job')

        insert_emp('insert into employee(id_number, name, age, sex, job) values(%s, %s, %s, %s, %s);', [ id_number,user_name, user_age, user_sex, user_job ])
        flash('添加成功')
        return redirect(url_for('index.index'))

    return render_template('index.html')

@bp.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        id = request.form.get('id')
        print(id)
        delete_emp('delete from employee where id = %s;', id)
        return redirect(url_for('index.index'))

    return render_template('index.html')


@bp.route('/edit', methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        id = request.form.get('ID')
        age = request.form.get('age')
        job = request.form.get('job')
        if not id or not age or not job:
            flash('无效修改')
            return redirect(url_for('index.edit'))

        answer=update('update employee set age=%s , job=%s where id=%s;',[age, job, id])
        if answer:
            flash('修改成功')
            return redirect(url_for('index.index'))

        return redirect(url_for('index.edit'))

    return render_template('edit.html')


