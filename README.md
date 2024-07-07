# SonicCleanse: Advanced Noise Suppression System

SonicCleanse is a web application designed for advanced audio processing to reduce noise in audio files. It allows users to upload audio files, apply noise reduction processing, and download the processed audio files.

## Features

- **Upload Audio Files**: Users can drag and drop audio files to upload for processing.
- **Noise Reduction**: Implements a high-pass filter to reduce noise in uploaded audio files.
- **Audio Playback**: Provides playback controls for both the original and processed audio files.
- **Download**: Users can download the processed audio file after processing.

## Technologies Used

- **Flask**: Backend web framework for handling requests and serving pages.
- **Librosa**: Python package for audio and music analysis.
- **Scipy**: Library for scientific and technical computing, used for signal processing.
- **Soundfile**: Library for reading and writing sound files.
- **HTML/CSS/JavaScript**: Frontend technologies for user interface and interactivity.

## Setup Instructions

1. **Clone the Repository**

   ```
   git clone https://github.com/your-username/sonic-cleanse.git
   cd sonic-cleanse
   ```

2. **Install Dependencies**

   ```
   pip install flask librosa scipy soundfile
   ```

3. **Run the Application**

   ```
   python app.py
   ```

   Navigate to `http://localhost:5000` in your web browser to access SonicCleanse.

## Usage

- **Upload Audio**: Drag and drop an audio file onto the designated area or use the file input button.
- **Process Audio**: Click "Process Audio" to apply noise reduction.
- **Playback**: Listen to both the original and processed audio files using the audio players provided.
- **Download**: Download the processed audio file using the provided link.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---
