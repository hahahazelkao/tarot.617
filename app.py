# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, url_for
import json, random, os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 讀取卡牌資料
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'static', 'data', 'image_name.json')
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    tarot_cards = json.load(f)

# 初始洗牌
shuffled_deck = random.sample(tarot_cards, len(tarot_cards))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw_card')
def draw_card():
    global shuffled_deck
    if not shuffled_deck:
        return jsonify({'error': '所有牌都已抽完'}), 400
    card = shuffled_deck.pop(0)
    filename = card.get('filename') or os.path.basename(card.get('image', ''))
    image_url = url_for('static', filename=f"images/{filename}")
    return jsonify({
        'name': card['name'],
        'description': card['description'],
        'image': image_url
    })

@app.route('/reset_deck')
def reset_deck():
    global shuffled_deck
    shuffled_deck = random.sample(tarot_cards, len(tarot_cards))
    return jsonify({'message': '牌組已重新洗牌'})

if __name__ == '__main__':
    app.run(debug=True)