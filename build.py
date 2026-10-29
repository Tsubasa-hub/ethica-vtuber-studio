#!/usr/bin/env python3
"""src/ の本文フラグメントに共通ヘッダー・フッターを付けて、公開用 HTML をルートに書き出す。
使い方: python3 build.py  （index.html / 事業ページ / privacy.html を再生成）"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
SITE_NAME = "ETHICA VTuber Studio"
PAGES = {
    # ファイル名: (title, description, ヘッダー種別 'top'|'sub')
    "index":         ("ETHICA VTuber Studio｜所属しない、VTuber の支援スタジオ", "VTuber の「やりたい」を実現しやすく。VTuber タイアップ、イベント・自社番組、キャラクターと映像の制作、税務・法務の支援。所属不要の VTuber 支援スタジオです。", "top"),
    "entertainment": ("エンターテインメント事業｜ETHICA VTuber Studio", "VTuber 活動サポート、VTuber イベント、自社 IP 番組、イベント企画・運営。所属不要で、必要な支援だけを選べます。", "sub"),
    "marketing":     ("マーケティング事業｜ETHICA VTuber Studio", "VTuber タイアップ、コンテンツプロデュース、SNS マーケティング、グッズ・D2C プランニング。企業と VTuber をつなぎ、届く企画にします。", "sub"),
    "creative":      ("クリエイティブ事業｜ETHICA VTuber Studio", "キャラクター制作、映像制作、デザイン制作、ブランディングと構成の考案。配信の第一印象をつくります。", "sub"),
    "support":       ("クリエイターサポート事業｜ETHICA VTuber Studio", "税務、法務・契約、資金と機材の計画、条件の事前開示。ひとりでは判断しにくいことを、専門家と一緒に確認します。", "sub"),
    "privacy":       ("プライバシーポリシー｜ETHICA VTuber Studio", "ETHICA VTuber Studio のプライバシーポリシー。", "sub"),
}
BIZ = [("entertainment", "ENTERTAINMENT", "エンターテインメント事業"),
       ("marketing", "MARKETING", "マーケティング事業"),
       ("creative", "CREATIVE", "クリエイティブ事業"),
       ("support", "CREATOR SUPPORT", "クリエイターサポート事業")]

HEAD = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex,nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Noto+Sans+JP:wght@400;500;700&family=Shippori+Mincho:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
"""

def header(kind):
    nav = ("TOP", "index.html"), ("SERVICE", "index.html#service"), ("MESSAGE", "index.html#message"), ("COMPANY", "index.html#company"), ("ACCESS", "index.html#access"), ("CONTACT", "index.html#contact")
    gn = "".join(f'<a href="{h}">{t}</a>' for t, h in nav)
    sub = "".join(f'<a href="{k}.html">{ja}</a>' for k, en, ja in BIZ)
    return f"""<header class="hd{' sub' if kind == 'sub' else ''}">
<div class="wrap">
<a class="logo" href="index.html" aria-label="{SITE_NAME}">ETHICA<span class="dot"></span><small>VTUBER STUDIO</small></a>
<nav class="gnav" aria-label="グローバルナビゲーション">{gn}</nav>
<a class="hd-cta" href="index.html#contact">お問い合わせ</a>
<button class="burger" aria-label="メニュー" aria-expanded="false"><span></span><span></span><span></span></button>
</div>
</header>
<nav class="mnav" aria-label="モバイルナビゲーション">{gn}<div class="sub">{sub}</div><a class="btn" href="index.html#contact">お問い合わせ</a></nav>
"""

FOOTER = """<footer class="ft">
<div class="wrap">
<div class="row">
<a class="logo" href="index.html">ETHICA<span class="dot"></span><small>VTUBER STUDIO</small></a>
<nav class="gnav" aria-label="フッターナビゲーション"><a href="index.html">TOP</a><a href="index.html#service">SERVICE</a><a href="index.html#message">MESSAGE</a><a href="index.html#company">COMPANY</a><a href="index.html#access">ACCESS</a><a href="index.html#contact">CONTACT</a></nav>
</div>
<div class="biz">{biz}</div>
<div class="bottom"><span>© ETHICA VTuber Studio</span><a href="privacy.html">プライバシーポリシー</a></div>
</div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
""".format(biz="".join(f'<a href="{k}.html">{ja}</a>' for k, en, ja in BIZ))

for name, (title, desc, kind) in PAGES.items():
    body = (ROOT / "src" / f"{name}.html").read_text(encoding="utf-8")
    html = HEAD.format(title=title, desc=desc) + header(kind) + body + FOOTER
    (ROOT / f"{name}.html").write_text(html, encoding="utf-8")
    print("wrote", f"{name}.html", len(html))
