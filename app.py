from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
import os
import librosa
import scipy.signal
import soundfile as sf
import secrets
from mysql.connector import errorcode
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
    'database': 'helmet_detection',
}


# Function to connect to the database
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
        else:
            print('Connection failed')
            return None
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None


# Define the folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



# Home route
@app.route('/')
def index():
    # Redirect to login if user is not logged in
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        else:
            return render_template('login_error.html')
    return render_template('login.html')


# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Hash the password using the default method (pbkdf2:sha256)
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('login'))

    return render_template('signup.html')


# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert feedback into the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)',
            (name, email, message)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('contact'))

    return render_template('contact.html')


# About route
@app.route('/about')
def about():
    # Redirect to login if user is not logged in
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('about.html')


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    directory = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory, filename, as_attachment=True)


@app.route('/play/<filename>', methods=['GET'])
def play_audio(filename):
    directory = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory, filename)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio_file' not in request.files:
        return "No file part"

    file = request.files['audio_file']

    if file.filename == '':
        return "No selected file"

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        processed_file = process_audio(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template('index.html', original_audio=filename, processed_audio=processed_file)


def process_audio(filepath):
    y, sr = librosa.load(filepath, sr=16000, mono=True, duration=10)
    yf = f_high(y, sr)
    output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'filtered_audio.mp3')
    sf.write(output_file, yf, sr)
    return 'filtered_audio.mp3'


def f_high(y, sr):
    b, a = scipy.signal.butter(10, 2000 / (sr / 2), btype='highpass')
    yf = scipy.signal.lfilter(b, a, y)
    return yf


if __name__ == '__main__':
    app.run(debug=True)
