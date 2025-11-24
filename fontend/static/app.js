document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('genre-select').addEventListener('change', getRecommendations);
});

async function getRecommendations() {
    const genre = document.getElementById('genre-select').value;
    const listElement = document.getElementById('recommendation-list');
    listElement.innerHTML = 'Loading recommendations...';

    try {
        const response = await fetch(`/api/recommendations?genre=${genre}`);
        const data = await response.json();

        listElement.innerHTML = '';

        if (data.success && data.books.length > 0) {
            data.books.forEach(book => {
                const bookDiv = document.createElement('div');
                bookDiv.className = 'book-item';
                bookDiv.innerHTML = `
                    <h3>${book.title}</h3>
                    <p><strong>Author:</strong> ${book.author}</p>
                    <p><strong>Genre:</strong> ${book.genre}</p>
                    `;
                listElement.appendChild(bookDiv);
            });
        } else {
            listElement.innerHTML = `<p>No recommendations found for ${genre}.</p>`;
        }
    } catch (error) {
        listElement.innerHTML = `<p>Error fetching recommendations from API.</p>`;
        console.error('Fetch error:', error);
    }
}
