# Importing necessary libraries
import librosa.display  # For displaying audio features
import numpy as np  # For numerical operations
from IPython.display import Audio, display  # For displaying audio in Jupyter notebooks
import scipy.signal  # For signal processing
import matplotlib.pyplot as plt  # For plotting
import warnings  # For managing warnings
from pylab import rcParams  # For setting figure size
import soundfile as sf  # For reading and writing sound files
import os  # For file and directory operations

# Set the figure size for plots
rcParams['figure.figsize'] = 14, 6

# Ignore warnings
warnings.filterwarnings('ignore')

# Set the sample rate for audio files
sr = 16000

# Define the file path for the audio file
e_file = r"D:\BNMIT\Engineering CSE\Projects\Noise Supression\Test Audio\BLKFR-10-CPL_20190611_093000.pt540.mp3"

# Load 10 seconds of the file
y, sr = librosa.load(e_file, mono=True, sr=sr, offset=0, duration=10)

# Display the original audio
display(Audio(y, rate=sr))

# Plot the waveform of the original audio
plt.figure()
librosa.display.waveshow(y, sr=sr, x_axis='time')
plt.title("Waveform of the Original Audio")
plt.show()


# Define a high-pass filter function
def f_high(y, sr):
    b, a = scipy.signal.butter(10, 2000 / (sr / 2), btype='highpass')  # Design a high-pass Butterworth filter
    yf = scipy.signal.lfilter(b, a, y)  # Apply the filter to the signal
    return yf


# Apply the high-pass filter to the audio
yf = f_high(y, sr)

# Ensure the output directory exists
output_dir = 'Filtered Audio'
os.makedirs(output_dir, exist_ok=True)

# Save the filtered audio to mp3 file in the output directory
output_file = os.path.join(output_dir, 'filtered_audio.mp3')
sf.write(output_file, yf, sr)

# Plot the waveform of the original and filtered audio
plt.figure()
librosa.display.waveshow(y, sr=sr, x_axis='time')
librosa.display.waveshow(yf, sr=sr, x_axis='time', color='r', alpha=0.5)
plt.title("Original and Filtered Waveform")
plt.show()

# Compute and display the Mel spectrogram for the filtered audio
S = librosa.feature.melspectrogram(y=yf, sr=sr, n_mels=64)
D = librosa.power_to_db(S, ref=np.max)

plt.figure()
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title("Mel Spectrogram of Filtered Audio")
plt.show()

# Display the filtered audio
display(Audio(yf, rate=sr))
