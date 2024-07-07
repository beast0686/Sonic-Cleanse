from flask import Flask, render_template, request, send_from_directory
import os
import librosa
import scipy.signal
import soundfile as sf

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


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

        # Process the uploaded audio file
        processed_file = process_audio(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template('index.html', original_audio=filename, processed_audio=processed_file)


def process_audio(filepath):
    # Load the audio file
    y, sr = librosa.load(filepath, sr=16000, mono=True, duration=10)

    # Apply the high-pass filter
    yf = f_high(y, sr)

    # Save the filtered audio
    output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'filtered_audio.mp3')
    sf.write(output_file, yf, sr)

    return 'filtered_audio.mp3'  # Return the filename or path of the processed file


def f_high(y, sr):
    b, a = scipy.signal.butter(10, 2000 / (sr / 2), btype='highpass')
    yf = scipy.signal.lfilter(b, a, y)
    return yf


if __name__ == '__main__':
    app.run(debug=True)
