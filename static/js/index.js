document.getElementById('startBtn').addEventListener('click', startDrawing);

let totalCardsToDraw = 0;
let drawnCardCount = 0;
const drawnCards = [];

function initializeDeck() {
    const deck = document.getElementById('tarotDeck');
    const resultDeck = document.getElementById('resultDeck');
    deck.innerHTML = '';
    resultDeck.innerHTML = '';
    drawnCardCount = 0;
    drawnCards.length = 0;

    for (let i = 0; i < 78; i++) {
        const cardElement = document.createElement('div');
        cardElement.className = 'tarot-card';
        cardElement.onclick = () => drawCard(cardElement);
        deck.appendChild(cardElement);
    }
}

function startDrawing() {
    const input = document.getElementById('cardCountInput');
    totalCardsToDraw = parseInt(input.value);
    if (isNaN(totalCardsToDraw) || totalCardsToDraw <= 0 || totalCardsToDraw > 78) {
        alert('請輸入有效的牌數 (1-78)');
        return;
    }
    initializeDeck();
    document.getElementById('tarotDeck').style.display = 'flex';
}

function drawCard(cardElement) {
    if (drawnCardCount >= totalCardsToDraw) {
        hideRemainingCards();
        document.getElementById('tarotDeck').style.display = 'none';
        return;
    }

    fetch('/draw_card')
        .then(res => res.json())
        .then(data => {
            const isRotated = Math.random() > 0.5;
            const rotationStyle = isRotated ? 'rotate(180deg)' : 'rotate(0deg)';
            cardElement.style.display = 'none';
            drawnCardCount++;
            drawnCards.push({ ...data, rotationStyle });
            updateResultDeck();
            if (drawnCardCount >= totalCardsToDraw) {
                hideRemainingCards();
                document.getElementById('tarotDeck').style.display = 'none';
            }
        });
}

function hideRemainingCards() {
    document.querySelectorAll('.tarot-card').forEach(card => {
        if (card.onclick) card.style.display = 'none';
    });
}

function updateResultDeck() {
    const resultDeck = document.getElementById('resultDeck');
    resultDeck.innerHTML = '';
    drawnCards.forEach(card => {
        const div = document.createElement('div');
        div.className = 'tarot-card';
        div.innerHTML = `
            <div class="card-front">
                <div class="card-image" style="background-image: url('${card.image}'); transform: ${card.rotationStyle};"></div>
                <h3>${card.name}</h3>
            </div>
        `;
        resultDeck.appendChild(div);
    });
}

// 初始載入
initializeDeck();