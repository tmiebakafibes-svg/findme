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
body{font-family:Arial; background:#f0f4ff; margin:0; text-align:center}
.box{max-width:480px; margin:0 auto; padding:20px; background:white; min-height:100vh}
h1{font-size:42px; margin:10px 0 5px}
.sub{font-size:19px; color:#333; margin-bottom:20px}
input{width:95%; padding:18px; font-size:20px; margin:10px 0; border:2px solid #ddd; border-radius:12px}
button{width:100%; padding:18px; font-size:22px; font-weight:bold; background:#0057ff; color:white; border:none; border-radius:12px}
.person{display:block; width:100%; padding:16px; margin:8px 0; font-size:21px; background:#f2f2f2; border:none; border-radius:12px; text-align:left}
.result{font-size:22px; background:#e8ffe8; padding:15px; border-radius:12px}
.owner{background:#fff3cd; padding:15px; font-size:20px; border-radius:12px; margin-top:20px}
.danger{background:#ff3b30; margin-top:10px}
</style></head><body><div class="box">
<h1>🔍 FindMe</h1>
<p class="sub">Find Anyone, Anywhere in the World 🌍<br>Search by Name OR Number</p>
<form method="get">
<input name="search" placeholder="Type name OR phone number..." value="{{search}}">
<button>🔍 SEARCH</button>
</form>
{% if search %}
  {% if matches %}
    <p>Found {{matches|length}} result(s) for "{{search}}":</p>
    {% for p in matches %}
      <a href="/?search={{p['name']}}&show=1" style="text-decoration:none"><button type="button" class="person">👤 {{p['name']}}<br><span style="font-size:16px; color:#555">{{p['number']}}</span></button></a>
    {% endfor %}
  {% else %}<p class="result">No results for "{{search}}"</p>{% endif %}
{% endif %}
{% if is_admin %}
<p class="owner"><b>OWNER ONLY 👑</b><br>Total people added: <b>{{total}}</b></p>
<a href="/?admin=Miebaka2026&clear=1" onclick="return confirm('Delete ALL names?')"><button type="button" class="danger">🗑️ DELETE ALL NAMES</button></a>
{% endif %}
<hr><h2>Add Yourself</h2>
<form method="post">
<input name="name" placeholder="Your Full Name" required>
<input name="number" placeholder="Your Phone Number" required>
<button>ADD ME SECURELY ✅</button>
</form>
<p style="color:#888; font-size:14px; margin-top:20px">If someone calls you with unknown number, search the number here to know who called you.</p>
</div></body></html>
"""
@app.route("/", methods=["GET","POST"])
def home():
    is_admin=request.args.get("admin","")==ADMIN_CODE
    if is_admin and request.args.get("clear")=="1":
        save([]); return "<h1>All Deleted ✅</h1><a href='/?admin=Miebaka2026'>Go back</a>"
    data=load()
    if request.method=="POST":
        data.append({"name":request.form["name"].strip(),"number":request.form["number"].strip()})
        save(data)
    search=request.args.get("search","").strip()
    matches=[]; found=None
    if search:
        s=search.lower().replace(" ","").replace("+","")
        for p in data:
            name_match = search.lower() in p["name"].lower()
            num_clean = p["number"].replace(" ","").replace("+","").replace("-","")
            num_match = s in num_clean
            if name_match or num_match: matches.append(p)
    return render_template_string(HTML, search=search, matches=matches, found=found, show=request.args.get("show",""), total=len(data), is_admin=is_admin)
if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
