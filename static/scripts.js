document.getElementById('processButton').addEventListener('click', function() {
    const audioUpload = document.getElementById('audioUpload');
    const audioPlayer = document.getElementById('audioPlayer');
    const audioSource = document.getElementById('audioSource');

    if (audioUpload.files.length === 0) {
        alert('Please upload an audio file first.');
        return;
    }

    const file = audioUpload.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        audioSource.src = e.target.result;
        audioPlayer.load();
        // Here you can add your backend processing logic
        alert('Audio file uploaded. Implement backend processing here.');

        // Smooth transition from noise to calm
        document.querySelector('.noise-animation').classList.add('hidden');
        document.querySelector('.calm-animation').classList.remove('hidden');
    };

    reader.readAsDataURL(file);
});

// Adding custom file input behavior
const customFileInput = document.getElementById('audioUpload');
const customFileLabel = document.createElement('label');
customFileLabel.innerText = 'Browse';
customFileLabel.setAttribute('for', 'audioUpload');
customFileLabel.classList.add('custom-file-label');
customFileInput.insertAdjacentElement('beforebegin', customFileLabel);

document.getElementById('audioUpload').addEventListener('change', function() {
    // Show noisy animation when file is added
    document.querySelector('.noise-animation').classList.remove('hidden');
    document.querySelector('.calm-animation').classList.add('hidden');
});

// Initially hide animations
document.querySelector('.noise-animation').classList.add('hidden');
document.querySelector('.calm-animation').classList.add('hidden');

// Logout button functionality
document.getElementById('logoutButton').addEventListener('click', function() {
    // Implement your logout functionality here
    alert('You have been logged out.');
    // For demonstration, redirect to login page (assuming 'login.html' exists)
    window.location.href = 'login.html';
});

// Add event listeners for drag and drop functionality
const dropArea = document.getElementById('dropArea');
const uploadInput = document.getElementById('audioUpload');

// Prevent default behaviors for drag events
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area on drag over
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

// Remove highlighting on drag leave
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight() {
    dropArea.classList.add('highlight');
}

function unhighlight() {
    dropArea.classList.remove('highlight');
}

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;

    handleFiles(files);
}

// Update file input on drop
function handleFiles(files) {
    uploadInput.files = files;
    handleFileSelect();
}

// Update input label on file select
uploadInput.addEventListener('change', handleFileSelect);

function handleFileSelect() {
    const files = uploadInput.files;
    if (files.length > 0) {
        const fileName = files[0].name;
        const dropText = document.querySelector('.drop-text');
        dropText.textContent = `File selected: ${fileName}`;
    } else {
        const dropText = document.querySelector('.drop-text');
        dropText.textContent = 'Drag and drop audio files here';
    }
}

// Process button functionality (your existing code)
document.getElementById('processButton').addEventListener('click', function() {
    const audioUpload = document.getElementById('audioUpload');
    const audioPlayer = document.getElementById('audioPlayer');
    const audioSource = document.getElementById('audioSource');

    if (audioUpload.files.length === 0) {
        alert('Please upload an audio file first.');
        return;
    }

    const file = audioUpload.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        audioSource.src = e.target.result;
        audioPlayer.load();
        // Here you can add your backend processing logic
        alert('Audio file uploaded. Implement backend processing here.');

        // Smooth transition from noise to calm
        document.querySelector('.noise-animation').classList.add('hidden');
        document.querySelector('.calm-animation').classList.remove('hidden');
    };

    reader.readAsDataURL(file);
});

// Initially hide animations
document.querySelector('.noise-animation').classList.add('hidden');
document.querySelector('.calm-animation').classList.add('hidden');

// Logout button functionality
document.getElementById('logoutButton').addEventListener('click', function() {
    // Implement your logout functionality here
    alert('You have been logged out.');
    // For demonstration, redirect to login page (assuming 'login.html' exists)
    window.location.href = 'login.html';
});

// JavaScript for additional animations or interactions

// Animation for drop area when files are dragged over
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, function() {
        dropArea.classList.add('highlight');
    }, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, function() {
        dropArea.classList.remove('highlight');
    }, false);
});

// Update file input label on file select
uploadInput.addEventListener('change', handleFileSelect);

function handleFileSelect() {
    const files = uploadInput.files;
    if (files.length > 0) {
        const fileName = files[0].name;
        const dropText = document.querySelector('.drop-text');
        dropText.textContent = `File selected: ${fileName}`;
        dropText.style.color = '#1565C0'; // Change text color on file selection
    } else {
        const dropText = document.querySelector('.drop-text');
        dropText.textContent = 'Drag and drop audio files here';
        dropText.style.color = '#ffffff'; // Reset text color if no file selected
    }
}

