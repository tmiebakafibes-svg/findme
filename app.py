import os, json
from flask import Flask, request, render_template_string
app = Flask(__name__)
ADMIN_CODE = os.environ.get("ADMIN_CODE", "Miebaka2026")
DATA_FILE = "data.json"
def load():
    try:
        with open(DATA_FILE) as f: return json.load(f)
    except: return []
def save(d):
    with open(DATA_FILE,"w") as f: json.dump(d,f)

HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial; background:#f0f4ff; margin:0; padding:0; text-align:center}
.box{max-width:480px; margin:0 auto; padding:20px; background:white; min-height:100vh}
h1{font-size:42px; margin:10px 0 5px}
.sub{font-size:19px; color:#333; margin-bottom:20px}
input{width:95%; padding:18px; font-size:20px; margin:10px 0; border:2px solid #ddd; border-radius:12px}
button{width:100%; padding:18px; font-size:22px; font-weight:bold; background:#0057ff; color:white; border:none; border-radius:12px}
button:active{background:#003bb5}
h2{font-size:26px; margin-top:30px}
.result{font-size:22px; background:#e8ffe8; padding:15px; border-radius:12px}
.owner{background:#fff3cd; padding:15px; font-size:20px; border-radius:12px; margin-top:20px}
</style></head><body><div class="box">
<h1>🔍 FindMe</h1>
<p class="sub">Find Anyone, Anywhere in the World 🌍</p>
<form method="get">
<input name="search" placeholder="Type name to search..." value="{{search}}">
<button>🔍 SEARCH</button>
</form>
{% if search %}
  {% if found %}<p class="result">✅ Found:<br><b style="font-size:26px">{{found['name']}}</b><br>{{found['number']}}</p>
  {% else %}<p class="result">No results for {{search}}</p>{% endif %}
{% endif %}
{% if is_admin %}<p class="owner"><b>OWNER ONLY 👑</b><br>Total people added: <b>{{total}}</b></p>{% endif %}
<hr>
<h2>Add Yourself</h2>
<form method="post">
<input name="name" placeholder="Your Full Name" required>
<input name="number" placeholder="Your Phone Number" required>
<button>ADD ME SECURELY ✅</button>
</form>
<p style="color:#888; font-size:14px; margin-top:30px">Your number is only shown to people who search your exact name.</p>
</div></body></html>
"""
@app.route("/", methods=["GET","POST"])
def home():
    data=load()
    if request.method=="POST":
        data.append({"name":request.form["name"].strip(),"number":request.form["number"].strip()})
        save(data)
    search=request.args.get("search","").strip()
    found=None
    if search:
        for p in data:
            if p["name"].lower()==search.lower(): found=p; break
    is_admin=request.args.get("admin","")==ADMIN_CODE
    return render_template_string(HTML, search=search, found=found, total=len(data), is_admin=is_admin)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
