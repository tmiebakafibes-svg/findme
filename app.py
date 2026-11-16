from flask import Flask, request, render_template_string, redirect, Response
import html

app = Flask(__name__)

@app.route('/google2a3c980215f4cbe3.html')
def google_verify():
    return "google-site-verification: google2a3c980215f4cbe3.html"

people = []
ADMIN_PASSWORD = "Chronking@2026"

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="google-site-verification" content="2JOES9UqjFu0xs5P1SZLCWP33B3cuoUAnK60dshkYHk" />
<meta name="viewport" content="width=device-width, initial-scale=1"><title>FindMe by CHRON AGOPOSTAM - Find People Anywhere in the World</title>
<title>FindMe by CHRON AGOPOSTAM - Find People Anywhere in the World</title>
<meta name="description" content="FindMe helps you find people by name all over the world. Add your name, let the world find you. Created by CHRON AGOPOSTAM in Port Harcourt, Nigeria.">
<meta name="keywords" content="FindMe, find people, find person by name, CHRON AGOPOSTAM, Port Harcourt, Nigeria">
<style>
body{background:#0a0a0a;color:#fff;font-family:Arial;text-align:center;padding:20px}
h1{color:#FFD700}
input{padding:12px;width:85%;border-radius:10px;border:2px solid #FFD700;background:#111;color:#fff}
button{padding:12px 20px;border:none;border-radius:10px;font-weight:bold;margin:5px}
.gold{background:#FFD700;color:#000}
.red{background:#ff3333;color:#fff}
.green{background:#00cc66;color:#fff}
.card{background:#1a1a1a;border:1px solid #FFD700;padding:15px;border-radius:15px;margin:10px}
</style>
</head>
<body>
<h1>👑 CHRON AGOPOSTAM</h1>
<h2 style="color:#FFD700">FIND ME SEARCH</h2>
<p>Search By Name or Number - Secure Version</p>
<form method="POST" action="/search">
<input name="q" placeholder="Type number e.g. 0812...">
<br><br><button class="gold">🔍 SEARCH</button>
</form>
<hr>
<h3>+ ADD MYSELF</h3>
<form method="POST" action="/add">
<input name="name" placeholder="Your Name" required><br><br>
<input name="number" placeholder="Your Number" required><br><br>
<button class="green">+ ADD ME SECURELY</button>
</form>
<hr>
<h3>Results:</h3>
{% for p in people %}
<div class="card">
<b>{{ p[0] }}</b><br>{{ p[1] }}<br>
<form method="POST" action="/delete">
<input type="hidden" name="number" value="{{ p[1] }}">
<input type="password" name="pwd" placeholder="Admin Password" style="width:60%">
<button class="red">🗑 DELETE - Admin Only</button>
</form>
</div>
{% endfor %}
<br>
<form method="POST" action="/clean">
<input type="password" name="pwd" placeholder="Admin Password for Cleaning">
<br><br><button class="red">🧹 CLEAN ALL - Admin Only</button>
</form>
<p style="font-size:12px;color:#888">Made by T Miebaka Fibes | Secured by Chron</p>
<div style="margin-top:40px;padding:20px;background:#1a1a1a;border-radius:10px;text-align:left">
<h3 style="color:#FFD700">About FindMe</h3>
<p>FindMe is a free people search platform created by CHRON AGOPOSTAM in Port Harcourt, Nigeria. It helps people find each other by name anywhere in the world. Add your name, let the world find you.</p>
<h3 style="color:#FFD700">Privacy Policy</h3>
<p>We respect your privacy. FindMe only shows the name and information you choose to add. We do not sell your data. If you want your name removed, contact us and we will remove it. By using FindMe, you agree to use it respectfully and not to harass anyone.</p>
<p style="font-size:12px;color:#999">© 2026 FindMe by CHRON AGOPOSTAM - Port Harcourt, Nigeria</p>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, people=people)

@app.route("/search", methods=["POST"])
def search():
    q = html.escape(request.form.get("q",""))
    found = [p for p in people if q in p[0] or q in p[1]]
    return render_template_string(HTML, people=found)

@app.route("/add", methods=["POST"])
def add():
    name = html.escape(request.form.get("name","")[:50])
    number = html.escape(request.form.get("number","")[:20])
    if name and number:
        people.append((name, number))
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    if request.form.get("pwd","") != ADMIN_PASSWORD:
        return "WRONG PASSWORD! Only Admin can delete. <a href='/'>Go Back</a>"
    num = request.form.get("number","")
    global people
    people = [p for p in people if p[1] != num]
    return redirect("/")

@app.route("/clean", methods=["POST"])
def clean():
    if request.form.get("pwd","") != ADMIN_PASSWORD:
        return "WRONG PASSWORD! <a href='/'>Go Back</a>"
    people.clear()
    return redirect("/")
@app.route('/privacy')
def privacy():
    return "CHRON AGOPOSTAM - FIND ME Privacy Policy: We only store Name and Phone Number you give us. We do not sell your data. To delete your data, contact Admin on WhatsApp. Your data is stored securely."
@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://findme-zs89.onrender.com/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>
</urlset>"""
    return Response(xml, mimetype="application/xml")
if __name__ == "__main__":
    app.run()

    
