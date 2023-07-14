from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/", methods=["GET"])
def init():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))
    else:
        return redirect(url_for("auth_bp.login"))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', salutacio_inicial = "Ei, tot bé?")

@main_bp.route("/hola", methods=["POST"])
@login_required
def hola():
    return "Hola des del servidor!"

@main_bp.route("/bondia", methods=["POST"])
@login_required
def bondia():
    return "Bon dia des del servidor!"

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))