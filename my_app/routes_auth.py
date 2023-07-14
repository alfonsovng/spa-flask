from flask import Blueprint, redirect, flash, request, render_template, url_for
from flask_login import current_user, login_user

from . import login_manager, logger
from .forms import LoginForm
from .models import User

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.init"))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        lowercase_email = form.email.data.lower()

        existing_user = User.find_user(email = lowercase_email)
        if existing_user and existing_user.check_password(password=form.password.data):
            
            logger.info(f"Login: {lowercase_email}")

            login_user(existing_user)
            
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main_bp.init"))

        flash(message = "Invalid email or password")
        return redirect(url_for("auth_bp.login"))

    return render_template('login.html', form = form)

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.find_user(email = user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    flash(message = "Please login to see this page")
    # TODO: set next
    return redirect(url_for("auth_bp.login"))
