import os, json
from flask import Flask, request, render_template_string

app = Flask(__name__)
ADMIN_CODE = os.environ.get("ADMIN_CODE", "Miebaka2026")
DATA_FILE = "data.json"

def load():
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

HTML = """
<h1 style="text-align:center">🔍 FindMe</h1>
<p style="text-align:center">Find Anyone, Anywhere in the World 🌍</p>
<form method="get" style="text-align:center">
  <input name="search" placeholder="Search name..." value="{{search}}">
  <button>Search</button>
</form>
{% if search %}
  {% if found %}
    <p style="text-align:center">✅ Found: <b>{{found['name']}}</b> - {{found['number']}}</p>
  {% else %}
    <p style="text-align:center">No results for {{search}}. Tell them to add themselves below.</p>
  {% endif %}
{% endif %}
{% if is_admin %}
  <hr><p style="text-align:center"><b>OWNER ONLY:</b> Total people added: {{total}}</p>
{% endif %}
<hr>
<h3 style="text-align:center">Add Yourself</h3>
<form method="post" style="text-align:center">
  <input name="name" placeholder="Your Name" required><br><br>
  <input name="number" placeholder="Your Number" required><br><br>
  <button>ADD ME SECURELY</button>
</form>
"""

@app.route("/", methods=["GET","POST"])
def home():
    data = load()
    if request.method == "POST":
        data.append({"name": request.form["name"].strip(), "number": request.form["number"].strip()})
        save(data)
    search = request.args.get("search","").strip()
    found = None
    if search:
        for p in data:
            if p["name"].lower() == search.lower():
                found = p
                break
    is_admin = request.args.get("admin","") == ADMIN_CODE
    return render_template_string(HTML, search=search, found=found, total=len(data), is_admin=is_admin)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
