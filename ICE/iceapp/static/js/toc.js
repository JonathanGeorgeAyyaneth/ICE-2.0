function htmlTableOfContents(documentRef, container) {
    var documentRef = documentRef || document;
    var headings = [].slice.call(documentRef.body.querySelectorAll('article h1, article h2, article h3, article h4, article h5, article h6'));
    var parentH2 = null;

    var toc = document.createElement('div');
    toc.id = 'toc';

    headings.forEach(function(heading, index) {
        var anchor = documentRef.createElement('a');
        anchor.setAttribute('name', 'toc' + index);
        anchor.setAttribute('id', 'toc' + index);

        var link = documentRef.createElement('a');
        link.setAttribute('href', '#toc' + index);
        link.textContent = heading.textContent;

        var div = documentRef.createElement('div');
        var tagName = heading.tagName.toLowerCase();
        div.setAttribute('class', tagName);

        if (tagName === 'h2') {
            parentH2 = heading;
        }

        if (tagName === 'h3' && parentH2) {
            div.style.marginLeft = '20px';
        }

        if (tagName === 'h1') {
            div.style.fontWeight = 'bold';
        }

        div.appendChild(link);
        toc.appendChild(div);
        heading.parentNode.insertBefore(anchor, heading);
    });

    container.appendChild(toc);
}

function informtoc() {
    var popupDiv = document.createElement('div');
    popupDiv.classList.add('popup');

    // styling the div
    popupDiv.style.position = 'fixed';
    popupDiv.style.top = '50%';
    popupDiv.style.left = '50%';
    popupDiv.style.transform = 'translate(-50%, -50%)';
    popupDiv.style.zIndex = '1000';
    
    var closeButton = document.createElement('button');
    closeButton.textContent = '×'; // Using '×' character for a close icon
    closeButton.style.position = 'absolute';
    closeButton.style.top = '10px';
    closeButton.style.right = '10px';
    closeButton.style.backgroundColor = 'transparent'; // Transparent background
    closeButton.style.border = 'none'; // No border
    closeButton.style.fontSize = '20px'; // Font size
    closeButton.style.cursor = 'pointer'; // Pointer cursor for better UX
    closeButton.onclick = function() {
        document.body.removeChild(popupDiv);
    };
    popupDiv.appendChild(closeButton);

    // adding text
    var textNode = document.createElement('h2');
    textNode.textContent = "Table of Contents";
    textNode.onclick = function() {
        document.body.removeChild(popupDiv);
    };
    popupDiv.appendChild(textNode);
    

    // create container for table of contents
    var tocContainer = document.createElement('div');
    popupDiv.appendChild(tocContainer);
    

    // call the table of contents function
    htmlTableOfContents(document, tocContainer);

    // appending it
    document.body.appendChild(popupDiv);
}

function updateTimes() {
    const elements = document.querySelectorAll('.comment-time');
    elements.forEach(element => {
        const timestamp = new Date(element.getAttribute('data-time'));
        const now = new Date();
        const seconds = Math.floor((now - timestamp) / 1000);
        
        let interval = Math.floor(seconds / 31536000);
        if (interval > 1) {
            element.innerText =interval + " years ago";
            return;
        }
        interval = Math.floor(seconds / 2592000);
        if (interval > 1) {
            element.innerText =interval + " months ago";
            return;
        }
        interval = Math.floor(seconds / 86400);
        if (interval > 1) {
            element.innerText =interval + " days ago";
            return;
        }
        interval = Math.floor(seconds / 3600);
        if (interval > 1) {
            element.innerText =interval + " hours ago";
            return;
        }
        interval = Math.floor(seconds / 60);
        if (interval > 1) {
            element.innerText =interval + " minutes ago";
            return;
        }
        element.innerText =Math.floor(seconds) + " seconds ago";
    });
}

// Initial call
document.addEventListener('DOMContentLoaded', function() {
    updateTimes();
});