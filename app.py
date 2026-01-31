import os
import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'cupid_arrow_secret_key'  # Change this for production

# --- CONFIGURATION ---
# Set this to False to enforce real dates. Set to True to see everything now.
DEV_MODE = True 

# Users (Username: 'love', Password: 'you')
USERS = {
    "love": generate_password_hash("you")
}

# The "Episodes" (Valentine Week)
# Dates are YYYY-MM-DD. 
CONTENT_DATA = [
    {
        "id": "rose",
        "date": "2026-02-07",
        "title": "Ep 1: The Red Rose",
        "subtitle": "Rose Day Special",
        "description": "Like a rose, you bring color and fragrance to my life. A small start to a big week.",
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        "memory_text": "Remember when we first met? I knew then that life would be rosier with you.",
        "secret_answer": "rose"
    },
    {
        "id": "propose",
        "date": "2026-02-08",
        "title": "Ep 2: The Question",
        "subtitle": "Propose Day",
        "description": "It takes courage to ask, but it's easy when the answer is in the heart.",
        "image": "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?auto=format&fit=crop&w=800&q=80",
        "memory_text": "If I had to ask you a thousand times, I would choose you every single time.",
        "secret_answer": "yes"
    },
    {
        "id": "chocolate",
        "date": "2026-02-09",
        "title": "Ep 3: Sweetness",
        "subtitle": "Chocolate Day",
        "description": "Life is like a box of chocolates, but you are the sweetest truffle in the box.",
        "image": "https://images.unsplash.com/photo-1511381939415-e44015466834?auto=format&fit=crop&w=800&q=80",
        "memory_text": "You are sweeter than any dessert I've ever had.",
        "secret_answer": "sweet"
    },
    {
        "id": "teddy",
        "date": "2026-02-10",
        "title": "Ep 4: Cuddles",
        "subtitle": "Teddy Day",
        "description": "Soft, warm, and always there to hold. Sending you a virtual bear hug.",
        "image": "https://images.unsplash.com/photo-1559570278-eb8d71d06403?auto=format&fit=crop&w=800&q=80",
        "memory_text": "I wish I could shrink you down and carry you in my pocket like a teddy bear.",
        "secret_answer": "hug"
    },
    {
        "id": "promise",
        "date": "2026-02-11",
        "title": "Ep 5: The Vow",
        "subtitle": "Promise Day",
        "description": "Promises are the glue of love. Here is mine to you, written in code and stone.",
        "image": "https://images.unsplash.com/photo-1516575150278-77136aed6920?auto=format&fit=crop&w=800&q=80",
        "memory_text": "I promise to be your debugger when life throws runtime errors.",
        "secret_answer": "forever"
    },
    {
        "id": "hug",
        "date": "2026-02-12",
        "title": "Ep 6: Embrace",
        "subtitle": "Hug Day",
        "description": "Sometimes words are not enough. A hug says everything the heart feels.",
        "image": "https://images.unsplash.com/photo-1517677130602-23a321cf7b98?auto=format&fit=crop&w=800&q=80",
        "memory_text": "Your arms are my favorite place to be.",
        "secret_answer": "warmth"
    },
    {
        "id": "kiss",
        "date": "2026-02-13",
        "title": "Ep 7: Spark",
        "subtitle": "Kiss Day",
        "description": "A touch of lips, a seal of love. The anticipation before the big day.",
        "image": "https://images.unsplash.com/photo-1514316454349-750a7fd3da3a?auto=format&fit=crop&w=800&q=80",
        "memory_text": "Sealed with a kiss.",
        "secret_answer": "mwah"
    },
    {
        "id": "valentine",
        "date": "2026-02-14",
        "title": "Season Finale: Us",
        "subtitle": "Valentine's Day",
        "description": "The grand finale. The reason for the season. My Forever Valentine.",
        "image": "https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&w=800&q=80",
        "memory_text": "You are my favorite movie, my favorite song, and my favorite person.",
        "secret_answer": "love"
    }
]

# --- HELPERS ---
def get_content_status():
    """Determines which episodes are locked based on current date."""
    today = datetime.date.today().isoformat()
    processed_content = []
    
    for item in CONTENT_DATA:
        # Create a copy so we don't mutate the global state permanently
        item_copy = item.copy()
        
        if DEV_MODE:
            item_copy['locked'] = False
        else:
            item_copy['locked'] = item['date'] > today
            
        processed_content.append(item_copy)
    
    return processed_content

def get_episode_by_id(ep_id):
    content = get_content_status()
    for item in content:
        if item['id'] == ep_id:
            return item
    return None

# --- ROUTES ---

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('profiles'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and check_password_hash(USERS[username], password):
            session['user'] = username
            return redirect(url_for('profiles'))
        else:
            flash('Invalid credentials. Try "love" and "you".')
            
    return render_template('login.html')

@app.route('/profiles')
def profiles():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('profiles.html')

@app.route('/browse')
def browse():
    if 'user' not in session: return redirect(url_for('login'))
    
    content = get_content_status()
    # Feature the first unlocked item, or the last one if all unlocked
    featured = next((item for item in reversed(content) if not item['locked']), content[0])
    
    return render_template('browse.html', content=content, featured=featured)

@app.route('/watch/<ep_id>')
def watch(ep_id):
    if 'user' not in session: return redirect(url_for('login'))
    
    episode = get_episode_by_id(ep_id)
    
    if not episode:
        return redirect(url_for('browse'))
        
    if episode['locked']:
        flash("Not available yet! Patience is romantic.")
        return redirect(url_for('browse'))
        
    return render_template('watch.html', episode=episode, is_finale=(ep_id == 'valentine'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)