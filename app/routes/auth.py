"""
auth.py — User registration, login, and logout routes
Author: Siddhi Singh (Full-Stack Lead)
"""
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.database import get_db
from app import bcrypt

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('predict.upload'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            flash('Please fill in all fields.', 'danger')
            return render_template('auth/login.html')

        db   = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user and bcrypt.check_password_hash(user['password'], password):
            session.clear()
            session['user_id']  = user['id']
            session['username'] = user['username']
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('predict.upload'))

        flash('Invalid username or password.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        return redirect(url_for('predict.upload'))

    if request.method == 'POST':
        username         = request.form.get('username', '').strip()
        password         = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Validation
        if not username or not password:
            flash('All fields are required.', 'danger')
            return render_template('auth/register.html')

        if len(username) < 3:
            flash('Username must be at least 3 characters.', 'danger')
            return render_template('auth/register.html')

        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return render_template('auth/register.html')

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('auth/register.html')

        db = get_db()
        existing = db.execute(
            'SELECT id FROM users WHERE username = ?', (username,)
        ).fetchone()

        if existing:
            flash('Username already taken. Please choose another.', 'danger')
            return render_template('auth/register.html')

        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        db.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, pw_hash)
        )
        db.commit()

        flash('Account created! Please sign in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/logout')
def logout():
    username = session.get('username', 'User')
    session.clear()
    flash(f'Goodbye, {username}!', 'success')
    return redirect(url_for('auth.login'))
