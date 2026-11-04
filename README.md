# rcuklegal.co.uk — Chu & Company Solicitors concept redesign

A redesign of [Chu & Company Solicitors](https://www.rcuklegal.co.uk/), an SRA-regulated English and Chinese-speaking firm at the Sheraton Skyline Hotel, London Heathrow. It is plain static HTML, CSS and JS and deploys to any static host.

> **Concept only.** This redesign was made by [UX CIRCLES](https://ux-circles.com/web). It is not the official Chu & Company website.
> Every page opens with a "Concept" bar, is marked `noindex`, and `robots.txt` blocks crawlers so the concept doesn't compete with the official site in search results.
> If the firm adopts it, remove the `.concept-bar` block and the `noindex` meta tag in `_build/build.py`, rebuild, and set `robots.txt` to `Allow: /`.

## Languages

| Path   | Version |
|--------|---------|
| `/`    | English (the default, as on the current site) |
| `/zh/` | 繁體中文 (Hong Kong usage) |

The current site has an EN/ZH switch, and many of the firm's clients are Hong Kong families on the BN(O) route, so the Chinese version uses Traditional characters. It reuses the firm's own Chinese service names (移民簽證, 民事訴訟, 企業及商業法律, 文件宣誓及公證, 刑事訴訟). The firm name and the legal pages stay in English.

## Pages

| Page | Contents |
|------|----------|
| `index.html` | Hero with a contact card (phone, WhatsApp, email, office), the six practice areas with starting prices, a BN(O) feature, how we work, fees at a glance, the office and a CTA |
| `services.html` | All six areas with service lists, prices and an "Ask about this" button that pre-fills the enquiry form |
| `bno-visa.html` | BN(O) guide: eligibility, visa length, family members, the A − B ≥ C funds formula, costs, settlement, FAQs |
| `fees.html` | Everything from the old fee pages on one page: how charging works, immigration fixed fees, documents, debt recovery, conveyancing and disbursements, hourly rates |
| `about.html` | The firm, its values and the complaints procedure (Legal Ombudsman and SRA details) |
| `contact.html` | Contact details and an enquiry form that opens a pre-filled email (no backend needed), with a preferred-language choice |

On phones a fixed bar at the bottom offers Call / WhatsApp / Enquire. The privacy notice, cookie policy and legal notices link back to the official site.

## Problems with the current site that this redesign fixes

- Wix template with a newsletter pop-up, cookie banner and chat widget covering the content. Several menus have no clear purpose ("Log In", "More...").
- The immigration fee table is an image over a photo of coins, partly hidden by a pop-up. Fees are spread across four pages.
- Broken links: "Child Dependant Visa" goes to the homepage, "Global Talent Visa" goes to `/student-visa`, and the Litigation page has no content.
- The Corporate & Commercial page links to another law firm's website.
- Many typos ("Permanant", "You can proof", "How much does it costs?"), and the brand appears under several different names.
- The free 30-minute consultation, which is the firm's strongest offer, is only mentioned on the fees page.

## Content sources and things to check before launch

All text, prices and contact details come from the official site (October–November 2026). Nothing has been added that the firm doesn't publish, such as team biographies or opening hours. Points to confirm with the firm:

- **Immigration route names:** The fee table uses legacy names ("Tier 1 investor", "Tier 2 sponsorship licence", "Tier 4 student", "Tier 5 youth mobility"). They are shown with current names: investor/innovator/start-up, sponsor licence, Student, Youth Mobility Scheme. The prices are unchanged.
- **Home Office fees and IHS:** The old BN(O) page listed April 2025 Home Office figures. This redesign doesn't print government fees. It links to GOV.UK and says the firm confirms current figures when it quotes.
- **Conveyancing:** The old table jumps from "£1m–£1.5m" to "Over £2m". Here it reads "Above £1.5m: on request".
- **Court fees:** The debt recovery court fee table is replaced with a note that HMCTS sets court fees, because these change.
- **Debt recovery hourly rates:** They differ slightly from the main fees page. The main fees page rates are used throughout.
- **Spouse visa page:** It still quotes the old £18,600 minimum income, so it was not carried over. The services page lists the route without figures.
- **Address:** The cookie policy says "Shop 1"; every other page says "Unit 1". "Unit 1" is used here.
- **Blog:** It has two posts, the latest from February 2025, so it isn't part of the concept.

## Design

Navy (`#002e5d`) and the pale-blue square from the firm's wordmark, Fraunces serif headlines, Instrument Sans body text (Noto Sans / Serif TC for Chinese). The home page avoids a grid of identical cards: a photo-led hero with a "We speak English · 廣東話 · 普通話" tag, a contact strip, the six practice areas as a numbered editorial list with prices, a full-bleed Hong Kong photo for the BN(O) section, and the firm's own line "No expectation gaps or nasty surprises under our watch" set as a statement.

### Photos

The firm has no photos of its own (the current site uses Adobe Stock images licensed to the firm), so the concept uses three [Unsplash](https://unsplash.com/license) photos. They are free for commercial use and need no attribution. Each one ties to the firm's real situation:

| File | Use | Unsplash photo id |
|------|-----|-------------------|
| `assets/img/hero-wing-*.webp` | Home hero: an office at Heathrow, clients flying in | `photo-1436491865332-7a61a109cc05` |
| `assets/img/hong-kong-*.webp` | BN(O) section and BN(O) page header | `photo-1536599018102-9f803c140fc1` |
| `assets/img/terminal-*.webp` | "Visit us" and contact page | `photo-1542296332-2e4473faf563` |

Each photo comes in 900 px and 1600 px WebP versions, served with `srcset`. If the firm adopts the site, a photo of the office at the Sheraton Skyline or of the team would be a stronger hero than stock.

## Editing and building

Every page is generated by `_build/build.py`, so the header, footer, navigation and contact details are edited in one place. Text is written as `L(English, 繁體中文)`. Update both languages together:

```
python3 _build/build.py
```

Only Python 3 is needed. To preview locally:

```
python3 -m http.server 5190
```

## Structure

```
index.html, services.html, bno-visa.html, fees.html, about.html, contact.html
zh/                  the same pages in 繁體中文
assets/css/style.css
assets/js/main.js    mobile menu, header shadow, scroll reveal, fees section highlight, enquiry form
assets/img/favicon.svg
_build/build.py      page generator
```
