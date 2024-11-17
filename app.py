# app.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 塔羅牌卡片列表（增加每張牌的圖片路徑）
tarot_cards = [
    {"name": "The Fool", "description": "New beginnings, optimism, trust in life", "image": "static/images/fool.jpg"},
    {"name": "The Magician", "description": "Action, the power to manifest", "image": "static/images/magician.jpg"},
    {"name": "The High Priestess", "description": "Inaction, going within, the subconscious", "image": "static/images/high-priestess.jpg"},
    {"name": "The Empress", "description": "Abundance, nurturing, fertility, life in bloom", "image": "static/images/empress.jpg"},
    {"name": "The Emperor", "description": "Structure, stability, rules and power", "image": "static/images/emperor.jpg"},
    {"name": "The Hierophant", "description": "Institutions, tradition, society and its rules", "image": "static/images/hierophant.jpg"},
    {"name": "The Lovers", "description": "Sexuality, passion, choice, uniting", "image": "static/images/lovers.jpg"},
    {"name": "The Chariot", "description": "Movement, progress, integration", "image": "static/images/chariot.jpg"},
    {"name": "Strength", "description": "Courage, subtle power, integration of animal self", "image": "static/images/strength.jpg"},
    {"name": "The Hermit", "description": "Meditation, solitude, consciousness", "image": "static/images/hermit.jpg"},
    {"name": "Wheel of Fortune", "description": "Cycles, change, ups and downs", "image": "static/images/fortune-wheel.jpg"},
    {"name": "Justice", "description": "Fairness, equality, balance", "image": "static/images/justice.jpg"},
    {"name": "The Hanged Man", "description": "Surrender, new perspective, enlightenment", "image": "static/images/hanged-man.jpg"},
    {"name": "Death", "description": "Endings, transformation, transition", "image": "static/images/death.jpg"},
    {"name": "Temperance", "description": "Balance, moderation, patience", "image": "static/images/temperance.jpg"},
    {"name": "The Devil", "description": "Destructive patterns, addiction, giving away power", "image": "static/images/devil.jpg"},
    {"name": "The Tower", "description": "Collapse of stable structures, release, sudden insight", "image": "static/images/tower.jpg"},
    {"name": "The Star", "description": "Hope, calm, a good omen", "image": "static/images/stars.jpg"},
    {"name": "The Moon", "description": "Mystery, the subconscious, dreams", "image": "static/images/moon.jpg"},
    {"name": "The Sun", "description": "Success, happiness, all will be well", "image": "static/images/sun.jpg"},
    {"name": "Judgement", "description": "Reflection, reckoning, awakening", "image": "static/images/judgement.jpg"},
    {"name": "The World", "description": "Completion, wholeness, attainment, celebration of life", "image": "static/images/world.jpg"},
    # Minor Arcana - Wands
    {"name": "Ace of Wands", "description": "Inspiration, new opportunities, growth, potential", "image": "static/images/ace-wands.jpg"},
    {"name": "Two of Wands", "description": "Future planning, progress, decisions, discovery", "image": "static/images/two-wands.jpg"},
    {"name": "Three of Wands", "description": "Preparation, foresight, enterprise, expansion", "image": "static/images/three-wands.jpg"},
    {"name": "Four of Wands", "description": "Celebration, harmony, marriage, home, community", "image": "static/images/four-wands.jpg"},
    {"name": "Five of Wands", "description": "Conflict, disagreements, competition, tension", "image": "static/images/five-wands.jpg"},
    {"name": "Six of Wands", "description": "Success, public recognition, progress, self-confidence", "image": "static/images/six-wands.jpg"},
    {"name": "Seven of Wands", "description": "Challenge, competition, protection, perseverance", "image": "static/images/seven-wands.jpg"},
    {"name": "Eight of Wands", "description": "Movement, fast-paced change, action, alignment", "image": "static/images/eight-wands.jpg"},
    {"name": "Nine of Wands", "description": "Resilience, courage, persistence, test of faith", "image": "static/images/nine-wands.jpg"},
    {"name": "Ten of Wands", "description": "Burden, extra responsibility, hard work, completion", "image": "static/images/ten-wands.jpg"},
    {"name": "Page of Wands", "description": "Inspiration, ideas, discovery, limitless potential", "image": "static/images/page-wands.jpg"},
    {"name": "Knight of Wands", "description": "Energy, passion, inspired action, adventure", "image": "static/images/knight-wands.jpg"},
    {"name": "Queen of Wands", "description": "Courage, determination, joy, vibrancy", "image": "static/images/queen-wands.jpg"},
    {"name": "King of Wands", "description": "Natural-born leader, vision, entrepreneur, honor", "image": "static/images/king-wands.jpg"},
    # Minor Arcana - Cups
    {"name": "Ace of Cups", "description": "Love, new relationships, compassion, creativity", "image": "static/images/ace-cups.jpg"},
    {"name": "Two of Cups", "description": "Unified love, partnership, mutual attraction", "image": "static/images/two-cups.jpg"},
    {"name": "Three of Cups", "description": "Celebration, friendship, creativity, collaborations", "image": "static/images/three-cups.jpg"},
    {"name": "Four of Cups", "description": "Meditation, contemplation, apathy, reevaluation", "image": "static/images/four-cups.jpg"},
    {"name": "Five of Cups", "description": "Regret, failure, disappointment, pessimism", "image": "static/images/five-cups.jpg"},
    {"name": "Six of Cups", "description": "Revisiting the past, childhood memories, innocence", "image": "static/images/six-cups.jpg"},
    {"name": "Seven of Cups", "description": "Opportunities, choices, wishful thinking, illusion", "image": "static/images/seven-cups.jpg"},
    {"name": "Eight of Cups", "description": "Disappointment, abandonment, withdrawal, escapism", "image": "static/images/eight-cups.jpg"},
    {"name": "Nine of Cups", "description": "Contentment, satisfaction, gratitude, wish come true", "image": "static/images/nine-cups.jpg"},
    {"name": "Ten of Cups", "description": "Divine love, blissful relationships, harmony, alignment", "image": "static/images/ten-cups.jpg"},
    {"name": "Page of Cups", "description": "Creative opportunities, intuitive messages, curiosity", "image": "static/images/page-cups.jpg"},
    {"name": "Knight of Cups", "description": "Romance, charm, 'Knight in shining armor,' imagination", "image": "static/images/knight-cups.jpg"},
    {"name": "Queen of Cups", "description": "Compassion, care, emotional stability, intuition", "image": "static/images/queen-cups.jpg"},
    {"name": "King of Cups", "description": "Emotionally balanced, compassionate, diplomatic", "image": "static/images/king-cups.jpg"},
    # Minor Arcana - Swords
    {"name": "Ace of Swords", "description": "Breakthrough, clarity, sharp mind", "image": "static/images/ace-swords.jpg"},
    {"name": "Two of Swords", "description": "Difficult decisions, weighing up options, an impasse", "image": "static/images/two-swords.jpg"},
    {"name": "Three of Swords", "description": "Heartbreak, emotional pain, sorrow, grief", "image": "static/images/three-swords.jpg"},
    {"name": "Four of Swords", "description": "Rest, relaxation, meditation, contemplation", "image": "static/images/four-swords.jpg"},
    {"name": "Five of Swords", "description": "Conflict, disagreements, competition, defeat", "image": "static/images/five-swords.jpg"},
    {"name": "Six of Swords", "description": "Transition, change, rite of passage", "image": "static/images/six-swords.jpg"},
    {"name": "Seven of Swords", "description": "Betrayal, deception, getting away with something", "image": "static/images/seven-swords.jpg"},
    {"name": "Eight of Swords", "description": "Imprisonment, self-victimization", "image": "static/images/eight-swords.jpg"},
    {"name": "Nine of Swords", "description": "Anxiety, hopelessness, nightmares", "image": "static/images/nine-swords.jpg"},
    {"name": "Ten of Swords", "description": "Painful endings, deep wounds, betrayal", "image": "static/images/ten-swords.jpg"},
    {"name": "Page of Swords", "description": "Curiosity, restlessness, mental energy", "image": "static/images/page-swords.jpg"},
    {"name": "Knight of Swords", "description": "Ambitious, action-oriented, driven to succeed", "image": "static/images/knight-swords.jpg"},
    {"name": "Queen of Swords", "description": "Complexity, perception, clear-mindedness", "image": "static/images/queen-swords.jpg"},
    {"name": "King of Swords", "description": "Intellectual, clear thinker, truthful, authoritative", "image": "static/images/king-swords.jpg"},
    # Minor Arcana - Pentacles
    {"name": "Ace of Pentacles", "description": "New financial or career opportunity, manifestation", "image": "static/images/ace-pentacles.jpg"},
    {"name": "Two of Pentacles", "description": "Balance, adaptability, time management", "image": "static/images/two-pentacles.jpg"},
    {"name": "Three of Pentacles", "description": "Teamwork, collaboration, skill development", "image": "static/images/three-pentacles.jpg"},
    {"name": "Four of Pentacles", "description": "Control, security, conservation", "image": "static/images/four-pentacles.jpg"},
    {"name": "Five of Pentacles", "description": "Financial loss, poverty, isolation", "image": "static/images/five-pentacles.jpg"},
    {"name": "Six of Pentacles", "description": "Generosity, charity, sharing, giving and receiving", "image": "static/images/six-pentacles.jpg"},
    {"name": "Seven of Pentacles", "description": "Long-term view, sustainable results, perseverance", "image": "static/images/seven-pentacles.jpg"},
    {"name": "Eight of Pentacles", "description": "Apprenticeship, repetitive tasks, skill development", "image": "static/images/eight-pentacles.jpg"},
    {"name": "Nine of Pentacles", "description": "Abundance, luxury, self-sufficiency, financial independence", "image": "static/images/nine-pentacles.jpg"},
    {"name": "Ten of Pentacles", "description": "Wealth, inheritance, family, establishment", "image": "static/images/ten-pentacles.jpg"},
    {"name": "Page of Pentacles", "description": "Manifestation, financial opportunity, new job", "image": "static/images/page-pentacles.jpg"},
    {"name": "Knight of Pentacles", "description": "Hard work, productivity, routine, conservatism", "image": "static/images/knight-pentacles.jpg"},
    {"name": "Queen of Pentacles", "description": "Practical, homely, motherly, down-to-earth", "image": "static/images/queen-pentacles.jpg"},
    {"name": "King of Pentacles", "description": "Wealth, business, leadership, security, discipline", "image": "static/images/king-pentacles.jpg"},
]

shuffled_deck = []

def shuffle_deck():
    """打亂牌組並保存"""
    global shuffled_deck
    shuffled_deck = random.sample(tarot_cards, len(tarot_cards))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw_card', methods=['GET'])
def draw_card():
    # 檢查是否還有牌可以抽
    if not shuffled_deck:
        return jsonify({"error": "所有牌都已抽完"}), 400
    
    # 從洗好的牌組中抽取第一張
    card = shuffled_deck.pop(0)
    return jsonify(card)

@app.route('/reset_deck', methods=['GET'])
def reset_deck():
    """重置牌組並重新洗牌"""
    shuffle_deck()
    return jsonify({"message": "牌組已重新洗牌"})

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    shuffle_deck()  # 啟動伺服器時打亂牌組
    app.run(debug=True)