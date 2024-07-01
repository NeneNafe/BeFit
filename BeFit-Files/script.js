const mainVideo = document.getElementById('main-vid');
const pipVideo = document.getElementById('pip-video');

// Check if videos are loaded
mainVideo.addEventListener('loadeddata', () => {
    console.log('Main video loaded successfully');
});

pipVideo.addEventListener('loadeddata', () => {
    console.log('PiP video loaded successfully');
});

// Error handling for video loading
mainVideo.addEventListener('error', (e) => {
    console.error('Error loading main video:', e);
});

pipVideo.addEventListener('error', (e) => {
    console.error('Error loading PiP video:', e);
});

// Synchronize the interpreter video with the main video
mainVideo.addEventListener('play', () => {
    console.log('Main video played');
    pipVideo.currentTime = mainVideo.currentTime;
    pipVideo.play();
});

mainVideo.addEventListener('pause', () => {
    console.log('Main video paused');
    pipVideo.pause();
});

mainVideo.addEventListener('seeked', () => {
    console.log('Main video seeked');
    pipVideo.currentTime = mainVideo.currentTime;
});

pipVideo.addEventListener('timeupdate', () => {
    console.log('PiP video time update:', pipVideo.currentTime);
});

// Handle PiP functionality
document.addEventListener('dblclick', async (event) => {
    if (event.target === pipVideo && document.pictureInPictureEnabled && !pipVideo.disablePictureInPicture) {
        try {
            if (pipVideo !== document.pictureInPictureElement) {
                await pipVideo.requestPictureInPicture();
                console.log('Entered Picture-in-Picture mode');
            } else {
                await document.exitPictureInPicture();
                console.log('Exited Picture-in-Picture mode');
            }
        } catch (error) {
            console.error('Error with PiP mode:', error);
        }
    }
});