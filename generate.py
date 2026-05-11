import feedparser
from datetime import datetime

feeds = [
    "https://feeds.reuters.com/reuters/worldNews",
    "https://feeds.reuters.com/reuters/businessNews"
]

cards = ""

for url in feeds:
    feed = feedparser.parse(url)

    for entry in feed.entries[:3]:

        title = entry.title
        link = entry.link
        summary = entry.get("summary", "")[:160]

        cards += f"""
<div class="card">

<div class="tag">
GLOBAL / ECONOMY
</div>

<div class="headline">
{title}
</div>

<div class="summary">
{summary}
</div>

<div class="source">
Reuters · {datetime.now().strftime('%Y.%m.%d')} ·
<a href="{link}" target="_blank">
Read Source →
</a>
</div>

</div>
"""

html = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Tonight Brief</title>

<style>
body{{
margin:0;
padding:0;
background:#f5f3ee;
color:#111;
font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif;
line-height:1.7;
}}

.container{{
max-width:680px;
margin:auto;
padding:56px 20px 80px;
}}

.title{{
font-size:52px;
font-weight:900;
}}

.subtitle{{
margin-top:8px;
font-size:24px;
color:#666;
}}

.meta{{
margin-top:28px;
font-size:15px;
line-height:1.8;
color:#666;
}}

.card{{
background:white;
border-radius:22px;
padding:24px;
margin-top:24px;
}}

.tag{{
font-size:12px;
letter-spacing:1px;
color:#888;
margin-bottom:12px;
}}

.headline{{
font-size:28px;
font-weight:700;
margin-bottom:14px;
}}

.summary{{
font-size:17px;
color:#333;
}}

.source{{
margin-top:18px;
font-size:14px;
color:#777;
}}
</style>
</head>

<body>

<div class="container">

<div class="title">
TONIGHT BRIEF
</div>

<div class="subtitle">
for Eliza
</div>

<div class="meta">
{datetime.now().strftime('%B %d, %Y')}<br>
Edition Auto
</div>

{cards}

</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Tonight Brief updated.")
