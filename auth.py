from flask import Blueprint, render_template, request, url_for, redirect, flash
from .forms import RegisterForm
from werkzeug.sercurity import generate_password_hash, check_password_hash
from .import db
from models import User

    @bp.route('/register,methods=['GET', 'POST'])
    def register():
        register= RegisterForm()
        if (register.validate_ib_submit()== True):
            # get user, password and email from form
            uname= register.user_name.data
            pwd = register.password.data
            email = register.email_id.data


            u1 = User.query.filter_by(name=uname).first()
            if u1:
                flash ('User name already exists, please login')
                return redirect (url_for)('auth.login'))
            pwd_hash = generate_password_hash(pwd)
            new_user = User (name= uname, password_hash= pwd_hash, emailid=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('main/index'))

        else:
            return render_template('user.html', form=register, heading='Register')

        @bp.route('/logout')   
        @login_required
        def logout():
            logout_user()
            return 'You have been logged out' 