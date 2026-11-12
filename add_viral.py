with open('app.py','r') as f:
    code = f.read()

viral_html = '''
<div style="background:#25D366;padding:15px;border-radius:10px;text-align:center;margin:15px 0;color:white;">
<h3>🔥 MAKE AM VIRAL - SHARE NOW!</h3>
<p>Share MY LOCK for your WhatsApp Status, help your friends no fall for SCAMMER!</p>
<a href="https://wa.me/?text=No%20more%20SCAMMER%20tag!%20Check%20any%20number%20for%20MY%20LOCK%20-%20Na%20you%20go%20put%20your%20own%20name!%20Add%20yourself%20FREE%20here:%20https://mylock-ph.com%20Call%2009029560760" target="_blank" style="display:block;background:white;color:#25D366;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📲 SHARE FOR WHATSAPP</a>
<a href="https://www.facebook.com/sharer/sharer.php?u=https://mylock-ph.com" target="_blank" style="display:block;background:#1877F2;color:white;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin:8px 0;">📘 SHARE FOR FACEBOOK</a>
<button onclick="navigator.clipboard.writeText('No more SCAMMER tag! Check number for MY LOCK - Add yourself FREE: https://mylock-ph.com Call 09029560760');alert('Link copied! Go paste for TikTok / Status!')" style="width:100%;background:#000;color:white;padding:12px;border-radius:8px;font-weight:bold;border:none;">🔗 COPY LINK FOR TIKTOK</button>
<p style="font-size:13px;margin-top:10px;">Share am, comment LOCK for TikTok, we go add you FREE + give you VERIFIED TICK!</p>
</div>
'''

if 'MAKE AM VIRAL' not in code:
    code = code.replace('</form>', '</form>' + viral_html)
    # Also add viral box near top after ADS box
    if 'ADS HERE' in code:
        code = code.replace('</div>', '</div>' + viral_html, 1)
    with open('app.py','w') as out:
        out.write(code)
    print("VIRAL CODE DON ENTER!")
else:
    print("VIRAL CODE DON DEY ALREADY!")
