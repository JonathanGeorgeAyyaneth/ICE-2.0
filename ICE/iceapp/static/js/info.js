function inform(imageSrc) {
    var popupDiv = document.createElement('div');
    popupDiv.classList.add('popup');

    // Styling the div
    popupDiv.style.position = 'fixed';
    popupDiv.style.top = '50%';
    popupDiv.style.left = '50%';
    popupDiv.style.transform = 'translate(-50%, -50%)';
    popupDiv.style.zIndex = '1000';
    popupDiv.style.backgroundColor = 'white';
    popupDiv.style.padding = '20px';
    popupDiv.style.borderRadius = '10px';
    popupDiv.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    popupDiv.style.maxWidth = '90vw';  // Ensure popup fits in viewport width
    popupDiv.style.maxHeight = '90vh';  // Ensure popup fits in viewport height
    popupDiv.style.overflow = 'hidden'; // Hide overflow

    // Adding the image
    var image = document.createElement('img');
    image.src = imageSrc;
    image.style.maxWidth = '100%';
    image.style.maxHeight = '80vh';
    popupDiv.appendChild(image);
    
    // Close button
    var closeButton = document.createElement('button');
    closeButton.textContent = 'Close';
    closeButton.style.display = 'block';
    closeButton.style.marginTop = '15px';
    closeButton.style.padding = '10px';
    closeButton.style.backgroundColor = '#ff8a00';
    closeButton.style.color = 'white';
    closeButton.style.border = 'none';
    closeButton.style.cursor = 'pointer';
    closeButton.style.borderRadius = '5px';
    closeButton.onclick = function() {
        document.body.removeChild(popupDiv);
    };
    popupDiv.appendChild(closeButton);

    // Appending the popup to the body
    document.body.appendChild(popupDiv);
}
