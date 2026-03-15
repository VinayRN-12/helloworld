<!DOCTYPE html>
<html>
<head>
    <title>Webcam Image Capture</title>
</head>
<body>
    <h2>Webcam Image Capture</h2>
    <video id="video" width="640" height="480" autoplay></video>
    <button id="captureButton">Capture</button>
    <canvas id="canvas" width="640" height="480" style="display: none;"></canvas>
    <script>
        // Get access to webcam
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                var video = document.getElementById('video');
                video.srcObject = stream;
            })
            .catch(function(err) {
                console.error('Error accessing webcam: ', err);
            });

        // Capture image from webcam
        document.getElementById('captureButton').addEventListener('click', function() {
            var video = document.getElementById('video');
            var canvas = document.getElementById('canvas');
            var context = canvas.getContext('2d');
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            var imageData = canvas.toDataURL('image/jpeg');

            // Send captured image to servlet
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'ImageServlet', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    console.log('Image sent successfully');
                }
            };
            xhr.send('image=' + encodeURIComponent(imageData));
        });
    </script>
</body>
</html>
