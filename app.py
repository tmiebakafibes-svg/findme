from flask import Flask, request, render_template_string
import sqlite3, os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'findme-change-this-key-12345')
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
@app.errorhandler(404)
def not_found(e):
    return "Page not found - Go back to FindMe", 404

@app.errorhandler(500)
def server_error(e):
    return "Something went wrong - Try again later", 500

def get_db():
    conn = sqlite3.connect('people.db')
    conn.execute('CREATE TABLE IF NOT EXISTS people (name TEXT, number TEXT)')
    return conn

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FindMe - Find Anyone in Nigeria | Search People By Name & Number</title>
<meta name="description" content="FindMe is Nigeria's free people search. Find anyone by name or phone number. Add yourself and be found. Created by CHRON.">
<meta name="keywords" content="FindMe, find people Nigeria, search phone number Nigeria, find anyone">
<style>
* { box-sizing: border-box; font-family: Arial, sans-serif; }
body { margin:0; padding:0; transition:0.3s; }
body.gold { background:#0a0a0a; color:white; }
body.white { background:#f5f7fa; color:#111; }
body.green { background:#e8f5e9; color:#111; }
.header { text-align:center; padding:25px 15px 10px; }
.logo { font-size:38px; font-weight:900; letter-spacing:2px; }
body.gold .logo { color:#FFD700; }
body.white .logo { color:#1a73e8; }
body.green .logo { color:#075E54; }
.sub { font-size:14px; opacity:0.7; margin-top:4px; }
.counter { display:inline-block; background:#FFD700; color:black; font-weight:900; font-size:13px; padding:6px 14px; border-radius:20px; margin-top:10px; }
body.white .counter { background:#1a73e8; color:white; }
body.green .counter { background:#075E54; color:white; }
.themes { display:flex; justify-content:center; gap:8px; margin:12px 0; }
.themes button { border:none; padding:8px 14px; border-radius:20px; font-weight:bold; cursor:pointer; font-size:12px; }
.t-gold { background:#FFD700; color:black; }
.t-white { background:white; color:#1a73e8; border:1px solid #ddd !important; }
.t-green { background:#25D366; color:white; }
.box { max-width:480px; margin:0 auto; padding:0 16px 30px; }
input { width:100%; padding:14px; border-radius:12px; border:2px solid #FFD700; margin-bottom:10px; font-size:16px; outline:none; background:white; color:black; }
body.white input { border-color:#1a73e8; }
body.green input { border-color:#25D366; }
.btn { width:100%; padding:14px; border:none; border-radius:12px; font-weight:900; font-size:16px; cursor:pointer; }
body.gold .btn-search { background:#FFD700; color:black; box-shadow:0 4px 15px rgba(255,215,0,0.4); }
body.white .btn-search { background:#1a73e8; color:white; }
body.green .btn-search { background:#075E54; color:white; }
.btn-add { background:#25D366; color:white; box-shadow:0 4px 15px rgba(37,211,102,0.4); margin-top:5px; }
.btn-share { background:#075E54; color:white; margin-top:15px; display:flex; align-items:center; justify-content:center; gap:8px; text-decoration:none; }
.section-title { text-align:center; font-size:20px; font-weight:900; margin:22px 0 12px; }
.card { background:white; color:black; padding:16px; border-radius:16px; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 2px 10px rgba(0,0,0,0.1); }
.card b { font-size:18px; }
.card span { font-size:15px; color:#555; }
.badge { background:#25D366; color:white; font-size:11px; padding:4px 8px; border-radius:20px; font-weight:bold; }
.about { background:#111; color:white; border-radius:16px; padding:18px; margin-top:20px; }
body.white .about { background:white; color:#111; box-shadow:0 2px 10px rgba(0,0,0,0.1); }
body.green .about { background:white; color:#111; }
.about h3 { color:#FFD700; margin:0 0 8px; }
body.white .about h3 { color:#1a73e8; }
body.green .about h3 { color:#075E54; }
.footer { text-align:center; font-size:12px; opacity:0.6; margin-top:15px; }
</style>
</head>
<body class="gold">
<div class="header">
<div class="logo">🔍 FINDME</div>
<div class="sub">Find Anyone in Nigeria - Fast & Free</div>
<div><span class="counter">👥 {{ total }} People Already Added</span></div>
<div class="themes">
<button class="t-gold" onclick="setTheme('gold')">✨ GOLD</button>
<button class="t-white" onclick="setTheme('white')">🤍 WHITE</button>
<button class="t-green" onclick="setTheme('green')">💚 GREEN</button>
</div>
</div>
<div class="box">
<form method="GET">
<input name="q" placeholder="Type name or number e.g. 0812..." value="{{ q }}">
<button class="btn btn-search">🔍 SEARCH</button>
</form>
<div class="section-title">+ ADD MYSELF</div>
<form method="POST" action="/add">
<input name="name" placeholder="Your Name" required>
<input name="number" placeholder="Your Number" required>
<button class="btn btn-add">+ ADD ME SECURELY</button>
</form>
<a class="btn btn-share" href="#" onclick="shareSite(); return false;">📤 SHARE FINDME ON WHATSAPP</a>
<div class="section-title">Results: {{ people|length }}</div>
{% for p in people %}
<div class="card">
<div><b>{{ p[0] }}</b><br><span>{{ p[1] }}</span></div>
<div class="badge">✓ Verified</div>
</div>
{% endfor %}
<div class="about">
<h3>About FindMe</h3>
FindMe is a free people search platform created by CHRON. Search by name or number, add yourself securely, and connect with people across Nigeria.
</div>
<div class="footer">Made by T Miebaka Fibes | Secured by Chron</div>
</div>
<script>
function setTheme(t){ document.body.className = t; localStorage.setItem('theme', t); }
let saved = localStorage.getItem('theme'); if(saved){ document.body.className = saved; }
function shareSite(){
  let text = "Check this out! 🔍 FINDME - Find Anyone in Nigeria Fast & Free. Add yourself: " + window.location.origin;
  window.open("https://wa.me/?text=" + encodeURIComponent(text), "_blank");
}
</script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    q = request.args.get('q','').strip()
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM people").fetchone()[0]
    if q:
        people = conn.execute("SELECT name, number FROM people WHERE name LIKE ? OR number LIKE ?", ('%'+q+'%','%'+q+'%')).fetchall()
    else:
        people = conn.execute("SELECT name, number FROM people LIMIT 20").fetchall()
    conn.close()
    return render_template_string(HTML, people=people, q=q, total=total)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name','').strip()
    number = request.form.get('number','').strip()
    if name and number:
        conn = get_db()
        conn.execute("INSERT INTO people VALUES (?,?)", (name, number))
        conn.commit(); conn.close()
    return home()
@app.route('/robots.txt')
def robots():
    return "User-agent: *\nAllow: /\nSitemap: https://findme-zs89.onrender.com/sitemap.xml", 200, {'Content-Type': 'text/plain'}

@app.route('/sitemap.xml')
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://findme-zs89.onrender.com/</loc><priority>1.0</priority></url>
</urlset>"""
    return xml, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
