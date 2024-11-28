const letters = document.querySelectorAll('.letter');

letters.forEach(letter => {
    letter.addEventListener('click', () => {
        const entries = letter.nextElementSibling; // Get the next <ul> (entries)
        entries.style.display = (entries.style.display === 'block') ? 'none' : 'block';
    });
});
