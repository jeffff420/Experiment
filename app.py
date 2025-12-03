# SINGLE FILE - Just run: python app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>I Love You 💖</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            overflow-x: hidden;
        }
        
        .page {
            display: none;
            min-height: 100vh;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }
        
        .page.active {
            display: flex;
        }
        
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        #page-0 {
            background: linear-gradient(135deg, #ffc0cb 0%, #dda0dd 50%, #ffc0cb 100%);
        }
        
        #page-1 {
            background: linear-gradient(135deg, #dda0dd 0%, #ffc0cb 50%, #ff6b6b 100%);
        }
        
        #page-2 {
            background: linear-gradient(135deg, #ffe66d 0%, #ffc0cb 50%, #dda0dd 100%);
        }
        
        #page-3 {
            background: linear-gradient(135deg, #ffc0cb 0%, #ff6b6b 50%, #9370db 100%);
        }
        
        .title {
            font-size: 4rem;
            font-weight: bold;
            margin: 1rem 0;
            text-align: center;
        }
        
        .title.pink { color: #ff1493; }
        .title.white { color: white; }
        .title.large { font-size: 5rem; }
        .title.shadow { text-shadow: 2px 2px 10px rgba(0,0,0,0.3); }
        
        .subtitle {
            font-size: 2rem;
            margin: 1rem 0;
            text-align: center;
        }
        
        .subtitle.purple { color: #9370db; }
        .subtitle.large { font-size: 2.5rem; }
        
        .btn {
            font-size: 1.5rem;
            font-weight: bold;
            padding: 1rem 2rem;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            margin: 1rem;
        }
        
        .btn:hover {
            transform: scale(1.1);
        }
        
        .btn-pink {
            background: #ff69b4;
            color: white;
        }
        
        .btn-green {
            background: #32cd32;
            color: white;
        }
        
        .btn-green.clicked {
            transform: scale(1.5);
        }
        
        .btn-red {
            background: #ff4444;
            color: white;
            transition: all 0.2s ease;
        }
        
        .btn-gradient {
            background: linear-gradient(135deg, #ff69b4, #9370db);
            color: white;
        }
        
        .btn-white {
            background: white;
            color: #ff69b4;
        }
        
        .button-group {
            display: flex;
            gap: 2rem;
            margin: 2rem 0;
        }
        
        .emoji {
            font-size: 8rem;
            margin: 2rem 0;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        @keyframes bounce {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }
        
        @keyframes wiggle {
            0%, 100% { transform: rotate(-5deg); }
            50% { transform: rotate(5deg); }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.1); }
            50% { transform: scale(1); }
            75% { transform: scale(1.1); }
        }
        
        @keyframes fallHeart {
            0% { 
                transform: translateY(-100vh) rotate(0deg); 
                opacity: 1; 
            }
            100% { 
                transform: translateY(100vh) rotate(360deg); 
                opacity: 0; 
            }
        }
        
        .float { animation: float 3s ease-in-out infinite; }
        .bounce { animation: bounce 0.6s ease-in-out infinite; }
        .wiggle { animation: wiggle 0.5s ease-in-out infinite; }
        .pulse { animation: pulse 1s ease-in-out infinite; }
        .heartbeat { animation: heartbeat 1.5s ease-in-out infinite; }
        
        .decoration {
            position: absolute;
            font-size: 4rem;
        }
        
        .decoration.top-left { top: 2rem; left: 2rem; }
        .decoration.top-right { top: 4rem; right: 4rem; }
        .decoration.bottom-left { bottom: 4rem; left: 4rem; }
        
        .delay-1 { animation-delay: 0.3s; }
        .delay-2 { animation-delay: 0.6s; }
        
        #hearts-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }
        
        .falling-heart {
            position: absolute;
            font-size: 4rem;
            animation: fallHeart 4s linear forwards;
        }
        
        .message-card {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 2rem;
            max-width: 600px;
            margin: 2rem 0;
        }
        
        .message-text {
            font-size: 1.8rem;
            color: white;
            text-align: center;
            line-height: 1.8;
        }
        
        .emoji-row {
            display: flex;
            gap: 2rem;
            font-size: 4rem;
            margin: 2rem 0;
        }
        
        .hint {
            color: white;
            font-size: 1.5rem;
            margin-top: 2rem;
            text-align: center;
            font-style: italic;
        }
        
        .footer {
            position: absolute;
            bottom: 2rem;
            font-size: 1.5rem;
            color: white;
            opacity: 0.75;
        }
        
        @media (max-width: 768px) {
            .title { font-size: 2.5rem; }
            .title.large { font-size: 3rem; }
            .subtitle { font-size: 1.5rem; }
            .emoji { font-size: 5rem; }
            .btn { font-size: 1.2rem; padding: 0.8rem 1.5rem; }
            .message-text { font-size: 1.3rem; }
        }
    </style>
</head>
<body>
    <!-- Page 0: Welcome -->
    <div id="page-0" class="page active">
        <div class="container">
            <div class="emoji float">🎀</div>
            <h1 class="title pink">Hiii! 💕</h1>
            <p class="subtitle purple">I have something special to tell you...</p>
            <button class="btn btn-pink" onclick="nextPage(1)">Continue 💖</button>
            
            <div class="decoration top-left bounce">⭐</div>
            <div class="decoration top-right bounce delay-1">✨</div>
            <div class="decoration bottom-left bounce delay-2">🌸</div>
        </div>
    </div>

    <!-- Page 1: Question -->
    <div id="page-1" class="page">
        <div class="container">
            <div id="hearts-container"></div>
            
            <div class="emoji wiggle">🐱</div>
            <h1 class="title white shadow">Do you love me? 🥺</h1>
            
            <div class="button-group">
                <button class="btn btn-green" id="yes-btn" onclick="handleYes()">YES! 💚</button>
                <button class="btn btn-red" id="no-btn" onmouseover="moveNoButton()">No 😢</button>
            </div>
            
            <p class="hint">*Try clicking No... I dare you* 😏</p>
        </div>
    </div>

    <!-- Page 2: Yay -->
    <div id="page-2" class="page">
        <div class="container">
            <div class="emoji pulse">🎉</div>
            <h1 class="title pink">YAAAY! 🥳</h1>
            <p class="subtitle purple large">I knew you'd say yes! 💕</p>
            
            <div style="display: flex; gap: 2rem; margin: 2rem 0;">
                <span style="font-size: 5rem; animation: spin 3s linear infinite;">⭐</span>
                <span style="font-size: 5rem; animation: spin 3s linear infinite; animation-delay: 0.5s;">✨</span>
                <span style="font-size: 5rem; animation: spin 3s linear infinite; animation-delay: 1s;">💫</span>
            </div>
            
            <style>
                @keyframes spin {
                    from { transform: rotate(0deg); }
                    to { transform: rotate(360deg); }
                }
            </style>
            
            <button class="btn btn-gradient" onclick="nextPage(3)">Continue 💖</button>
        </div>
    </div>

    <!-- Page 3: Final Message -->
    <div id="page-3" class="page">
        <div class="container">
            <div class="emoji heartbeat">💖</div>
            <h1 class="title white shadow large">I Love You Too! 💕</h1>
            
            <div class="message-card">
                <p class="message-text">
                    You're the most amazing, beautiful, and wonderful person ever! 
                    Every moment with you is precious. Thank you for being you! 🌸✨
                </p>
            </div>
            
            <div class="emoji-row">
                <span>🐱</span>
                <span class="heartbeat">💝</span>
                <span>🎀</span>
                <span class="heartbeat delay-1">💕</span>
                <span>🌟</span>
            </div>
            
            <button class="btn btn-white" onclick="nextPage(0)">Start Over 🔄</button>
            
            <div class="footer">Made with 💖 just for you</div>
        </div>
    </div>

    <script>
        let currentPage = 0;
        
        function nextPage(pageNum) {
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            
            const nextPageElement = document.getElementById('page-' + pageNum);
            nextPageElement.classList.add('active');
            currentPage = pageNum;
            
            if (pageNum === 1) {
                generateHearts();
            }
        }
        
        function generateHearts() {
            const container = document.getElementById('hearts-container');
            container.innerHTML = '';
            
            for (let i = 0; i < 20; i++) {
                const heart = document.createElement('div');
                heart.className = 'falling-heart';
                heart.textContent = '💕';
                heart.style.left = Math.random() * 100 + '%';
                heart.style.animationDelay = Math.random() * 2 + 's';
                container.appendChild(heart);
            }
        }
        
        function moveNoButton() {
            const noBtn = document.getElementById('no-btn');
            const x = (Math.random() * 200) - 100;
            const y = (Math.random() * 200) - 100;
            noBtn.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
        }
        
        function handleYes() {
            const yesBtn = document.getElementById('yes-btn');
            yesBtn.classList.add('clicked');
            
            setTimeout(function() {
                nextPage(2);
                yesBtn.classList.remove('clicked');
            }, 500);
        }
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    print("=" * 60)
    print("💖 LOVE WEBSITE IS STARTING! 💖")
    print("=" * 60)
    print("🌐 Open your browser and go to:")
    print("    http://localhost:5000")
    print("    or")
    print("    http://127.0.0.1:5000")
    print("=" * 60)
    print("Press CTRL+C to stop the server")
    print("=" * 60)
    app.run(debug=True, port=5000, host='0.0.0.0')