from flask import Flask, request, redirect

app = Flask(__name__)
@app.route('/google2a3c980215f4cbe3.html')
def google_verify():
    return "google-site-verification: google2a3c980215f4cbe3.html"
# Our small database - na here names dey
people = {}

@app.route('/')
def home():
    html = """
    <meta name="google-site-verification" content="SgdwEEzzk4MpOQr0-YrRYKTOZH0ZkBy1WUmtctrgsqU" />
    <h1 style="text-align:center;color:blue;">🔒 FIND ME SEARCH</h1>
    <p style="text-align:center;">Na YOU control your name! No be Truecaller!</p>

    <!-- ADS SPACE - NA HERE MONEY GO DEY -->
    <div style="background:yellow;text-align:center;padding:10px;border:1px solid black;">
    📢 ADS HERE - Your Shop Advert Here! Call 09029560760 / 07073840263 To Advertise - N20,000/month
    </div>
<div style="background:#25D366;padding:15px;border-radius:10px;text-align:center;margin:15px 0;color:white;">
<h3>🔥 MAKE AM VIRAL - SHARE NOW!</h3>
<p>Share FIND ME for your WhatsApp Status, help your friends no fall for SCAMMER!</p>
<a href="https://wa.me/?text=No%20more%20SCAMMER%20tag!%20Check%20any%20number%20for%20MY%20LOCK%20-%20Na%20you%20go%20put%20your%20own%20name!%20Add%20yourself%20FREE%20here:%20https://findme-ph.com%20Call%2009029560760" target="_blank" style="display:block;background:white;color:#25D366;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📲 SHARE FOR WHATSAPP</a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://findme-ph.com" target="_blank" style="display:block;background:#1877F2;color:white;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📘 SHARE FOR FACEBOOK</a>
<button onclick="navigator.clipboard.writeText('No more SCAMMER tag! Check number for FIND ME - Add yourself FREE: https://findme-ph.com Call 09029560760');alert('Link copied! Go paste for TikTok / Status!')" style="width:100%;background:#000;color:white;padding:12px;border-radius:8px;font-weight:bold;border:none;">🔗 COPY LINK FOR TIKTOK</button>
<p style="font-size:13px;margin-top:10px;">Share am, comment LOCK for TikTok, we go add you FREE + give you VERIFIED TICK!</p>
</div>

    <br>

    <div style="text-align:center;">
    <a href="/add"><button style="padding:15px;background:green;color:white;font-size:18px;">+ ADD MYSELF</button></a>
    </div>
    <br>
    <form action="/search" method="get" style="text-align:center;">
    <input name="q" placeholder="Type number e.g 0812..." style="padding:12px;width:70%;">
    <br><br>
    <button style="padding:12px;background:blue;color:white;">SEARCH</button>
    </form>
<div style="background:#25D366;padding:15px;border-radius:10px;text-align:center;margin:15px 0;color:white;">
<h3>🔥 MAKE AM VIRAL - SHARE NOW!</h3>
<p>Share FIND ME for your WhatsApp Status, help your friends no fall for SCAMMER!</p>
<a href="https://wa.me/?text=No%20more%20SCAMMER%20tag!%20Check%20any%20number%20for%20MY%20LOCK%20-%20Na%20you%20go%20put%20your%20own%20name!%20Add%20yourself%20FREE%20here:%20https://findme-ph.com%20Call%2009029560760" target="_blank" style="display:block;background:white;color:#25D366;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📲 SHARE FOR WHATSAPP</a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://findme-ph.com" target="_blank" style="display:block;background:#1877F2;color:white;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📘 SHARE FOR FACEBOOK</a>
<button onclick="navigator.clipboard.writeText('No more SCAMMER tag! Check number for FIND ME - Add yourself FREE: https://findme-ph.com Call 09029560760');alert('Link copied! Go paste for TikTok / Status!')" style="width:100%;background:#000;color:white;padding:12px;border-radius:8px;font-weight:bold;border:none;">🔗 COPY LINK FOR TIKTOK</button>
<p style="font-size:13px;margin-top:10px;">Share am, comment LOCK for TikTok, we go add you FREE + give you VERIFIED TICK!</p>
</div>

    <br><hr>
    <h3>People wey don add themself:</h3>
    """
    for phone, info in people.items():
        html += f"<p><b>{info['name']}</b> - {phone}<br>📍 {info['address']} | Age: {info['age']} | ✅ Verified by FIND ME</p><hr>"
    if not people:
        html += "<p>Nobody don add yet. Be the first!</p>"
    return html

@app.route('/add')
def add_form():
    return """
    <h2>ADD YOURSELF</h2>
    <form action="/save" method="post">
    Your Name:<br><input name="name" required style="padding:10px;width:90%;"><br><br>
    Your Phone:<br><input name="phone" required style="padding:10px;width:90%;"><br><br>
    Your Age:<br><input name="age" style="padding:10px;width:90%;"><br><br>
    Your Home Address / Area:<br><input name="address" placeholder="e.g Rumuokoro, Port Harcourt" required style="padding:10px;width:90%;"><br><br>
    <button style="padding:15px;background:green;color:white;">ADD ME NOW</button>
    </form>
<div style="background:#25D366;padding:15px;border-radius:10px;text-align:center;margin:15px 0;color:white;">
<h3>🔥 MAKE AM VIRAL - SHARE NOW!</h3>
<p>Share FIND ME for your WhatsApp Status, help your friends no fall for SCAMMER!</p>
<a href="https://wa.me/?text=No%20more%20SCAMMER%20tag!%20Check%20any%20number%20for%20MY%20LOCK%20-%20Na%20you%20go%20put%20your%20own%20name!%20Add%20yourself%20FREE%20here:%20https://findme-ph.com%20Call%2009029560760" target="_blank" style="display:block;background:white;color:#25D366;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📲 SHARE FOR WHATSAPP</a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://findme-ph.com" target="_blank" style="display:block;background:#1877F2;color:white;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📘 SHARE FOR FACEBOOK</a>
<button onclick="navigator.clipboard.writeText('No more SCAMMER tag! Check number for FIND ME - Add yourself FREE: https://findme-ph.com Call 09029560760');alert('Link copied! Go paste for TikTok / Status!')" style="width:100%;background:#000;color:white;padding:12px;border-radius:8px;font-weight:bold;border:none;">🔗 COPY LINK FOR TIKTOK</button>
<p style="font-size:13px;margin-top:10px;">Share am, comment LOCK for TikTok, we go add you FREE + give you VERIFIED TICK!</p>
</div>

    <br><a href="/">Back</a>
    """

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    phone = request.form['phone']
    age = request.form['age']
    address = request.form['address']
    people[phone] = {'name': name, 'age': age, 'address': address}
    return redirect('/')

@app.route('/search')
def search():
    q = request.args.get('q', '')
    html = f"<h2>Result for {q}</h2><a href='/'>Back</a><hr>"
    found = False
    for phone, info in people.items():
        if q in phone or q.lower() in info['name'].lower():
            html += f"<h3>✅ {info['name']}</h3><p>📞 {phone}<br>📍 {info['address']}<br>Age: {info['age']}<br>🔒 Verified by FIND ME - Na owner put am!</p>"
            found = True
    if not found:
        html += "<p>Not found. Tell the person to add themself for FIND ME!</p>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request
app = Flask(__name__)

people = [
    {"name":"T Miebaka Fibes","age":"30","phone":"0812 000 0000","address":"Port Harcourt, Rivers State"},
]

@app.route('/')
def home():
    return """
    <body style="text-align:center; font-family:Arial; background:#f0f8ff; padding:20px;">
    <h1 style="color:#1a73e8">🔍 FIND ME SEARCH</h1>
    <p>Search By Name or Number - Like Truecaller!</p>
    <form method="GET" action="/search">
    <input name="q" placeholder="Type number e.g. 0812..." style="padding:12px; width:85%; font-size:16px; border-radius:20px; border:1px solid #ccc; text-align:center;"><br><br>
    <button style="padding:12px 30px; background:#1a73e8; color:white; border:none; border-radius:10px; font-size:17px;">SEARCH</button>
    </form>
<div style="background:#25D366;padding:15px;border-radius:10px;text-align:center;margin:15px 0;color:white;">
<h3>🔥 MAKE AM VIRAL - SHARE NOW!</h3>
<p>Share FIND ME for your WhatsApp Status, help your friends no fall for SCAMMER!</p>
<a href="https://wa.me/?text=No%20more%20SCAMMER%20tag!%20Check%20any%20number%20for%20MY%20LOCK%20-%20Na%20you%20go%20put%20your%20own%20name!%20Add%20yourself%20FREE%20here:%20https://findme-ph.com%20Call%2009029560760" target="_blank" style="display:block;background:white;color:#25D366;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📲 SHARE FOR WHATSAPP</a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://findme-ph.com" target="_blank" style="display:block;background:#1877F2;color:white;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📘 SHARE FOR FACEBOOK</a>
<button onclick="navigator.clipboard.writeText('No more SCAMMER tag! Check number for FIND ME - Add yourself FREE: https://findme-ph.com Call 09029560760');alert('Link copied! Go paste for TikTok / Status!')" style="width:100%;background:#000;color:white;padding:12px;border-radius:8px;font-weight:bold;border:none;">🔗 COPY LINK FOR TIKTOK</button>
<p style="font-size:13px;margin-top:10px;">Share am, comment LOCK for TikTok, we go add you FREE + give you VERIFIED TICK!</p>
</div>
<br>
    <a href="/add" style="display:block; background:#25D366; color:white; padding:12px; border-radius:10px; text-decoration:none; font-size:17px;">+ ADD MYSELF - Make My Number Findable</a>
    <p style="color:#888; margin-top:20px;">Made by T Miebaka Fibes</p></body>
    """
@app.route('/search')
def search():
    q = request.args.get("q","").lower()
    results = [p for p in people if q in p['name'].lower() or q in p['phone']]
    cards = ""
    for p in results:
        cards += f"<div style='background:white; padding:15px; margin:10px; border-radius:12px; text-align:left; box-shadow:0 2px 5px #ccc;'><b>👤 {p['name']}</b><br>🎂 Age: {p['age']}<br>📞 Phone: {p['phone']}<br>🏠 Address: {p['address']}</div>"
    if q and not results:
        cards = f"<p>No person found for <b>{q}</b></p><p>Tell them to ADD THEMSELF!</p><a href='/add'>+ ADD THEM HERE</a>"
    return f"<body style='font-family:Arial; background:#f0f8ff; padding:20px; text-align:center;'><h2>Results for '{q}'</h2>{cards}<br><a href='/'>Back to Search</a></body>"

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get("age")
        phone = request.form.get("phone")
        address = request.form.get("address")
        people.append({"name":name,"age":age,"phone":phone,"address":address})
        return f"<body style='text-align:center; font-family:Arial; padding:40px; background:#f0f8ff;'><h2 style='color:green'>✅ SUCCESS!</h2><h3>{name} don join!</h3><p>Now anybody wey search your number go see your name and address!</p><a href='/'>Go Search Now</a></body>"
    return """
    <body style="text-align:center; font-family:Arial; background:#f0f8ff; padding:20px;">
    <h2>➕ ADD YOURSELF</h2><p>Like Truecaller - Add your details</p>
    <form method="POST" action="/add">
    <input name="name" placeholder="Your Full Name" required style="padding:12px; width:85%; margin:5px; border-radius:10px; border:1px solid #ccc;"><br>
    <input name="age" placeholder="Your Age" required style="padding:12px; width:85%; margin:5px; border-radius:10px; border:1px solid #ccc;"><br>
    <input name="phone" placeholder="Your Phone Number" required style="padding:12px; width:85%; margin:5px; border-radius:10px; border:1px solid #ccc;"><br>
    <input name="address" placeholder="Your Home Address / Area e.g. Rumuokoro, PH" required style="padding:12px; width:85%; margin:5px; border-radius:10px; border:1px solid #ccc;"><br><br>
    <button style="padding:12px 30px; background:#25D366; color:white; border:none; border-radius:10px; font-size:17px;">ADD ME NOW</button>
    </form>
<div style="background:#25D366;padding:15px;border-radius:10px;text-align:center;margin:15px 0;color:white;">
<h3>🔥 MAKE AM VIRAL - SHARE NOW!</h3>
<p>Share FIND ME for your WhatsApp Status, help your friends no fall for SCAMMER!</p>
<a href="https://wa.me/?text=No%20more%20SCAMMER%20tag!%20Check%20any%20number%20for%20MY%20LOCK%20-%20Na%20you%20go%20put%20your%20own%20name!%20Add%20yourself%20FREE%20here:%20https://findme-ph.com%20Call%2009029560760" target="_blank" style="display:block;background:white;color:#25D366;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📲 SHARE FOR WHATSAPP</a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://findme-ph.com" target="_blank" style="display:block;background:#1877F2;color:white;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📘 SHARE FOR FACEBOOK</a>
<button onclick="navigator.clipboard.writeText('No more SCAMMER tag! Check number for FIND ME - Add yourself FREE: https://findme-ph.com Call 09029560760');alert('Link copied! Go paste for TikTok / Status!')" style="width:100%;background:#000;color:white;padding:12px;border-radius:8px;font-weight:bold;border:none;">🔗 COPY LINK FOR TIKTOK</button>
<p style="font-size:13px;margin-top:10px;">Share am, comment LOCK for TikTok, we go add you FREE + give you VERIFIED TICK!</p>
</div>

    <p style="color:red; font-size:13px;">⚠️ Advice: No put your exact house number for public. Put Area only, like 'Rumuokoro, Port Harcourt' - e safe pass.</p>
    </body>
    """
@app.route('/manifest.json')
def manifest():
    return {"name":"FIND ME SEARCH","short_name":"FIND ME","start_url":"/","display":"standalone","background_color":"#f0f8ff","theme_color":"#1a73e8","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/3064/3064155.png","sizes":"512x512","type":"image/png"}]}
