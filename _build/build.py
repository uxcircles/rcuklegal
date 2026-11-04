"""Build the Chu & Company concept site.

    python3 _build/build.py

Writes the English pages into the repo root and the Traditional Chinese pages
into zh/. Text is written as L(English, 繁體中文). Only needs Python 3.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OFFICIAL = "https://www.rcuklegal.co.uk/"
PHONE = "020 8897 3366"
PHONE_INTL = "+44 (0)20 8897 3366"
TEL = "tel:+442088973366"
WHATSAPP = "07990 667 894"
WA = "https://wa.me/447990667894"
FAX = "020 8897 6633"
EMAIL = "info@rcuklegal.co.uk"
SRA_NO = "8006741"
SRA_REGISTER = "https://www.sra.org.uk/consumers/register/"
ADDRESS_LINES = ["Unit 1, Sheraton Skyline Hotel", "Bath Road (A4), Hayes", "Middlesex UB3 5BP"]
MAPS = "https://www.google.com/maps/search/?api=1&query=Sheraton+Skyline+Hotel+Bath+Road+Hayes+UB3+5BP"
GOV_FEES = "https://www.gov.uk/government/publications/visa-regulations-revised-table"
GOV_IHS = "https://www.gov.uk/healthcare-immigration-application/how-much-pay"
GOV_BNO = "https://www.gov.uk/british-national-overseas-bno-visa"

LANG = "en"


def L(en, zh):
    return zh if LANG == "zh" else en


def asset(path):
    return ("../" if LANG == "zh" else "") + path


# ---------------------------------------------------------------- icons
def icon(name, cls="ic"):
    paths = {
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
        "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "ext": '<path d="M7 17 17 7M9 7h8v8"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "close": '<path d="M6 6l12 12M18 6 6 18"/>',
        "chat": '<path d="M20 11.5a8 8 0 0 1-11.8 7L4 20l1.4-4A8 8 0 1 1 20 11.5z"/><path d="M9 10.5h.01M12.5 10.5h.01M16 10.5h.01"/>',
        "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "pound": '<path d="M17 20H7c2-1.5 3-3.5 3-6V8.5A3.5 3.5 0 0 1 16.5 7"/><path d="M6.5 13h8"/>',
        "lang": '<path d="M4 5h9M8.5 3v2M6 5c.5 3 2.5 5.5 5 7M11 5c-.7 3.4-3 6.3-6 8"/><path d="m12 21 4.5-10 4.5 10M13.6 17.5h5.8"/>',
        "plane": '<path d="M21 15.5 13.5 11V5.5a1.5 1.5 0 0 0-3 0V11L3 15.5v2l7.5-2.3v3.6L8.5 20v1.5L12 20.5l3.5 1V20l-2-1.2v-3.6l7.5 2.3z"/>',
        "passport": '<rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M9 16.5h6"/>',
        "scale": '<path d="M12 4v16M7 20h10M5 7h14"/><path d="m5 7-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/>',
        "building": '<rect x="4" y="3" width="11" height="18" rx="1"/><path d="M15 9h5v12h-5M8 7h3M8 11h3M8 15h3"/>',
        "key": '<circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l2 2M15 8l2 2"/>',
        "doc": '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M8.5 13h7M8.5 17h5"/>',
        "gavel": '<path d="m14 4 6 6M11 7l6 6M12.5 5.5l-5 5M18.5 11.5l-5 5"/><path d="M10 13 3 20"/><path d="M13 21h8"/>',
        "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
        "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    }
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')


# The firm's wordmark sits on a pale-blue square; the mark keeps that idea.
BRAND_MARK = (
    '<svg class="brand-mark" viewBox="0 0 44 44" aria-hidden="true">'
    '<rect x="0" y="0" width="30" height="30" rx="3" fill="#cfe1f2"/>'
    '<rect x="9" y="9" width="35" height="35" rx="3" fill="#002e5d"/>'
    '<text x="26.5" y="33" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-size="19" '
    'font-weight="600" fill="#ffffff">C<tspan fill="#9cc5ea" font-style="italic" font-weight="400">&amp;</tspan></text>'
    '</svg>'
)

PAGES = ["index.html", "services.html", "bno-visa.html", "fees.html", "about.html", "contact.html"]


def nav_items():
    return [
        ("services.html", L("Services", "服務範圍")),
        ("bno-visa.html", L("BN(O) visa", "BN(O) 簽證")),
        ("fees.html", L("Fees", "收費")),
        ("about.html", L("About us", "關於我們")),
        ("contact.html", L("Contact", "聯絡我們")),
    ]


def brand():
    return (f'<a class="brand" href="index.html" aria-label="{L("Chu &amp; Company Solicitors, home", "Chu &amp; Company 律師行主頁")}">{BRAND_MARK}'
            '<span class="brand-text"><span class="brand-name" lang="en">Chu <span>&amp;</span> Company</span>'
            f'<span class="brand-sub">{L("Solicitors · London Heathrow", "律師行 · 倫敦希斯路")}</span></span></a>')


def lang_switch(page):
    en_href = ("../" if LANG == "zh" else "") + page
    zh_href = page if LANG == "zh" else "zh/" + page
    cur = ' aria-current="true"'
    return (f'<div class="lang-switch" aria-label="{L("Language", "語言")}">'
            f'<a href="{en_href}" lang="en-GB" hreflang="en-GB"{cur if LANG == "en" else ""}>EN</a>'
            f'<a href="{zh_href}" lang="zh-Hant" hreflang="zh-Hant"{cur if LANG == "zh" else ""}>中文</a></div>')


def layout(page, title, description, body):
    current = ' aria-current="page"'
    nav = "\n      ".join(
        f'<a href="{href}"{current if href == page else ""}>{label}</a>' for href, label in nav_items()
    )
    html_lang = L("en-GB", "zh-Hant-HK")
    zh_fonts = "&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@500;600" if LANG == "zh" else ""
    return f"""<!doctype html>
<html lang="{html_lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#002e5d">
<link rel="alternate" hreflang="en-GB" href="{("../" if LANG == "zh" else "") + page}">
<link rel="alternate" hreflang="zh-Hant" href="{page if LANG == "zh" else "zh/" + page}">
<link rel="icon" href="{asset("assets/img/favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Instrument+Sans:wght@400;500;600{zh_fonts}&display=swap">
<link rel="stylesheet" href="{asset("assets/css/style.css")}">
</head>
<body class="lang-{LANG}">
<a class="skip" href="#main">{L("Skip to content", "跳到主要內容")}</a>
<div class="concept-bar" role="note">
  <div class="container concept-inner">
    <p><span class="concept-tag">Concept</span><span class="concept-long">{L(f'Concept redesign. Not the <a href="{OFFICIAL}" target="_blank" rel="noopener">official Chu &amp; Company website</a>.', f'改版概念設計，並非 <a href="{OFFICIAL}" target="_blank" rel="noopener">Chu &amp; Company 官方網站</a>。')}</span></p>
    <a href="https://ux-circles.com/web" target="_blank" rel="noopener"><span class="concept-by">{L("Designed by ", "設計：")}</span><strong>UX CIRCLES</strong> {icon("ext", "ic-ext")}</a>
  </div>
</div>
<header class="site-header">
  <div class="container header-inner">
    {brand()}
    <nav class="nav" id="site-nav" aria-label="{L("Main", "主選單")}">
      {nav}
      <div class="nav-extra">
        <a class="nav-phone" href="{TEL}">{icon("phone")}<span>{PHONE}</span></a>
        <a class="btn btn-primary" href="contact.html#enquiry">{L("Free consultation", "免費初步諮詢")}</a>
      </div>
    </nav>
    <div class="header-tools">
      {lang_switch(page)}
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{L("Menu", "選單")}">{icon("menu", "ic-open")}{icon("close", "ic-close")}</button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        {brand()}
        <p>{L("English and Chinese-speaking solicitors at London Heathrow, advising on immigration, disputes, business, property, criminal matters and documents since 2016.",
              "位於倫敦希斯路機場地區的中英雙語律師行，自 2016 年起處理移民、民事訴訟、企業商業、物業、刑事及文件公證事務。")}</p>
        <p class="footer-langs">English · 廣東話 · 普通話</p>
      </div>
      <div>
        <p class="footer-h">{L("Office", "辦公室")}</p>
        <address>{"<br>".join(ADDRESS_LINES)}</address>
        <a class="footer-map" href="{MAPS}" target="_blank" rel="noopener">{L("Open in Google Maps", "在 Google 地圖開啟")} {icon("ext", "ic-ext")}</a>
      </div>
      <div>
        <p class="footer-h">{L("Contact", "聯絡")}</p>
        <ul>
          <li><a href="{TEL}">{L("Tel", "電話")} {PHONE}</a></li>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp {WHATSAPP}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><span class="muted">{L("Fax", "傳真")} {FAX}</span></li>
        </ul>
      </div>
      <div>
        <p class="footer-h">{L("Information", "資料")}</p>
        <ul>
          <li><a href="fees.html">{L("Fees and pricing", "收費資料")}</a></li>
          <li><a href="about.html#complaints">{L("Complaints procedure", "投訴程序")}</a></li>
          <li><a href="{OFFICIAL}privacy-notice" target="_blank" rel="noopener">{L("Privacy notice", "私隱政策（英文）")}</a></li>
          <li><a href="{OFFICIAL}cookies-policy" target="_blank" rel="noopener">{L("Cookie policy", "Cookie 政策（英文）")}</a></li>
          <li><a href="{OFFICIAL}accessibility" target="_blank" rel="noopener">{L("Legal notices", "法律聲明（英文）")}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <p>{L(f'Chu &amp; Company is authorised and regulated by the Solicitors Regulation Authority, SRA No. {SRA_NO}. <a href="{SRA_REGISTER}" target="_blank" rel="noopener">Check the SRA register</a>.',
            f'Chu &amp; Company 由英格蘭及威爾斯律師監管局（SRA）授權及監管，SRA 編號 {SRA_NO}。<a href="{SRA_REGISTER}" target="_blank" rel="noopener">查閱 SRA 登記冊</a>。')}</p>
      <p>&copy; Chu &amp; Company. {L("Concept redesign by", "改版概念設計：")} <a href="https://ux-circles.com/web" target="_blank" rel="noopener">UX CIRCLES</a>.</p>
    </div>
  </div>
</footer>
<div class="mobile-cta">
  <a class="btn btn-ghost" href="{TEL}">{icon("phone")} {L("Call", "致電")}</a>
  <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{icon("chat")} WhatsApp</a>
  <a class="btn btn-primary" href="contact.html#enquiry">{L("Enquire", "查詢")}</a>
</div>
<script src="{asset("assets/js/main.js")}"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- shared content
def areas():
    """slug, icon, name, summary, items, price line, price link"""
    return [
        ("immigration", "passport", L("Immigration", "移民簽證"),
         L("Visas, settlement and British citizenship, for individuals, families and businesses sponsoring staff.",
           "簽證、永久居留及入籍申請，服務個人、家庭及需要擔保員工的企業。"),
         [L("BN(O) visa for Hong Kong families", "香港家庭 BN(O) 簽證"),
          L("Spouse, partner and family visas", "配偶、伴侶及家庭簽證"),
          L("Indefinite Leave to Remain", "永久居留（ILR）"),
          L("British citizenship (naturalisation and registration)", "入籍英國（歸化及登記）"),
          L("Skilled Worker visas and sponsor licences", "技術工作簽證及擔保牌照"),
          L("Business routes: innovator, start-up and overseas business representative", "商業簽證：創新者、初創及海外企業代表"),
          L("Student, Youth Mobility and visitor visas", "學生、青年交流計劃及訪客簽證")],
         L("Fixed fees from <strong>£800</strong> + VAT", "定額收費 <strong>£800</strong> 起（另加增值稅）"), "fees.html#immigration"),
        ("litigation", "scale", L("Litigation &amp; Dispute Resolution", "民事訴訟及爭議解決"),
         L("Getting money back and settling disputes, from small claims and unpaid invoices to court proceedings and arbitration.",
           "追討欠款及解決糾紛，由小額錢債、未付發票，到法院訴訟及仲裁。"),
         [L("Small claims", "小額錢債"), L("Civil litigation", "民事訴訟"), L("Property litigation", "物業糾紛"),
          L("Arbitration", "仲裁"), L("Debt recovery and collection", "追收債務欠款")],
         L("Debt recovery from <strong>£350</strong> + VAT", "追收欠款 <strong>£350</strong> 起（另加增值稅）"), "fees.html#debt"),
        ("corporate", "building", L("Corporate &amp; Commercial", "企業及商業法律"),
         L("Setting up, expanding or restructuring a business, with practical, commercially focused advice for companies of every size.",
           "成立、擴展或重組業務，為不同規模的企業提供務實、以商業為本的意見。"),
         [L("Setting up a UK business from abroad", "由海外來英成立公司"),
          L("Partnerships, joint ventures and shareholders’ agreements", "合夥、合營及股東協議"),
          L("Commercial contracts and agency agreements", "商務合約及代理協議"),
          L("Private equity", "私募股權"), L("Restructuring and insolvency", "重組及無力償債"),
          L("Commercial disputes and international business", "商業糾紛及國際業務")],
         L("Quoted per matter after a free first consultation", "免費初步諮詢後按個案報價"), "fees.html#rates"),
        ("property", "key", L("Property", "物業"),
         L("Commercial property leasing, and the sale and purchase of residential and commercial property.",
           "商用物業租賃，以及住宅及商業物業買賣。"),
         [L("Commercial leases for landlords and tenants", "代表業主或租客處理商業租約"),
          L("Freehold and leasehold sales and purchases", "永久業權及租賃業權物業買賣"),
          L("Stamp Duty and Land Registry", "印花稅及土地註冊處手續")],
         L("Conveyancing from <strong>£1,150</strong> + VAT", "物業轉讓 <strong>£1,150</strong> 起（另加增值稅）"), "fees.html#conveyancing"),
        ("documents", "doc", L("Documents &amp; Certification", "文件宣誓及公證"),
         L("Certified copies, oaths and declarations, powers of attorney and apostilles, usually handled the same day.",
           "文件核證副本、宣誓及聲明、授權書及海牙認證，一般即日辦妥。"),
         [L("Certified true copies", "核證副本"), L("Oaths, affirmations and statutory declarations", "宣誓、非宗教式宣誓及法定聲明"),
          L("Power of Attorney and Lasting Power of Attorney", "授權書及持久授權書"),
          L("Apostille and legalisation through the FCDO", "經英國外交部辦理海牙認證"),
          L("ID1 identity verification for HM Land Registry", "土地註冊處 ID1 身份核實")],
         L("Certified copies <strong>£10</strong> + VAT", "核證副本 <strong>£10</strong>（另加增值稅）"), "fees.html#documents"),
        ("criminal", "gavel", L("Criminal Law", "刑事訴訟"),
         L("Advice and representation from the police station onwards, explained in your own language.",
           "由警署會面開始提供意見及代表，以你熟悉的語言解釋每一步。"),
         [L("Arrest and police station interviews", "被捕及警署會面"), L("Assault", "襲擊"),
          L("Motoring offences", "交通違例"), L("Sexual offences", "性罪行")],
         L(f'Call <strong>{PHONE}</strong> to talk it through', f'致電 <strong>{PHONE}</strong> 查詢'), None),
    ]


def immigration_fees():
    return [
        (L("BN(O) visa", "BN(O) 簽證"), "£1,000 – £2,000"),
        (L("Spouse, partner and family visas (Appendix FM)", "配偶、伴侶及家庭簽證（Appendix FM）"), "£1,800 – £3,800"),
        (L("Indefinite Leave to Remain", "永久居留（ILR）"), "£1,500 – £3,500"),
        (L("British citizenship: naturalisation or registration", "入籍英國：歸化或登記"), "£1,000 – £2,500"),
        (L("Skilled Worker visa", "技術工作簽證"), "£1,200 – £2,800"),
        (L("Sponsor licence for employers", "僱主擔保牌照"), "£4,500 – £8,500"),
        (L("Investor, innovator and start-up visas", "投資者、創新者及初創簽證"), "£8,800 – £15,000"),
        (L("Overseas business representative visa", "海外企業代表簽證"), "£8,800 – £15,000"),
        (L("Student visa", "學生簽證"), "£800 – £1,200"),
        (L("Youth Mobility Scheme", "青年交流計劃"), "£1,000 – £1,500"),
        (L("Marriage visitor or fiancé(e) visa", "結婚訪客或未婚夫妻簽證"), "£1,200 – £2,500"),
        (L("Visitor visa (no previous refusal)", "訪客簽證（從未被拒）"), "£800 – £1,200"),
    ]


def rates():
    return [
        (L("Senior solicitor (over 10 years’ experience)", "資深律師（10 年以上經驗）"), "£450 – £600"),
        (L("Solicitor (5 to 10 years’ experience)", "律師（5 至 10 年經驗）"), "£250 – £450"),
        (L("Junior solicitor (under 5 years’ experience)", "初級律師（5 年以下經驗）"), "£200 – £250"),
        (L("Trainee solicitor or paralegal", "見習律師或律師助理"), "£150 – £180"),
    ]


def price_table(rows, head, cls=""):
    body = "".join(f"<tr><th scope=\"row\">{a}</th>{''.join(f'<td>{c}</td>' for c in rest)}</tr>" for a, *rest in rows)
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    return f'<div class="table-wrap"><table class="ptable {cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def page_head(crumb, eyebrow, h1, lede, extra=""):
    return f"""
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">{L("Home", "主頁")}</a> <span aria-hidden="true">/</span> {crumb}</p>
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>{extra}
  </div>
</section>"""


def cta_band():
    return f"""<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>{L("Start with a free 30-minute consultation.", "先來一次 30 分鐘免費諮詢。")}</h2>
      <p>{L("Tell us what is happening, in English, Cantonese or Mandarin. You are under no obligation to instruct us afterwards.",
            "用英語、廣東話或普通話告訴我們你的情況。諮詢後你無須委託本行。")}</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-light" href="contact.html#enquiry">{L("Book a consultation", "預約諮詢")} {icon("arrow")}</a>
      <a class="btn btn-outline-light" href="{WA}" target="_blank" rel="noopener">{icon("chat")} WhatsApp</a>
    </div>
  </div>
</section>"""


def contact_card():
    return f"""<aside class="hero-card" aria-label="{L("Contact details", "聯絡資料")}">
      <p class="hero-card-h">{icon("lang")} {L("Talk to us in", "可用語言")} <span lang="en">English</span> · <span lang="zh-Hant-HK">廣東話</span> · <span lang="zh-Hant">普通話</span></p>
      <ul class="hero-contacts">
        <li><a href="{TEL}"><span class="ic-wrap">{icon("phone")}</span><span><small>{L("Telephone", "電話")}</small><strong>{PHONE}</strong></span></a></li>
        <li><a href="{WA}" target="_blank" rel="noopener"><span class="ic-wrap wa">{icon("chat")}</span><span><small>WhatsApp</small><strong>{WHATSAPP}</strong></span></a></li>
        <li><a href="mailto:{EMAIL}"><span class="ic-wrap">{icon("mail")}</span><span><small>{L("Email", "電郵")}</small><strong>{EMAIL}</strong></span></a></li>
        <li><a href="{MAPS}" target="_blank" rel="noopener"><span class="ic-wrap">{icon("pin")}</span><span><small>{L("Office", "辦公室")}</small><strong>{L("Sheraton Skyline Hotel, Heathrow", "希斯路 Sheraton Skyline 酒店")}</strong></span></a></li>
      </ul>
      <p class="hero-card-foot">{icon("shield")} {L(f"SRA-regulated · SRA No. {SRA_NO}", f"受 SRA 監管 · 編號 {SRA_NO}")}</p>
    </aside>"""


# ---------------------------------------------------------------- pages
def home():
    tiles = "\n".join(
        f"""<a class="area reveal" href="services.html#{slug}">
        <span class="area-ic">{icon(ic)}</span>
        <h3>{name}</h3>
        <p>{summary}</p>
        <span class="area-price">{price}</span>
        <span class="area-more">{L("Learn more", "了解更多")} {icon("arrow")}</span>
      </a>""" for slug, ic, name, summary, items, price, _ in areas())

    glance = [
        (L("Initial consultation (30 minutes)", "初步諮詢（30 分鐘）"), L("Free", "免費")),
        (L("Certified true copy, per document", "核證副本（每份）"), "£10 + VAT"),
        (L("Statutory declaration", "法定聲明"), L("from £120 + VAT", "£120 起 + VAT")),
        (L("BN(O) visa application", "BN(O) 簽證申請"), "£1,000 – £2,000 + VAT"),
        (L("Spouse or partner visa", "配偶或伴侶簽證"), "£1,800 – £3,800 + VAT"),
        (L("Undisputed debt up to £5,000", "無爭議欠款（£5,000 以下）"), "£350 + VAT"),
    ]
    glance_rows = "".join(f"<li><span>{a}</span><strong>{b}</strong></li>" for a, b in glance)

    steps = [
        (L("Free first conversation", "免費初步諮詢"),
         L("30 minutes to understand your situation and tell you plainly what the options are.", "用 30 分鐘了解你的情況，清楚說明可行方案。")),
        (L("A fixed fee, in writing", "書面確認定額收費"),
         L("Most of our work is fixed fee. We confirm the price and what it covers in an engagement letter before we start.", "大部分服務以定額收費。開始前會以委託書列明價錢及包括的工作。")),
        (L("We prepare and handle it", "由我們準備及處理"),
         L("We gather the evidence, prepare the documents and deal with the Home Office, court or other side for you.", "我們整理證明文件、準備申請，並代你與內政部、法院或對方交涉。")),
        (L("Updates at every stage", "每個階段都有更新"),
         L("You hear from us in English or Chinese as things move, so there are no surprises.", "進度有變我們會以中文或英文通知你，不會有意外。")),
    ]
    step_html = "".join(f'<li class="reveal"><span class="step-n">{i}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(steps, 1))

    body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">{L("SRA-regulated solicitors · Est. 2016", "受 SRA 監管律師行 · 2016 年成立")}</p>
      <h1>{L("Bilingual solicitors, <em>minutes from Heathrow.</em>", "中英雙語律師，<em>就在希斯路機場旁。</em>")}</h1>
      <p class="lede">{L("Chu &amp; Company helps individuals, families and businesses with immigration, disputes, company matters, property and documents, and explains every step clearly in English, Cantonese or Mandarin.",
                       "Chu &amp; Company 為個人、家庭及企業處理移民、民事訴訟、公司、物業及文件事務，並以英語、廣東話或普通話清楚解釋每一步。")}</p>
      <div class="hero-actions">
        <a class="btn btn-primary btn-lg" href="contact.html#enquiry">{L("Book a free consultation", "預約免費諮詢")} {icon("arrow")}</a>
        <a class="btn btn-ghost btn-lg" href="services.html">{L("Our services", "服務範圍")}</a>
      </div>
      <ul class="hero-points">
        <li>{icon("check")} {L("30-minute first consultation, free", "首 30 分鐘諮詢免費")}</li>
        <li>{icon("check")} {L("Fixed fees for most work", "大部分服務定額收費")}</li>
        <li>{icon("check")} {L("We can meet at your office or home", "可到你的辦公室或府上會面")}</li>
      </ul>
    </div>
    {contact_card()}
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">{L("What we do", "服務範圍")}</p>
        <h2>{L("Six areas of law, one team that speaks your language.", "六大法律範疇，一支說你語言的團隊。")}</h2>
      </div>
      <a class="text-link" href="services.html">{L("All services", "全部服務")} {icon("arrow")}</a>
    </div>
    <div class="area-grid">
      {tiles}
    </div>
  </div>
</section>

<section class="section bno-band on-dark">
  <div class="container bno-grid">
    <div class="reveal">
      <p class="eyebrow">{L("Moving from Hong Kong", "由香港移居英國")}</p>
      <h2>{L("BN(O) visa applications for the whole family.", "全家一起申請 BN(O) 簽證。")}</h2>
      <p>{L("The BN(O) route lets British National (Overseas) status holders and their families live, work and study in the UK, and leads to settlement after five years. We check eligibility for every family member, work out the financial requirement and put the evidence together with you.",
            "BN(O) 簽證讓英國國民（海外）身份持有人及其家人在英國居住、工作及讀書，五年後可申請永久居留。我們會逐一核實每位家庭成員的資格，計算資金要求，並與你一起整理證明文件。")}</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="bno-visa.html">{L("BN(O) visa guide", "BN(O) 簽證指南")} {icon("arrow")}</a>
        <a class="btn btn-outline-light" href="contact.html?matter=immigration#enquiry">{L("Ask about your case", "查詢你的個案")}</a>
      </div>
    </div>
    <dl class="facts reveal">
      <div><dt>{L("Visa length", "簽證年期")}</dt><dd>{L("30 months or 5 years", "30 個月或 5 年")}</dd></div>
      <div><dt>{L("Settlement", "永久居留")}</dt><dd>{L("After 5 years in the UK", "在英國住滿 5 年後")}</dd></div>
      <div><dt>{L("Who can come", "可同行家人")}</dt><dd>{L("Partner, children, born-after-1997 adult children, dependent relatives", "伴侶、子女、1997 年後出生的成年子女及受供養親屬")}</dd></div>
      <div><dt>{L("Our fixed fee", "本行定額收費")}</dt><dd>£1,000 – £2,000 <small>+ VAT</small></dd></div>
    </dl>
  </div>
</section>

<section class="section">
  <div class="container how-grid">
    <div>
      <p class="eyebrow">{L("How we work", "工作方式")}</p>
      <h2>{L("Clear advice, a clear price, no nasty surprises.", "清楚的意見、清楚的價錢、沒有意外。")}</h2>
      <p class="lede">{L("Every case is handled with care, because a small detail can make a critical difference. We listen first, then give you a strategy that is in your best interests.",
                       "每個個案我們都細心處理，因為一個小細節也可能影響結果。我們先聆聽，再為你度身訂造最符合你利益的方案。")}</p>
    </div>
    <ol class="steps">{step_html}</ol>
  </div>
</section>

<section class="section section-alt">
  <div class="container glance-grid">
    <div>
      <p class="eyebrow">{L("Fees", "收費")}</p>
      <h2>{L("Prices you can see before you call.", "未致電已經知道價錢。")}</h2>
      <p>{L("Most of our services are fixed fee. These are common examples; the full list, hourly rates and what each fee includes are on our fees page.",
            "大部分服務以定額收費。以下是常見例子；完整收費、時薪及包括的工作，請參閱收費頁。")}</p>
      <a class="text-link" href="fees.html">{L("See all fees", "查看全部收費")} {icon("arrow")}</a>
    </div>
    <ul class="glance reveal">{glance_rows}</ul>
  </div>
</section>

<section class="section">
  <div class="container visit-grid">
    <div class="visit-art reveal" aria-hidden="true">{visit_svg()}</div>
    <div>
      <p class="eyebrow">{L("Visit us", "到訪本行")}</p>
      <h2>{L("At the Sheraton Skyline, on the Bath Road.", "位於 Bath Road 的 Sheraton Skyline 酒店內。")}</h2>
      <p>{L("Our office is inside the Sheraton Skyline Hotel at London Heathrow, which makes it easy to see us on the way to or from a flight. If it suits you better, we can also come to you: your office, your home or a private members’ club.",
            "本行位於倫敦希斯路機場的 Sheraton Skyline 酒店內，出入境前後順道來訪十分方便。如你較方便，我們亦可到你的辦公室、府上或私人會所會面。")}</p>
      <address class="visit-address">{"<br>".join(ADDRESS_LINES)}</address>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{MAPS}" target="_blank" rel="noopener">{icon("map")} {L("Get directions", "路線指引")}</a>
        <a class="btn btn-ghost" href="contact.html">{L("All contact details", "全部聯絡資料")}</a>
      </div>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("index.html",
                  L("Chu &amp; Company Solicitors | English and Chinese-speaking lawyers at London Heathrow",
                    "Chu &amp; Company 律師行｜倫敦希斯路中英雙語律師"),
                  L("SRA-regulated English, Cantonese and Mandarin-speaking solicitors at London Heathrow: immigration and BN(O) visas, litigation, corporate, property, criminal law and document certification.",
                    "倫敦希斯路受 SRA 監管的中英雙語律師行，以英語、廣東話及普通話處理移民及 BN(O) 簽證、民事訴訟、企業商業、物業、刑事及文件公證。"),
                  body)


def visit_svg():
    return """<svg viewBox="0 0 560 420" role="img">
  <rect width="560" height="420" rx="18" fill="#e7eff7"/>
  <path d="M0 300 L560 250" stroke="#ffffff" stroke-width="30"/>
  <path d="M0 300 L560 250" stroke="#c9d9ea" stroke-width="2" stroke-dasharray="12 10"/>
  <text x="440" y="236" font-family="Instrument Sans, sans-serif" font-size="12" font-weight="600" letter-spacing=".12em" fill="#5d7088" transform="rotate(-5 440 236)">BATH ROAD · A4</text>
  <g fill="#d6e4f1"><rect x="40" y="40" width="130" height="90" rx="6"/><rect x="390" y="40" width="130" height="120" rx="6"/><rect x="60" y="330" width="170" height="60" rx="6"/><rect x="320" y="320" width="200" height="70" rx="6"/></g>
  <g transform="translate(205 120)">
    <rect width="150" height="150" rx="6" fill="#002e5d"/>
    <g fill="#9cc5ea" opacity=".75">
      <rect x="18" y="20" width="22" height="14" rx="2"/><rect x="50" y="20" width="22" height="14" rx="2"/><rect x="82" y="20" width="22" height="14" rx="2"/><rect x="114" y="20" width="18" height="14" rx="2"/>
      <rect x="18" y="46" width="22" height="14" rx="2"/><rect x="50" y="46" width="22" height="14" rx="2"/><rect x="82" y="46" width="22" height="14" rx="2"/><rect x="114" y="46" width="18" height="14" rx="2"/>
      <rect x="18" y="72" width="22" height="14" rx="2"/><rect x="50" y="72" width="22" height="14" rx="2"/><rect x="82" y="72" width="22" height="14" rx="2"/><rect x="114" y="72" width="18" height="14" rx="2"/>
    </g>
    <rect x="56" y="104" width="38" height="46" rx="3" fill="#cfe1f2"/>
  </g>
  <g transform="translate(280 96)">
    <path d="M0 22s-17-15-17-28a17 17 0 0 1 34 0C17 7 0 22 0 22z" fill="#d1553b"/>
    <circle cy="-6" r="6.5" fill="#fff"/>
  </g>
  <g transform="translate(470 330) rotate(-35)" fill="#002e5d" opacity=".9">
    <path d="M40 9 24 0V-14a3 3 0 0 0-6 0V0L2 9v5l16-5v9l-5 3v3l8-2 8 2v-3l-5-3v-9l16 5z" transform="scale(1.4)"/>
  </g>
</svg>"""


def services():
    blocks = []
    for slug, ic, name, summary, items, price, link in areas():
        lis = "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in items)
        price_html = f'<a href="{link}">{price} {icon("arrow")}</a>' if link else f"<span>{price}</span>"
        extra = ""
        if slug == "immigration":
            promises = [
                (L("Strategy and planning", "策略及規劃"), L("We review each case to find the best visa route and give you clear, complete advice.", "我們審視每個個案，找出最合適的簽證途徑，提供清晰完整的意見。")),
                (L("Confidentiality", "保密"), L("Information about you and your income is handled strictly and kept private.", "你的個人及收入資料會受到嚴格管理及保密。")),
                (L("Meet where it suits you", "在你方便的地方會面"), L("At our office, or at your private office, home or members’ club.", "在本行辦公室，或你的私人辦公室、府上或會所。")),
                (L("Joined-up advice", "整合意見"), L("We work with your financial and tax advisers so the visa, investments and tax position fit together.", "我們與你的財務及稅務顧問合作，確保簽證、投資及稅務安排互相配合。")),
                (L("After the visa", "簽證批出之後"), L("We can keep managing the visa side of things alongside your bankers and advisers.", "我們可繼續與你的銀行及顧問一起處理簽證相關事宜。")),
                (L("Fits around your life", "配合你的生活"), L("A planned timetable so the application causes as little disruption as possible.", "有計劃的時間表，讓申請盡量不影響你的日常生活。")),
            ]
            pl = "".join(f"<li><h4>{t}</h4><p>{d}</p></li>" for t, d in promises)
            extra = f"""
        <div class="promise">
          <h3 class="promise-h">{L("What you get from our immigration team", "本行移民團隊的承諾")}</h3>
          <ul class="promise-list">{pl}</ul>
          <a class="text-link" href="bno-visa.html">{L("Read our BN(O) visa guide", "閱讀 BN(O) 簽證指南")} {icon("arrow")}</a>
        </div>"""
        if slug == "documents":
            extra = f"""
        <p class="note">{L("Bring the original documents with you. Certified copies are usually ready the same day; apostilles take around 15 working days through the FCDO Legalisation Office.",
                          "請帶同文件正本。核證副本一般即日完成；海牙認證經英國外交部認證辦公室辦理，約需 15 個工作天。")}</p>"""
        if slug == "criminal":
            extra = f"""
        <p class="note">{L(f'If you or a family member has been arrested, call <a href="{TEL}">{PHONE}</a>. This list is not exhaustive.',
                          f'如你或家人被捕，請致電 <a href="{TEL}">{PHONE}</a>。以上並非全部服務範圍。')}</p>"""
        blocks.append(f"""
    <article class="svc reveal" id="{slug}">
      <div class="svc-side">
        <span class="area-ic">{icon(ic)}</span>
        <h2>{name}</h2>
        <p>{summary}</p>
        <p class="svc-price">{price_html}</p>
        <a class="btn btn-ghost" href="contact.html?matter={slug}#enquiry">{L("Ask about this", "就此查詢")}</a>
      </div>
      <div class="svc-main">
        <ul class="ticks">{lis}</ul>{extra}
      </div>
    </article>""")
    jump = "".join(f'<a href="#{slug}">{name}</a>' for slug, _, name, *_ in areas())
    body = page_head(L("Services", "服務範圍"), L("Services", "服務範圍"),
                     L("Legal help for private clients and businesses.", "為個人及企業客戶提供法律服務。"),
                     L("Immigration, disputes, business, property, criminal matters and documents, handled by a bilingual team regulated by the SRA.",
                       "移民、訴訟、企業、物業、刑事及文件事務，由受 SRA 監管的雙語團隊處理。"),
                     f'<nav class="jump" aria-label="{L("On this page", "本頁內容")}">{jump}</nav>')
    body += f"""
<section class="section">
  <div class="container svc-list">{"".join(blocks)}
  </div>
</section>
{cta_band()}
"""
    return layout("services.html", L("Services | Chu &amp; Company Solicitors", "服務範圍｜Chu &amp; Company 律師行"),
                  L("Immigration and BN(O) visas, litigation and debt recovery, corporate and commercial, property, criminal law and document certification at London Heathrow.",
                    "移民及 BN(O) 簽證、民事訴訟及追收欠款、企業商業、物業、刑事及文件公證。"),
                  body)


def bno():
    family = [
        (L("Partner", "伴侶"), L("Spouse, civil partner, or unmarried partner who has lived with the BN(O) status holder for 2 years or more.", "配偶、民事伴侶，或與 BN(O) 身份持有人同居 2 年或以上的未婚伴侶。")),
        (L("Household child", "同住子女"), L("Children or grandchildren under 18 of the BN(O) status holder or their partner.", "BN(O) 身份持有人或其伴侶未滿 18 歲的子女或孫兒女。")),
        (L("Household member", "同住家庭成員"), L("Children aged 18 or over of the status holder or their partner, born on or after 1 July 1997, with their own partner and children who normally live with them.", "BN(O) 身份持有人或其伴侶年滿 18 歲、於 1997 年 7 月 1 日或之後出生的子女，以及與其同住的伴侶及子女。")),
        (L("Adult dependent relative", "成年受供養親屬"), L("Parents, grandparents, brothers, sisters, sons or daughters (18+) who normally live with the status holder and are exceptionally dependent on their care.", "與 BN(O) 身份持有人同住、在照顧上高度依賴對方的父母、祖父母、兄弟姊妹或成年子女（18 歲或以上）。")),
    ]
    fam = "".join(f'<div class="fam reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in family)

    elig = [
        L("You are a British National (Overseas).", "你是英國國民（海外）。"),
        L("You are 18 or older.", "你年滿 18 歲。"),
        L("Your permanent home is in Hong Kong if you apply from outside the UK; or in the UK, Channel Islands, Isle of Man or Hong Kong if you apply in the UK.", "如在英國境外申請，你的永久居所須在香港；如在英國境內申請，則須在英國、海峽群島、馬恩島或香港。"),
        L("You can show enough money to support yourself and your family for 6 months in the UK, unless you have already lived in the UK for 12 months (not on a Youth Mobility Scheme visa).", "你能證明有足夠資金支持自己及家人在英國生活 6 個月；如已在英國居住滿 12 個月（青年交流計劃簽證除外）則無須證明。"),
        L("You can provide a TB test certificate, unless you already provided one for an earlier UK visa.", "你能提供肺結核檢測證明，除非之前申請英國簽證時已提交。"),
    ]
    elig_html = "".join(f"<li>{icon('check')}<span>{e}</span></li>" for e in elig)

    funds = [(L("Single adult", "單身成人"), "£2,000"), (L("Couple with a child", "夫婦及一名子女"), "£3,100"),
             (L("Couple with 3 children", "夫婦及三名子女"), "£4,600"),
             (L("Couple with 2 parents and 2 adult children", "夫婦、兩位父母及兩名成年子女"), "£9,200")]

    faqs = [
        (L("I don’t have enough funds. Can I rely on a third party?", "我的資金不足，可以靠第三方嗎？"),
         L("Yes. You can rely on funds or support from a third party, for example a credible offer from relatives or friends in the UK to share accommodation with you, as long as it does not breach the overcrowding rules.",
           "可以。你可以依靠第三方的資金或支援，例如在英國的親友提出可信的同住安排，但不能違反居所過度擠迫的規定。")),
        (L("Can the lead applicant and family members apply separately?", "主申請人和家人可以分開申請嗎？"),
         L("A partner and children under 18 can apply later to join the status holder. A grandchild or adult dependent relative must apply together with the status holder as the same household, within 48 hours of the lead application. An adult child of a status holder (born on or after 1 July 1997) can apply independently, whether or not their parent has applied.",
           "伴侶及未滿 18 歲子女可於稍後申請與身份持有人團聚。孫兒女或成年受供養親屬必須以同一家庭身份，於主申請人遞交申請後 48 小時內一同申請。BN(O) 身份持有人於 1997 年 7 月 1 日或之後出生的成年子女，無論父母是否已申請，都可以獨立申請。")),
        (L("Can we travel to the UK separately?", "我們可以分開來英嗎？"),
         L("Children under 18 must travel with one or both parents unless they are joining parents already in the UK. Other family members can travel separately.",
           "未滿 18 歲子女須與父母其中一方或雙方同行，除非是與已在英國的父母團聚。其他家庭成員可分開來英。")),
        (L("I am already in the UK. Do I still need to show 6 months of funds?", "我已在英國，仍須證明 6 個月生活費嗎？"),
         L("Not if you have lived in the UK on another route, such as a student or work visa (but not the Youth Mobility Scheme), for 12 months before you apply.",
           "如你在申請前已以其他簽證（例如學生或工作簽證，但青年交流計劃除外）在英國居住滿 12 個月，則無須證明。")),
        (L("I can’t travel within 90 days of my vignette date. What now?", "我未能在簽證貼紙日期起 90 天內來英，怎麼辦？"),
         L("You can apply for a replacement vignette using the Home Office online form.", "你可以透過內政部網上表格申請補發簽證貼紙。")),
        (L("I don’t live in Hong Kong or the UK now. Can I still apply?", "我現時不在香港或英國居住，仍可申請嗎？"),
         L("You can apply from any country, for example while studying or working abroad, but you must show your ordinary residence is in Hong Kong. That is unlikely if you have permanent or settled status in another country.",
           "你可以在任何國家申請，例如在海外讀書或工作期間，但必須證明你的通常居所在香港。如你在其他國家擁有永久或定居身份，一般難以符合此要求。")),
        (L("Can I withdraw my application?", "我可以撤回申請嗎？"),
         L("Yes, before a decision is made. The Immigration Health Surcharge is refunded; whether the application fee is refunded depends on how far the application has progressed.",
           "可以，但須在作出決定前提出。移民健康附加費會退還；申請費能否退還則視乎申請進度。")),
        (L("My entry clearance application was refused. What can I do?", "我的入境許可申請被拒，可以怎樣做？"),
         L("There is no right of appeal against an entry clearance refusal, but if the Home Office made an error you can apply for an administrative review. The application fee is not refunded; the Immigration Health Surcharge is.",
           "入境許可被拒沒有上訴權，但如內政部出錯，你可以申請行政覆核。申請費不獲退還，但移民健康附加費會退還。")),
    ]
    faq_html = "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)

    toc = [("eligibility", L("Eligibility", "申請資格")), ("family", L("Family members", "家庭成員")),
           ("money", L("Funds", "資金要求")), ("costs", L("Costs", "費用")), ("settlement", L("Settlement", "永久居留")),
           ("faq", L("FAQs", "常見問題"))]
    toc_html = "".join(f'<a href="#{i}">{t}</a>' for i, t in toc)

    body = page_head(f'<a href="services.html">{L("Services", "服務範圍")}</a> <span aria-hidden="true">/</span> {L("BN(O) visa", "BN(O) 簽證")}',
                     L("Immigration · Hong Kong", "移民 · 香港"),
                     L("The BN(O) visa, explained.", "BN(O) 簽證全攻略。"),
                     L("The BN(O) route lets British National (Overseas) status holders and their immediate family from Hong Kong live, work and study in the UK, and leads to settlement. Here is what you need to know, and how we can help.",
                       "BN(O) 簽證讓英國國民（海外）身份持有人及其直系家人由香港移居英國，在英國居住、工作及讀書，並可申請永久居留。以下是你需要知道的重點，以及我們可以如何協助。"),
                     f'<nav class="jump" aria-label="{L("On this page", "本頁內容")}">{toc_html}</nav>')
    body += f"""
<section class="section">
  <div class="container article-grid">
    <div class="article">
      <section id="eligibility">
        <h2>{L("Who is eligible?", "誰符合資格？")}</h2>
        <p>{L("To qualify, you must show UK Visas and Immigration that:", "你須向英國簽證及移民局證明：")}</p>
        <ul class="ticks">{elig_html}</ul>
        <div class="callout">
          <h3>{L("Do I have BN(O) status?", "我有沒有 BN(O) 身份？")}</h3>
          <p>{L("BN(O) status was created on 1 July 1987 by the Hong Kong Act 1985 and the Hong Kong (British Nationality) Order 1986. If you registered as a BN(O) before 1 July 1997, or were under 18 then and were added to a parent’s passport, you can apply. If you are not sure, HM Passport Office can check.",
                "BN(O) 身份根據《1985 年香港法令》及《1986 年香港（英國國籍）令》於 1987 年 7 月 1 日設立。如你在 1997 年 7 月 1 日前已登記為 BN(O)，或當時未滿 18 歲並已加入父母的護照，即可申請。如不確定，可向英國護照辦事處查詢。")}</p>
        </div>
      </section>

      <section id="length">
        <h2>{L("How long is the visa?", "簽證有效期多長？")}</h2>
        <p>{L("You choose to apply for 30 months (2 years 6 months) or 5 years. The visa can be extended as many times as you need before you qualify for settlement.",
              "你可選擇申請 30 個月（2 年 6 個月）或 5 年。在符合永久居留資格前，簽證可以無限次續期。")}</p>
      </section>

      <section id="family">
        <h2>{L("Which family members can come with you?", "哪些家人可以一同申請？")}</h2>
        <div class="fam-grid">{fam}</div>
        <p>{L("Every dependant has to prove their relationship with the BN(O) status holder. We help you collect and check the documents for each person.",
              "每位受養人都要證明與 BN(O) 身份持有人的關係。我們會協助你為每位家庭成員收集及核對文件。")}</p>
      </section>

      <section id="money">
        <h2>{L("Meeting the financial requirement", "如何符合資金要求")}</h2>
        <p>{L("There is no fixed amount. You need to show enough to support your family for at least 6 months in the UK. The Home Office uses this formula:",
              "沒有固定金額，但你須證明有足夠資金支持家人在英國生活最少 6 個月。內政部使用以下公式：")}</p>
        <div class="formula" role="img" aria-label="A minus B is greater than or equal to C">
          <span><b>A</b><small>{L("Net income or funds available", "稅後收入或可用資金")}</small></span>
          <i>−</i>
          <span><b>B</b><small>{L("Housing costs", "住屋開支")}</small></span>
          <i>≥</i>
          <span><b>C</b><small>{L("What your household would receive on Income Support", "你的家庭可領取的入息補助金額")}</small></span>
        </div>
        <p>{L("As a guide, in addition to housing costs:", "以下金額可作參考（住屋開支以外）：")}</p>
        {price_table(funds, [L("Household", "家庭組合"), L("Guide amount", "參考金額")], "compact")}
      </section>

      <section id="costs">
        <h2>{L("What it costs", "申請費用")}</h2>
        <p>{L("There are two parts: the Home Office charges, which you pay directly when you apply, and our fee for preparing the application.",
              "費用分兩部分：申請時直接繳付給內政部的官方費用，以及本行準備申請的律師費。")}</p>
        <div class="cost-split">
          <div class="cost-card">
            <h3>{L("Home Office charges, per person", "內政部收費（每人）")}</h3>
            <ul>
              <li><span>{L("Application fee", "申請費")}</span><strong>{L("Set by the Home Office", "由內政部釐定")}</strong></li>
              <li><span>{L("Immigration Health Surcharge", "移民健康附加費")}</span><strong>{L("Per year of the visa", "按簽證年期計算")}</strong></li>
            </ul>
            <p class="small">{L(f'These change from time to time, so we confirm the current figures for your family when we quote. Check the latest on <a href="{GOV_BNO}" target="_blank" rel="noopener">GOV.UK</a>.',
                               f'官方收費不時調整，我們報價時會按你家庭的情況確認最新金額。最新資料請參閱 <a href="{GOV_BNO}" target="_blank" rel="noopener">GOV.UK</a>。')}</p>
          </div>
          <div class="cost-card accent">
            <h3>{L("Our fixed fee", "本行定額收費")}</h3>
            <p class="big">£1,000 – £2,000 <small>+ VAT</small></p>
            <p class="small">{L("For the main applicant. £500 is added for each dependant. Agreed in writing before we start.",
                               "主申請人收費，每位受養人另加 £500。開始前以書面確認。")}</p>
            <a class="text-link" href="fees.html#immigration">{L("What the fee includes", "收費包括甚麼")} {icon("arrow")}</a>
          </div>
        </div>
      </section>

      <section id="settlement">
        <h2>{L("Settlement after five years", "五年後申請永久居留")}</h2>
        <p>{L("After 5 years in the UK, BN(O) visa holders can apply for settlement (indefinite leave to remain). The earliest you can apply is 28 days before you reach 5 years. Time on these visas before switching to BN(O) also counts: Global Talent (or Tier 1 Exceptional Talent), Investor, Entrepreneur, Skilled Worker (or Tier 2 General), Minister of Religion, Sportsperson, Representative of an Overseas Business and UK Ancestry. Time on a Student or Youth Mobility Scheme visa does not.",
              "BN(O) 簽證持有人在英國住滿 5 年後，可申請永久居留（ILR），最早可於滿 5 年前 28 天遞交。轉為 BN(O) 簽證前持有以下簽證的時間亦可計算在內：全球人才（或 Tier 1 傑出人才）、投資者、企業家、技術工作（或 Tier 2 一般工作）、宗教人員、運動員、海外企業代表及英國祖裔簽證。學生簽證及青年交流計劃簽證的時間則不計算。")}</p>
        <p>{L("To qualify you need to:", "申請資格：")}</p>
        <ul class="ticks">
          <li>{icon("check")}<span>{L("meet the English requirement, with a qualification at B1 or above, or a degree taught in English (with an Ecctis statement if it was studied outside an English-speaking country);", "符合英語要求：持有 B1 或以上程度的英語資格，或以英語授課的學位（如在非英語國家修讀，須附 Ecctis 證明）；")}</span></li>
          <li>{icon("check")}<span>{L("pass the Life in the UK Test;", "通過「英國生活常識考試」；")}</span></li>
          <li>{icon("check")}<span>{L("have spent no more than 180 days outside the UK in any 12 months during the 5 years;", "在 5 年內任何 12 個月期間離開英國不超過 180 天；")}</span></li>
          <li>{icon("check")}<span>{L("not have breached immigration rules.", "沒有違反移民規定。")}</span></li>
        </ul>
        <p class="note">{L("Settlement rules are under review by the government. We will tell you if anything changes for your family.", "政府正在檢討永久居留規則，如有任何影響你家庭的改變，我們會通知你。")}</p>
      </section>

      <section id="faq">
        <h2>{L("Frequently asked questions", "常見問題")}</h2>
        <div class="faqs">{faq_html}</div>
      </section>
    </div>
    <aside class="article-side">
      <div class="side-card">
        <p class="eyebrow">{L("Talk to our immigration team", "聯絡本行移民團隊")}</p>
        <h3>{L("Not sure if your family qualifies?", "不確定家人是否符合資格？")}</h3>
        <p>{L("Book a free 30-minute consultation in Cantonese, Mandarin or English.", "預約 30 分鐘免費諮詢，可用廣東話、普通話或英語。")}</p>
        <a class="btn btn-primary" href="contact.html?matter=immigration#enquiry">{L("Book a consultation", "預約諮詢")}</a>
        <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{icon("chat")} WhatsApp</a>
        <p class="small">{L("Information on this page is general guidance, not legal advice for your case.", "本頁資料只屬一般指引，並非針對你個案的法律意見。")}</p>
      </div>
    </aside>
  </div>
</section>
{cta_band()}
"""
    return layout("bno-visa.html", L("BN(O) visa | Chu &amp; Company Solicitors", "BN(O) 簽證｜Chu &amp; Company 律師行"),
                  L("BN(O) visa guide from Cantonese-speaking solicitors: eligibility, family members, funds, costs, settlement and FAQs. Fixed fee £1,000 to £2,000 + VAT.",
                    "廣東話律師為你解說 BN(O) 簽證：申請資格、家庭成員、資金要求、費用、永久居留及常見問題。定額收費 £1,000 至 £2,000 另加增值稅。"),
                  body)


def fees():
    incl = [
        L("discussing your circumstances and confirming the right application, and any alternatives", "詳細了解你的情況，確認最合適的申請及其他選擇"),
        L("advising on the Immigration Rules and whether you meet them, and how to overcome any gaps", "就移民規則及你是否符合要求提供意見，以及如何解決不足之處"),
        L("reviewing your evidence and helping you obtain anything missing", "審閱證明文件，協助取得欠缺的文件"),
        L("preparing and submitting the application with a covering letter of legal submissions", "準備及遞交申請，並附上法律陳述信"),
        L("coordinating Home Office appointments and liaising with the Home Office", "安排內政部預約及與內政部聯絡"),
        L("advising you on the outcome and next steps", "就結果及下一步提供意見"),
    ]
    excl = [
        L("Home Office application fees, paid by you directly", "內政部申請費（由你直接繳付）"),
        L("the Immigration Health Surcharge", "移民健康附加費"),
        L("appeals if an application is refused", "申請被拒後的上訴"),
        L("disbursements such as translation, interpreters or expert reports, which we quote before incurring", "翻譯、傳譯或專家報告等代支費用（產生前會先報價）"),
    ]
    debt = [(L("Up to £5,000", "£5,000 以下"), "£350", "£420"),
            ("£5,001 – £10,000", "£450", "£540"),
            ("£10,001 – £50,000", "£650", "£780")]
    conv = [(L("Up to £500,000", "£500,000 以下"), "£1,150 – £1,350", "£1,250 – £1,450"),
            ("£500,000 – £1m", "£1,350 – £1,750", "£1,450 – £1,850"),
            ("£1m – £1.5m", "£1,750 – £2,150", "£1,850 – £2,350"),
            (L("Above £1.5m", "£1.5m 以上"), L("On request", "按要求報價"), L("On request", "按要求報價"))]
    docs = [(L("Certified true copy (per document, up to 2 pages)", "核證副本（每份文件，最多 2 頁）"), "£10"),
            (L("Apostille or legalisation (per document, plus FCDO fees)", "海牙認證或領事認證（每份文件，另加外交部費用）"), L("from £100", "£100 起")),
            (L("Statutory declaration", "法定聲明"), L("from £120", "£120 起")),
            (L("Ordinary Power of Attorney or Lasting Power of Attorney", "一般授權書或持久授權書"), L("from £180", "£180 起")),
            (L("ID1 identity verification for HM Land Registry", "土地註冊處 ID1 身份核實"), "£100"),
            (L("Witnessing documents, oaths and affirmations", "見證文件簽署、宣誓及非宗教式宣誓"), L("Ask us", "請查詢"))]
    disb = [
        (L("Search fees (depending on location)", "查冊費（視乎物業位置）"), "£350 – £500"),
        (L("Electronic money transfer, per transfer", "電子轉賬（每次）"), "£35 + VAT"),
        (L("HM Land Registry bankruptcy search, per person", "土地註冊處破產查冊（每人）"), "£2"),
        (L("HM Land Registry registration (freehold, by value)", "土地註冊處登記費（永久業權，按價值）"), "£20 – £500"),
        (L("OS1 priority search", "OS1 優先查冊"), "£3"),
        (L("ID check, per individual (companies £10 + £5 per beneficial owner)", "身份核實（每人；公司 £10，每名實益擁有人另加 £5）"), "£5 + VAT"),
    ]
    toc = [("start", L("How we charge", "收費方式")), ("immigration", L("Immigration", "移民")),
           ("documents", L("Documents", "文件公證")), ("debt", L("Debt recovery", "追收欠款")),
           ("conveyancing", L("Conveyancing", "物業轉讓")), ("rates", L("Hourly rates", "時薪"))]
    toc_html = "".join(f'<a href="#{i}">{t}</a>' for i, t in toc)
    li = lambda xs: "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in xs)

    body = page_head(L("Fees", "收費"), L("Fees", "收費資料"),
                     L("Transparent fees, agreed before we start.", "透明收費，開始前先確認。"),
                     L("We know legal bills can be worrying, so we set out costs at the outset of every matter. Most of our work is fixed fee; where it is not, we give you regular updates. All figures exclude VAT unless stated.",
                       "我們明白律師費令人擔心，所以每宗個案開始時都會先列明費用。大部分服務以定額收費；如非定額，我們會定期更新費用。除特別註明外，所有金額均不包括增值稅。"))
    body += f"""
<section class="section">
  <div class="container fees-layout">
    <nav class="toc" aria-label="{L("Fees sections", "收費項目")}">{toc_html}</nav>
    <div class="fees-main">
      <section id="start" class="fee-sec">
        <h2>{L("How we charge", "收費方式")}</h2>
        <div class="how-cards">
          <div><span class="area-ic">{icon("clock")}</span><h3>{L("First 30 minutes free", "首 30 分鐘免費")}</h3><p>{L("An initial consultation with no obligation to instruct us. Further consultations are charged at the hourly rate of the person you see.", "初步諮詢，無須委託。其後的諮詢按負責律師的時薪收費。")}</p></div>
          <div><span class="area-ic">{icon("doc")}</span><h3>{L("Engagement letter", "委託書")}</h3><p>{L("We confirm the fee, what it covers and the assumptions in writing. A retainer deposit is paid on instruction.", "我們會以書面確認收費、所包括的工作及前提。委託時須繳付按金。")}</p></div>
          <div><span class="area-ic">{icon("pound")}</span><h3>{L("Balance before submission", "遞交前付清餘額")}</h3><p>{L("For fixed fees, the balance is due before submission or conclusion. Ongoing cases receive interim bills.", "定額收費的餘額須在遞交或完成前付清。持續進行的個案會分期發出賬單。")}</p></div>
        </div>
        <p class="small">{L("Every case is different, so these are ranges for standard matters and are for reference only. Disbursements are not included unless agreed. The immigration fees below are for private individuals, not commercial clients.",
                           "每個個案都不同，以下為一般個案的收費範圍，僅供參考。除另有協議外，收費不包括代支費用。以下移民收費適用於個人客戶，不適用於商業客戶。")}</p>
      </section>

      <section id="immigration" class="fee-sec">
        <h2>{L("Immigration", "移民簽證")}</h2>
        <p>{L("Fixed fees for the main applicant. £500 is added for each dependant.", "主申請人定額收費，每位受養人另加 £500。")}</p>
        {price_table(immigration_fees(), [L("Application", "申請類別"), L("Fixed fee (excl. VAT)", "定額收費（不含增值稅）")])}
        <div class="two-col">
          <div><h3>{L("Included", "收費包括")}</h3><ul class="ticks">{li(incl)}</ul></div>
          <div><h3>{L("Not included", "收費不包括")}</h3><ul class="dashes">{"".join(f"<li>{x}</li>" for x in excl)}</ul>
            <p class="small">{L(f'See GOV.UK for <a href="{GOV_FEES}" target="_blank" rel="noopener">Home Office fees</a> and the <a href="{GOV_IHS}" target="_blank" rel="noopener">Immigration Health Surcharge</a>.',
                               f'內政部收費請參閱 GOV.UK：<a href="{GOV_FEES}" target="_blank" rel="noopener">申請費</a>及<a href="{GOV_IHS}" target="_blank" rel="noopener">移民健康附加費</a>。')}</p></div>
        </div>
        <div class="callout">
          <h3>{L("How long it takes", "所需時間")}</h3>
          <p>{L("We normally submit within 4 weeks of your instructions, and tell you early if it will take longer. We cannot control Home Office processing times. Estimates assume the evidence arrives on time, you meet the category requirements and there are no previous refusals or complications.",
                "我們一般在收到指示後 4 星期內遞交申請，如需更長時間會及早通知你。內政部的處理時間不在我們控制之內。估算以文件按時提供、你符合申請類別要求、以及沒有被拒紀錄或其他複雜情況為前提。")}</p>
        </div>
      </section>

      <section id="documents" class="fee-sec">
        <h2>{L("Documents &amp; certification", "文件宣誓及公證")}</h2>
        {price_table(docs, [L("Service", "服務"), L("Fee (excl. VAT)", "收費（不含增值稅）")])}
        <p class="small">{L("Bring the originals. Certified copies are usually returned the same day. Apostilles take around 15 working days.", "請帶同正本。核證副本一般即日交回。海牙認證約需 15 個工作天。")}</p>
      </section>

      <section id="debt" class="fee-sec">
        <h2>{L("Debt recovery", "追收欠款")}</h2>
        <p>{L("Fixed fees for an undisputed business-to-business debt up to £50,000 where the debtor pays after our letter and no court proceedings are needed.",
              "適用於企業之間、金額不超過 £50,000、沒有爭議的欠款，並在對方收到律師信後還款、無須入稟法院的情況。")}</p>
        {price_table(debt, [L("Debt value (incl. interest)", "欠款金額（包括利息）"), L("Our fee (excl. VAT)", "律師費（不含增值稅）"), L("Total (incl. VAT)", "總額（含增值稅）")])}
        <p>{L("If the debt is disputed or proceedings are issued, we agree the fee with you first, usually at our hourly rates. Court fees are set by HM Courts &amp; Tribunals Service and depend on the claim value. Undisputed matters usually take 2 to 4 weeks; if the matter goes to court, 16 to 32 weeks.",
              "如欠款有爭議或須入稟法院，我們會先與你協定收費，一般按時薪計算。法院費用由英國法院及審裁處服務署釐定，視乎申索金額而定。無爭議個案一般需時 2 至 4 星期；如須入稟法院，則約 16 至 32 星期。")}</p>
        <p class="small">{L("The VAT on our fee cannot be reclaimed from the debtor. Enforcement, such as bailiffs, is not included.", "律師費的增值稅不能向欠款人追討。強制執行（例如執達吏）不包括在內。")}</p>
      </section>

      <section id="conveyancing" class="fee-sec">
        <h2>{L("Conveyancing", "物業轉讓")}</h2>
        <p>{L("Legal fees for the sale or purchase of a freehold property with no mortgage, assuming a straightforward transaction. Leasehold adds £350.",
              "以下為沒有按揭的永久業權物業買賣律師費，以一般交易為前提。租賃業權物業另加 £350。")}</p>
        {price_table(conv, [L("Property value", "物業價值"), L("Sale", "出售"), L("Purchase", "購買")])}
        <h3>{L("Typical disbursements", "常見代支費用")}</h3>
        {price_table(disb, [L("Item", "項目"), L("Cost", "費用")], "compact")}
        <p class="small">{L("Stamp Duty Land Tax (or Land Transaction Tax in Wales) depends on the price; HMRC and the Welsh Revenue Authority have calculators. For leaseholds, notice, deed of covenant and compliance fees are set by the lease or management company.",
                           "印花稅（威爾斯為土地交易稅）視乎樓價而定，可使用英國稅務海關總署及威爾斯稅務局的計算器。租賃業權物業的通知費、契諾契約費及合規證明費，由租約或管理公司釐定。")}</p>
      </section>

      <section id="rates" class="fee-sec">
        <h2>{L("Hourly rates", "時薪")}</h2>
        <p>{L("Used for work that is not fixed fee, and for consultations after the free first session.", "適用於非定額收費的工作，以及免費首次諮詢以後的諮詢。")}</p>
        {price_table(rates(), [L("Fee earner", "負責人員"), L("Per hour (excl. VAT)", "每小時（不含增值稅）")])}
      </section>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("fees.html", L("Fees | Chu &amp; Company Solicitors", "收費｜Chu &amp; Company 律師行"),
                  L("Fixed fees for immigration, document certification, debt recovery and conveyancing, plus hourly rates. Free 30-minute initial consultation.",
                    "移民、文件公證、追收欠款及物業轉讓的定額收費及時薪。首 30 分鐘諮詢免費。"),
                  body)


def about():
    values = [
        ("shield", L("SRA-regulated", "受 SRA 監管"), L(f"A firm of solicitors authorised to practise in England and Wales since 2016. SRA No. {SRA_NO}.", f"自 2016 年起獲授權在英格蘭及威爾斯執業的律師行。SRA 編號 {SRA_NO}。")),
        ("lang", L("We speak your language", "說你的語言"), L("English, Cantonese and Mandarin, so legal terms and options are explained in the language you think in.", "英語、廣東話及普通話，以你最熟悉的語言解釋法律術語及選擇。")),
        ("check", L("Professional and ethical", "專業、遵守職業操守"), L("Careful, experienced and always acting in your best interests.", "細心、具豐富經驗，時刻以你的最佳利益為先。")),
        ("building", L("Private and commercial", "個人及商業客戶"), L("From personal visas to corporate global mobility, agency agreements and joint ventures.", "由個人簽證到企業全球人才流動、代理協議及合營協議。")),
    ]
    vals = "".join(f'<div class="value reveal"><span class="area-ic">{icon(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in values)
    steps = [
        L("Talk to the person handling your matter first. Most concerns can be put right quickly.", "請先與負責你個案的人員商討，大部分問題都能迅速解決。"),
        L("If that doesn’t resolve it, write to our firm’s manager, Mr Raymond Chu. We acknowledge your complaint within 5 working days and record it in our complaints register.", "如仍未解決，請以書面向本行經理朱先生（Mr Raymond Chu）投訴。我們會在 5 個工作天內確認收到，並記錄在投訴登記冊。"),
        L("We will give you our final response within 8 weeks.", "我們會在 8 星期內給你最終回覆。"),
        L("If you are still unhappy, you can refer the matter to the Legal Ombudsman within 6 months of our final response (and within 6 years of the problem, or 3 years of when you found out about it).", "如你仍不滿意，可在收到最終回覆後 6 個月內，向法律申訴專員（Legal Ombudsman）投訴（並須在事件發生後 6 年內，或得悉問題後 3 年內提出）。"),
    ]
    st = "".join(f"<li>{s}</li>" for s in steps)
    body = page_head(L("About us", "關於我們"), L("About us", "關於我們"),
                     L("A boutique firm that explains the law in your language.", "以你的語言解釋法律的精品律師行。"),
                     L("Chu &amp; Company is a boutique law firm providing bespoke legal advice to private and commercial clients across the country. We were established in 2016 under the rules of the Solicitors Regulation Authority, with a full licence to practise as solicitors in England and Wales.",
                       "Chu &amp; Company 是一間精品律師行，為全國各地的個人及商業客戶提供度身訂造的法律意見。本行於 2016 年按英格蘭及威爾斯律師監管局的規定成立，持有完整執照在英格蘭及威爾斯以律師行名義執業。"))
    body += f"""
<section class="section">
  <div class="container about-grid">
    <div class="prose">
      <h2>{L("Our firm", "本行簡介")}</h2>
      <p>{L("As a multilingual firm, we explain legal processes to clients whose first language is English, Cantonese or Mandarin. Over recent years our practice has grown from immigration into related work such as agency agreements and joint ventures, from personal immigration to corporate global mobility.",
            "作為多語律師行，我們能以英語、廣東話或普通話向客戶解釋法律程序。近年本行的業務由移民擴展至相關範疇，例如代理協議及合營協議，由個人移民到企業的全球人才流動方案。")}</p>
      <p>{L("We keep clients well informed so we can work together properly. We cannot remove every risk that comes with a transaction, but we can plan cost-effective measures for those risks, so there are no expectation gaps or nasty surprises.",
            "我們會讓客戶清楚掌握每個進展，方便彼此配合。我們未必能消除交易中所有固有風險，但可以為這些風險制定具成本效益的應對措施，不會有期望落差，也不會有意外。")}</p>
      <p>{L("Our dedication and attention to detail have earned us a reputation for resolving clients’ problems amicably and efficiently.",
            "憑著用心及對細節的重視，我們在妥善、高效地為客戶解決問題方面建立了良好聲譽。")}</p>
    </div>
    <div class="values">{vals}</div>
  </div>
</section>

<section class="section section-alt" id="complaints">
  <div class="container about-grid">
    <div>
      <p class="eyebrow">{L("Complaints procedure", "投訴程序")}</p>
      <h2>{L("If something goes wrong", "如服務未如理想")}</h2>
      <p>{L("We want to hear about it, and we aim to put it right.", "我們希望知道，並會盡力改善。")}</p>
    </div>
    <div>
      <ol class="numbered">{st}</ol>
      <div class="callout">
        <h3>{L("Legal Ombudsman", "法律申訴專員")}</h3>
        <p><a href="https://www.legalombudsman.org.uk" target="_blank" rel="noopener">www.legalombudsman.org.uk</a> · <a href="tel:+443005550333">0300 555 0333</a> · <a href="mailto:enquiries@legalombudsman.org.uk">enquiries@legalombudsman.org.uk</a><br>PO Box 6806, Wolverhampton WV1 9WJ</p>
        <p class="small">{L('Concerns about a solicitor’s behaviour, such as dishonesty or discrimination, can be <a href="https://www.sra.org.uk/consumers/problems/report-solicitor/" target="_blank" rel="noopener">reported to the SRA</a>.',
                           '如對律師的行為有疑慮（例如不誠實或歧視），可<a href="https://www.sra.org.uk/consumers/problems/report-solicitor/" target="_blank" rel="noopener">向 SRA 舉報</a>。')}</p>
      </div>
    </div>
  </div>
</section>
{cta_band()}
"""
    return layout("about.html", L("About us | Chu &amp; Company Solicitors", "關於我們｜Chu &amp; Company 律師行"),
                  L("Chu & Company is an SRA-regulated boutique law firm established in 2016, advising in English, Cantonese and Mandarin.",
                    "Chu & Company 是 2016 年成立、受 SRA 監管的精品律師行，提供英語、廣東話及普通話法律服務。"),
                  body)


def contact():
    options = "".join(f'<option value="{slug}">{name}</option>' for slug, _, name, *_ in areas())
    opt = L("(optional)", "（選填）")
    langs = [("English", "English"), ("Cantonese", "廣東話"), ("Mandarin", "普通話")]
    lang_opts = "".join(f'<label class="chip"><input type="radio" name="lang" value="{v}"{" checked" if i == 0 else ""}><span>{L(v, z)}</span></label>' for i, (v, z) in enumerate(langs))
    body = page_head(L("Contact", "聯絡我們"), L("Contact", "聯絡我們"),
                     L("Tell us what you need.", "告訴我們你需要甚麼。"),
                     L("Call, WhatsApp or send a few details. Your first 30-minute consultation is free, and we will tell you the next steps and the likely cost.",
                       "致電、WhatsApp 或留下資料。首 30 分鐘諮詢免費，我們會告訴你下一步及預計費用。"))
    body += f"""
<section class="section">
  <div class="container contact-grid">
    <div>
      <ul class="contact-list">
        <li><span class="ic-wrap">{icon("phone")}</span><div><small>{L("Telephone", "電話")}</small><a href="{TEL}"><strong>{PHONE}</strong></a><p>{L("From abroad", "海外致電")}: {PHONE_INTL}</p></div></li>
        <li><span class="ic-wrap wa">{icon("chat")}</span><div><small>WhatsApp</small><a href="{WA}" target="_blank" rel="noopener"><strong>{WHATSAPP}</strong></a><p>{L("Handy if you are messaging from Hong Kong or abroad.", "身在香港或海外，用 WhatsApp 聯絡最方便。")}</p></div></li>
        <li><span class="ic-wrap">{icon("mail")}</span><div><small>{L("Email", "電郵")}</small><a href="mailto:{EMAIL}"><strong>{EMAIL}</strong></a><p>{L("Fax", "傳真")}: {FAX}</p></div></li>
        <li><span class="ic-wrap">{icon("pin")}</span><div><small>{L("Office", "辦公室")}</small><strong>{", ".join(ADDRESS_LINES)}</strong><p><a href="{MAPS}" target="_blank" rel="noopener">{L("Open in Google Maps", "在 Google 地圖開啟")}</a> · {L("We can also meet at your office or home.", "亦可到你的辦公室或府上會面。")}</p></div></li>
      </ul>
      <div class="visit-art small-art" aria-hidden="true">{visit_svg()}</div>
    </div>
    <form class="form" id="enquiry-form" novalidate data-email="{EMAIL}">
      <h2 id="enquiry">{L("Book a free consultation", "預約免費諮詢")}</h2>
      <p>{L(f"This opens an email to {EMAIL} with your details filled in. Please don’t send confidential documents at this stage.",
            f"按下後會開啟一封寄往 {EMAIL} 的電郵，並已填好你的資料。此階段請勿附上機密文件。")}</p>
      <div class="field-row">
        <div class="field"><label for="name">{L("Name", "姓名")}</label><input id="name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="phone">{L("Phone or WhatsApp", "電話或 WhatsApp")} <span class="opt">{opt}</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field"><label for="email">{L("Email", "電郵")}</label><input id="email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="matter">{L("What is it about?", "查詢事項")}</label><select id="matter" name="matter">{options}<option value="other">{L("Something else", "其他")}</option></select></div>
      <fieldset class="field"><legend>{L("Preferred language", "希望使用的語言")}</legend><div class="chips">{lang_opts}</div></fieldset>
      <div class="field"><label for="message">{L("Your message", "內容")}</label><textarea id="message" name="message" required placeholder="{L("A few lines about your situation, and any deadlines.", "簡述你的情況及任何期限。")}"></textarea></div>
      <button class="btn btn-primary btn-lg" type="submit">{L("Write email", "撰寫電郵")} {icon("arrow")}</button>
      <p class="form-note">{L(f'Sending an enquiry doesn’t make you a client. We confirm terms and costs in writing before any work begins. See our <a href="{OFFICIAL}privacy-notice" target="_blank" rel="noopener">privacy notice</a>.',
                               f'提交查詢並不代表已委託本行。開始任何工作前，我們會以書面確認條款及費用。請參閱<a href="{OFFICIAL}privacy-notice" target="_blank" rel="noopener">私隱政策（英文）</a>。')}</p>
    </form>
  </div>
</section>
"""
    return layout("contact.html", L("Contact | Chu &amp; Company Solicitors", "聯絡我們｜Chu &amp; Company 律師行"),
                  L("Contact Chu & Company: Unit 1, Sheraton Skyline Hotel, Bath Road, Hayes UB3 5BP. Tel 020 8897 3366, WhatsApp 07990 667 894.",
                    "聯絡 Chu & Company：Unit 1, Sheraton Skyline Hotel, Bath Road, Hayes UB3 5BP。電話 020 8897 3366，WhatsApp 07990 667 894。"),
                  body)


if __name__ == "__main__":
    builders = {"index.html": home, "services.html": services, "bno-visa.html": bno, "fees.html": fees,
                "about.html": about, "contact.html": contact}
    for LANG, out in [("en", ROOT), ("zh", ROOT / "zh")]:
        out.mkdir(exist_ok=True)
        for name in PAGES:
            (out / name).write_text(builders[name](), encoding="utf-8")
            print("wrote", (out / name).relative_to(ROOT))
