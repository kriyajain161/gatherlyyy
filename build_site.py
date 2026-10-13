from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "public"

ROUTES = [
    {"path": "/", "title": "Gatherly — Social Experiences", "description": "Meet people naturally through welcoming, activity-led social experiences. Explore Gatherly's concept preview."},
    {"path": "/experiences/", "title": "Explore Experiences — Gatherly", "description": "Explore the activity formats Gatherly is developing, from board games and creative workshops to supper clubs and outdoor socials."},
    {"path": "/experience/board-games/", "title": "Board Game Social — Gatherly", "description": "An illustrative concept for a hosted, low-pressure board game social."},
    {"path": "/experience/creative-workshop/", "title": "Creative Workshop — Gatherly", "description": "An illustrative concept for a relaxed, beginner-friendly creative workshop."},
    {"path": "/experience/supper-club/", "title": "Supper Club — Gatherly", "description": "An illustrative concept for a shared-table supper club built around good conversation."},
    {"path": "/experience/outdoor-social/", "title": "Outdoor Social — Gatherly", "description": "An illustrative concept for a gentle group walk and easy outdoor conversation."},
    {"path": "/how-it-works/", "title": "How It Works — Gatherly", "description": "See how shared activities, clear expectations and welcoming hosts can make meeting new people feel easier."},
    {"path": "/students/", "title": "For Students — Gatherly", "description": "Low-pressure activity ideas for students, interns and recent graduates looking to meet people beyond their usual circle."},
    {"path": "/city-seekers/", "title": "For Professionals & Newcomers — Gatherly", "description": "Curated social experience ideas for young professionals, freelancers and people finding their feet in a new city."},
    {"path": "/community/", "title": "Our Community — Gatherly", "description": "The community principles Gatherly intends to build around respect, consent, clear expectations and welcoming facilitation."},
    {"path": "/about/", "title": "About Gatherly", "description": "Learn about the Gatherly concept: making it easier to connect through shared offline activities."},
    {"path": "/faq/", "title": "Frequently Asked Questions — Gatherly", "description": "Answers about solo attendance, event concepts, group fit, hosts and the current Gatherly concept preview."},
    {"path": "/partners/", "title": "Partner With Gatherly", "description": "Explore potential ways for activity hosts, venues, campuses and community groups to collaborate with Gatherly."},
]

ASSETS = {
    "hero": "/manus-storage/async-images/521ubBhoyWuNCcwRzrxc7f/image-1.webp",
    "creative": "/manus-storage/async-images/521ubBhoyWuNCcwRzrxc7f/image-2.webp",
    "supper": "/manus-storage/async-images/521ubBhoyWuNCcwRzrxc7f/image-3.webp",
    "outdoors": "/manus-storage/async-images/521ubBhoyWuNCcwRzrxc7f/image-4.webp",
}

EXPERIENCES = [
    {
        "slug": "board-games", "title": "Board Game Social", "category": "tabletop",
        "kind": "TABLETOP · CONCEPT PREVIEW", "image": ASSETS["hero"],
        "alt": "A small group of young adults talking over a casual board game at a shared table.",
        "short": "Let the game do some of the introducing, with easy rounds and room for conversation.",
        "audience": "A playful format for students and early-career adults who enjoy games or simply want an easy way into a conversation.",
        "host": "A host would welcome the group, explain the game and help people find a place at the table.",
        "flow": ["Arrive and settle in", "Pick an easy-to-learn game", "Play in small groups with time to chat"],
        "image_position": "center",
    },
    {
        "slug": "creative-workshop", "title": "Make Something Together", "category": "creative",
        "kind": "CREATIVE · CONCEPT PREVIEW", "image": ASSETS["creative"],
        "alt": "Participants sharing clay and ideas at a bright neighborhood creative workshop.",
        "short": "A hands-on workshop where trying something new is more important than getting it perfect.",
        "audience": "For curious beginners and creative regulars alike; the shared activity gives everyone something to talk about.",
        "host": "A facilitator would introduce the activity and help newcomers get comfortable with the materials.",
        "flow": ["Meet the facilitator and group", "Try a simple guided activity", "Share the process or keep creating quietly"],
        "image_position": "center",
    },
    {
        "slug": "supper-club", "title": "A Table for Good Conversation", "category": "food",
        "kind": "FOOD & CONVERSATION · CONCEPT PREVIEW", "image": ASSETS["supper"],
        "alt": "A small group sharing food and conversation around a warmly lit supper-club table.",
        "short": "A shared meal with gentle conversation prompts and a small-group feel.",
        "audience": "Designed as a more curated evening for people who like food, conversation and a little structure.",
        "host": "A host would set the tone, explain any prompts and make space for everyone to join in at their own pace.",
        "flow": ["Settle around a shared table", "Enjoy a relaxed meal", "Use optional prompts to keep conversation flowing"],
        "image_position": "center",
    },
    {
        "slug": "outdoor-social", "title": "A Walk With Good Company", "category": "outdoor",
        "kind": "OUTDOORS · CONCEPT PREVIEW", "image": ASSETS["outdoors"],
        "alt": "A small group walking together along a leafy city-park path.",
        "short": "An easy-paced outdoor meetup with fresh air, a simple route and natural conversation.",
        "audience": "A gentle format for people who prefer walking side by side rather than sitting in a room.",
        "host": "A host would welcome participants and share the route, timing and practical details in advance.",
        "flow": ["Meet at a confirmed starting point", "Walk at a conversational pace", "Pause together before wrapping up"],
        "image_position": "center",
    },
]

NAV = [
    ("/experiences/", "Explore experiences"),
    ("/how-it-works/", "How it works"),
    ("/students/", "For students"),
    ("/city-seekers/", "For professionals"),
    ("/community/", "Our community"),
]


def e(value: str) -> str:
    return html.escape(value, quote=True)


def logo() -> str:
    return '''<svg class="brand-mark" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M18.5 9.5c-6.1 0-11 4.9-11 11 0 5.7 4.3 10.4 9.8 11l3.4 6.8 4.4-8.7"/><path d="M29.5 38.5c6.1 0 11-4.9 11-11 0-5.7-4.3-10.4-9.8-11l-3.4-6.8-4.4 8.7"/><circle cx="24" cy="24" r="3.2"/></svg>'''


def shell(route: dict, body: str) -> str:
    route_path = route["path"]
    nav_links = "".join(
        f'<a href="{path}"{(" aria-current=\"page\"" if route_path == path else "")}>{e(label)}</a>'
        for path, label in NAV
    )
    title = e(route["title"])
    description = e(route["description"])
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f6f1e7">
  <meta name="description" content="{description}">
  <title>{title}</title>
  <link rel="stylesheet" href="/styles.css">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <script src="/site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="/" aria-label="Gatherly home">{logo()}<span>gatherly</span><sup>concept</sup></a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open navigation"><span></span><span></span></button>
      <nav class="site-nav" id="primary-nav" aria-label="Main navigation">{nav_links}<a class="nav-cta" href="/experiences/">See the concepts <span aria-hidden="true">↗</span></a></nav>
    </div>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div class="footer-main">
      <div class="footer-brand"><a class="brand brand--footer" href="/">{logo()}<span>gatherly</span><sup>concept</sup></a><p>Good reasons to come together.<br>Real-world connection, one shared activity at a time.</p></div>
      <div class="footer-links"><p class="footer-label">Explore</p><a href="/experiences/">Experience concepts</a><a href="/how-it-works/">How it works</a><a href="/students/">For students</a><a href="/city-seekers/">For professionals</a></div>
      <div class="footer-links"><p class="footer-label">About</p><a href="/community/">Community principles</a><a href="/about/">About Gatherly</a><a href="/faq/">FAQs</a><a href="/partners/">Partner ideas</a></div>
    </div>
    <div class="footer-note"><span>Gatherly is a provisional working name.</span><span>Experience ideas are previews. Details will be shared once confirmed.</span><span>© <span data-year>2026</span> Gatherly concept</span></div>
  </footer>
</body>
</html>'''


def eyebrow(text: str, extra: str = "") -> str:
    return f'<p class="eyebrow {extra}">{e(text)}</p>'


def button(href: str, text: str, style: str = "primary") -> str:
    arrow = '<span aria-hidden="true">↗</span>'
    return f'<a class="button button--{e(style)}" href="{e(href)}">{e(text)} {arrow}</a>'


def experience_card(item: dict, detail: bool = False) -> str:
    href = f'/experience/{item["slug"]}/'
    return f'''<article class="experience-card" data-category="{e(item["category"])}">
      <a class="experience-image" href="{href}" aria-label="Explore {e(item["title"])} concept"><img src="{e(item["image"])}" alt="{e(item["alt"])}" loading="lazy" decoding="async"><span class="image-stamp">Format<br>preview</span></a>
      <div class="experience-card__body"><p class="eyebrow">{e(item["kind"])}</p><h3><a href="{href}">{e(item["title"])}</a></h3><p>{e(item["short"])}</p><a class="text-link" href="{href}">Explore the idea <span aria-hidden="true">→</span></a></div>
    </article>'''


def preview_notice() -> str:
    return '<div class="notice notice--soft"><span class="notice-icon" aria-hidden="true">✳</span><p><strong>Concept preview.</strong> This isn’t a live event listing. Dates, venues, prices and availability will be published once confirmed.</p></div>'


def home() -> str:
    cards = "".join(experience_card(item) for item in EXPERIENCES)
    return f'''<section class="hero container">
      <div class="hero-copy">{eyebrow("A social life, with a little less small talk", "eyebrow--accent")}<h1>Come for the activity.<br><em>See who you meet.</em></h1><p class="hero-intro">Hosted, low-pressure experiences that help new people connect naturally—without needing to arrive with a group.</p><div class="button-row">{button("/experiences/", "Explore experience ideas")}{button("/how-it-works/", "How it works", "quiet")}</div><p class="hero-footnote"><span class="status-dot"></span> Early concept preview · no events open for booking</p></div>
      <div class="hero-visual"><img src="{ASSETS['hero']}" alt="Young adults sharing conversation around a casual board game at a table" fetchpriority="high"><div class="hero-caption"><span class="caption-mark" aria-hidden="true">✳</span><span>A shared activity<br>makes room for a hello.</span></div><span class="hero-orbit" aria-hidden="true"></span></div>
      <span class="hero-side-note" aria-hidden="true">A good reason<br>to come together</span>
    </section>
    <section class="intro-band"><div class="container intro-band__inner"><p class="eyebrow">Not another networking night</p><p class="intro-statement">The activity is the <em>starting point</em>.<br>Connection can happen at its own pace.</p><span class="scribble" aria-hidden="true"></span></div></section>
    <section class="section container audience-section"><div class="section-heading section-heading--split"><div>{eyebrow("Find your kind of gathering")}<h2>Different chapters.<br><em>Shared curiosity.</em></h2></div><p>Experiences should feel right for the people in the room. Choose the path that sounds most like you.</p></div><div class="audience-grid"><a class="audience-card audience-card--sage" href="/students/"><span class="audience-index">01 / CAMPUS & EARLY CAREER</span><span class="audience-doodle" aria-hidden="true">✳</span><h3>For students<br>& new grads</h3><p>Easygoing ways to meet people beyond your usual circle—through games, creative sessions and shared challenges.</p><span class="card-link">See the student path <b aria-hidden="true">↗</b></span></a><a class="audience-card audience-card--ink" href="/city-seekers/"><span class="audience-index">02 / CITY CONNECTION SEEKERS</span><span class="audience-doodle" aria-hidden="true">◌</span><h3>For professionals<br>& newcomers</h3><p>Curated social ideas for busy schedules, new neighbourhoods and life beyond the workday.</p><span class="card-link">See the city path <b aria-hidden="true">↗</b></span></a></div></section>
    <section class="section section--tint"><div class="container"><div class="section-heading section-heading--split"><div>{eyebrow("The formats we’re exploring")}<h2>Something to do.<br><em>Someone to meet.</em></h2></div><p>From games to shared tables, each idea gives the group a natural starting point. These are format previews, not scheduled events.</p></div><div class="experience-grid">{cards}</div><div class="section-end">{button("/experiences/", "Browse all format ideas", "outline")}</div></div></section>
    <section class="section container steps-section"><div class="section-heading"><div>{eyebrow("A simple shape to the experience")}<h2>Less “walk into a room.”<br><em>More “join us here.”</em></h2></div></div><div class="steps-grid"><article class="step"><span class="step-number">01</span><h3>Pick a shared activity</h3><p>Choose an idea that fits your interests, energy and kind of evening.</p></article><article class="step"><span class="step-number">02</span><h3>Arrive as you are</h3><p>A host helps the group get settled and explains what to expect.</p></article><article class="step"><span class="step-number">03</span><h3>Let the activity lead</h3><p>Take part, chat or ease in at your own pace. No forced introductions.</p></article><article class="step"><span class="step-number">04</span><h3>Reconnect by choice</h3><p>Any follow-up connection should be optional and consent-led.</p></article></div><div class="section-end">{button("/how-it-works/", "See the full approach", "quiet")}</div></section>
    <section class="solo-section"><div class="container solo-panel"><div class="solo-mark" aria-hidden="true">↗</div><div>{eyebrow("A note for first-timers", "eyebrow--light")}<h2>Coming on your own?<br><em>That’s a good way to arrive.</em></h2><p>The idea is to make the first few minutes feel less like a test. A shared activity gives everyone something to begin with.</p><a class="text-link text-link--light" href="/faq/#solo">Read the solo-attendance FAQ <span aria-hidden="true">→</span></a></div><div class="solo-sticker" aria-hidden="true">No group<br>required</div></div></section>
    <section class="section container closing-cta"><div>{eyebrow("A concept taking shape")}<h2>Find the kind of<br><em>connection you like.</em></h2><p>Start with the formats, see how the experience could work, and check back when details are confirmed.</p>{button("/experiences/", "Explore the ideas")}</div><div class="closing-doodle" aria-hidden="true"><span></span><span></span><i>✳</i></div></section>'''


def experiences_page() -> str:
    cards = "".join(experience_card(item) for item in EXPERIENCES)
    return f'''<section class="page-hero container page-hero--wide">{eyebrow("A menu of possibilities", "eyebrow--accent")}<h1>Choose a little<br><em>something to do.</em></h1><p class="page-intro">Shared games, creative experiments, good food and fresh air. These concepts show the kinds of gatherings Gatherly is exploring.</p>{preview_notice()}</section>
    <section class="section container listing-section"><div class="filter-bar" aria-label="Filter experience concepts"><span class="filter-label">Browse by feel</span><div class="filter-controls"><button class="filter-button is-active" type="button" data-filter="all" aria-pressed="true">All ideas</button><button class="filter-button" type="button" data-filter="tabletop" aria-pressed="false">Games</button><button class="filter-button" type="button" data-filter="creative" aria-pressed="false">Creative</button><button class="filter-button" type="button" data-filter="food" aria-pressed="false">Food</button><button class="filter-button" type="button" data-filter="outdoor" aria-pressed="false">Outdoors</button></div><span class="filter-count" aria-live="polite">4 format ideas</span></div><div class="experience-grid experience-grid--listing">{cards}</div><div class="listing-note"><span class="notice-icon" aria-hidden="true">✳</span><p><strong>Still taking shape.</strong> None of these is currently bookable. Dates, locations, prices, group details and availability will be shared once confirmed.</p></div></section>
    <section class="section section--paper"><div class="container small-cta"><div>{eyebrow("Wondering what to expect?")}<h2>A little structure.<br><em>Room to be yourself.</em></h2></div><div><p>Learn how a hosted activity could make arriving, joining in and meeting new people feel more natural.</p>{button("/how-it-works/", "How it could work", "outline")}</div></div></section>'''


def experience_detail(item: dict) -> str:
    steps = "".join(f'<li><span>{i:02}</span><p>{e(step)}</p></li>' for i, step in enumerate(item["flow"], 1))
    return f'''<section class="detail-hero container"><div class="detail-copy"><a class="back-link" href="/experiences/">← All experience ideas</a>{eyebrow(item["kind"], "eyebrow--accent")}<h1>{e(item["title"])}</h1><p class="page-intro">{e(item["short"])}</p>{preview_notice()}</div><div class="detail-image"><img src="{e(item["image"])}" alt="{e(item["alt"])}" fetchpriority="high"></div></section>
    <section class="section container detail-body"><div class="detail-main"><div class="prose-block">{eyebrow("The idea")}<h2>A shared focus.<br><em>An easier first hello.</em></h2><p>{e(item["audience"])}</p><p>This page describes a format Gatherly is exploring, not a confirmed event. The final activity, group size and practical information would be stated clearly before any event opened.</p></div><div class="prose-block"><h2>How the gathering could flow</h2><ol class="timeline-list">{steps}</ol></div><div class="prose-block"><h2>The host’s role</h2><p>{e(item["host"])}</p><p>Any host standards and attendee support process need to be confirmed before launch.</p></div></div><aside class="detail-aside"><div class="aside-card"><p class="eyebrow">Before anything is bookable</p><h3>Clear details first.</h3><p>Dates, venue, price, group fit, access notes, inclusions and cancellation terms will appear once confirmed.</p><div class="aside-rule"></div><p class="status-copy"><span class="status-dot"></span> Format preview · not scheduled</p></div><div class="aside-card aside-card--coral"><span class="aside-asterisk" aria-hidden="true">✳</span><h3>Attending solo should feel welcome.</h3><p>The concept is designed around a shared activity, not arriving with a ready-made group.</p></div></aside></section>
    <section class="section section--tint"><div class="container"><div class="section-heading section-heading--split"><div>{eyebrow("More ways to connect")}<h2>Another idea<br><em>might fit you.</em></h2></div><p>Browse the other activity formats currently in development.</p></div><div class="experience-grid">{''.join(experience_card(other) for other in EXPERIENCES if other["slug"] != item["slug"])}</div></div></section>'''


def how_page() -> str:
    return f'''<section class="page-hero container">{eyebrow("A little context goes a long way", "eyebrow--accent")}<h1>Know what to expect.<br><em>Then enjoy the moment.</em></h1><p class="page-intro">The Gatherly idea is simple: use an activity as a natural starting point, and let connection happen without pressure.</p>{preview_notice()}</section>
    <section class="section container how-layout"><div class="how-lead"><p class="eyebrow">The shape of a gathering</p><h2>Five small steps.<br><em>One shared reason.</em></h2><p>Every real event would have its own clear schedule, host and logistics. This is the experience model—not a promise about an event that is already scheduled.</p></div><ol class="how-steps"><li><span class="step-number">01</span><div><h3>Find an idea that fits</h3><p>Explore the activity, intended group feel, time and confirmed practical details before deciding.</p></div></li><li><span class="step-number">02</span><div><h3>Know what you’re saying yes to</h3><p>Event information should explain the format, host, access notes, price and relevant policies before booking opens.</p></div></li><li><span class="step-number">03</span><div><h3>Arrive and get welcomed</h3><p>A host should help attendees settle in, explain the flow and make the first few minutes easier.</p></div></li><li><span class="step-number">04</span><div><h3>Take part at your pace</h3><p>The shared activity gives everyone a focus. Conversation prompts can be optional, and quiet participation should be respected.</p></div></li><li><span class="step-number">05</span><div><h3>Choose whether to reconnect</h3><p>Any post-event group or introduction should be opt-in; attendee contact details should never be shared automatically.</p></div></li></ol></section>
    <section class="solo-section"><div class="container solo-panel"><div class="solo-mark" aria-hidden="true">↗</div><div>{eyebrow("You can come by yourself", "eyebrow--light")}<h2>No friend group<br><em>needed at the door.</em></h2><p>The format is intended to help people meet through doing something together. Nobody should be required to perform, overshare or be “the life of the room.”</p></div>{button("/faq/#solo", "Read first-timer FAQs", "light")}</div></section>
    <section class="section container closing-cta"><div>{eyebrow("See the possibilities")}<h2>Start with an<br><em>activity you like.</em></h2>{button("/experiences/", "Explore experience ideas")}</div></section>'''


def audience_page(kind: str) -> str:
    students = kind == "students"
    title = "For students, interns<br>& new grads" if students else "For professionals<br>& new-in-town"
    eyebrow_text = "CAMPUS EXPLORERS · AUDIENCE PATHWAY" if students else "CITY CONNECTION SEEKERS · AUDIENCE PATHWAY"
    intro = ("A wider circle can start with a shared game, a creative session or a new hobby. Gatherly is exploring relaxed formats for students, interns and recent graduates who want to meet people beyond the usual routine.") if students else ("A full work calendar doesn’t always make a city feel like yours. Gatherly is exploring curated, low-effort ways for young professionals, freelancers and newcomers to meet people beyond the workplace.")
    formats = EXPERIENCES[:2] if students else [EXPERIENCES[2], EXPERIENCES[3]]
    barriers = ("Affordability matters. Event pricing will be clear before launch; no unverified price is shown here.", "It can feel awkward to arrive alone. Formats are being designed around hosted welcomes and a shared activity.", "The experience should feel accessible to newcomers, not just hobby experts.") if students else ("Time is precious. Each live event should publish duration and schedule before booking.", "Group fit matters. Audience, group size and format should be described up front.", "A well-run plan beats another vague invite. Venue, host and inclusions will be clear once confirmed.")
    title_text = title.replace("<br>", " ")
    return f'''<section class="audience-hero container"><div class="audience-hero__copy">{eyebrow(eyebrow_text, "eyebrow--accent")}<h1>{title}</h1><p class="page-intro">{e(intro)}</p>{preview_notice()}</div><div class="audience-hero__note"><span class="audience-note-symbol" aria-hidden="true">✳</span><p>Shared interests are an easier place to begin than a room full of strangers.</p><span class="note-caption">A Gatherly idea</span></div></section>
    <section class="section section--paper"><div class="container audience-content"><div><p class="eyebrow">What matters to this group</p><h2>{"Fun first.\nComfort close behind." if students else "Good plans.\nBetter company."}</h2><p class="audience-body">{e(intro)}</p><div class="audience-points">{''.join(f'<article><span class="point-dot">✳</span><p>{e(point)}</p></article>' for point in barriers)}</div></div><aside class="audience-callout"><p class="eyebrow">A possible message</p><blockquote>{"Show up solo. Leave with stories—and maybe new friends." if students else "New city, new circle. Real conversations beyond your workday."}</blockquote><p class="callout-small">An early positioning idea, not a guaranteed event outcome.</p></aside></div></section>
    <section class="section container"><div class="section-heading section-heading--split"><div>{eyebrow("A few format ideas")}<h2>{"Try something new.\nMeet beyond your usual." if students else "A social plan that\nfits real life."}</h2></div><p>{"Board games and beginner-friendly creative sessions can create an easy shared focus." if students else "Curated small-group experiences can turn open time into a ready-made social plan."}</p></div><div class="experience-grid">{''.join(experience_card(item) for item in formats)}</div><div class="section-end">{button("/experiences/", "See every format idea", "outline")}</div></section>
    <section class="section section--ink"><div class="container small-cta small-cta--light"><div>{eyebrow("How a first visit could feel", "eyebrow--light")}<h2>Clear plan.<br><em>Friendly first hello.</em></h2></div><div><p>Learn about the intended flow, host role and consent-led follow-up.</p>{button("/how-it-works/", "See how it could work", "light")}</div></div></section>'''


def community_page() -> str:
    principles = [
        ("Clarity before arrival", "A future event page should make the format, group fit, host role, timing, venue details, price and relevant policies clear before booking."),
        ("Consent, not pressure", "Introductions, prompts, photos and follow-up should respect each attendee’s choice. Nobody should be asked to overshare."),
        ("A host who helps the room settle", "Hosts should explain the plan, make participation options clear and help the group ease into the shared activity."),
        ("Respectful conduct", "Community standards and a real way to raise concerns must be finalized and shared before any events begin."),
        ("Reconnect only by choice", "Any group chat or post-event connection should be opt-in; participants’ contact details should not be shared automatically."),
    ]
    return f'''<section class="page-hero container">{eyebrow("The community we want to build", "eyebrow--accent")}<h1>Welcoming by design.<br><em>Respectful by default.</em></h1><p class="page-intro">A good social experience needs more than a nice activity. It needs clear expectations, thoughtful facilitation and respect for each person’s boundaries.</p><div class="notice notice--caution"><span class="notice-icon" aria-hidden="true">!</span><p><strong>Planning principles, not final event policy.</strong> Host standards, reporting routes, venue practices and detailed guidelines must be confirmed and published before any event opens.</p></div></section>
    <section class="section section--paper"><div class="container principles-list">{''.join(f'<article class="principle"><span class="principle-num">{i:02}</span><div><h2>{e(head)}</h2><p>{e(copy)}</p></div><span class="principle-mark" aria-hidden="true">↗</span></article>' for i, (head, copy) in enumerate(principles, 1))}</div></section>
    <section class="section container small-cta"><div>{eyebrow("Designed to feel easy, not forced")}<h2>Shared activity.<br><em>Room for boundaries.</em></h2></div><div><p>See how Gatherly intends to shape the experience from discovery to optional follow-up.</p>{button("/how-it-works/", "How the concept works", "outline")}</div></section>'''


def about_page() -> str:
    return f'''<section class="about-hero container"><div>{eyebrow("About the concept", "eyebrow--accent")}<h1>Make meeting people<br><em>feel more natural.</em></h1><p class="page-intro">Gatherly is a working idea for hosted, offline experiences where an activity gives new people a comfortable place to begin.</p>{preview_notice()}</div><div class="about-art" aria-hidden="true"><span class="about-orbit about-orbit--one"></span><span class="about-orbit about-orbit--two"></span><span class="about-center">✳</span><span class="about-label about-label--a">shared interests</span><span class="about-label about-label--b">real life</span><span class="about-label about-label--c">new connections</span></div></section>
    <section class="section section--paper"><div class="container about-content"><div>{eyebrow("Why this idea exists")}<h2>There are events.<br><em>And there are ways in.</em></h2></div><div class="prose"><p>Meeting new people can be harder than finding something to do. Arriving alone, starting a conversation and deciding whether a group will feel comfortable are real barriers.</p><p>Gatherly’s concept is to make an activity the shared focus: play a game, try a creative skill, share a meal or take a gentle walk. Hosts can help everyone understand the flow, while attendees choose how much they take part.</p><p>The aim is a lower-pressure starting point—not a promise of instant friendship or a substitute for people’s own judgement.</p></div></div></section>
    <section class="section container values-row"><article><span>01</span><h3>Welcoming</h3><p>Make room for first-timers and solo attendees.</p></article><article><span>02</span><h3>Curious</h3><p>Use shared interests to get people started.</p></article><article><span>03</span><h3>Thoughtful</h3><p>Make the format and expectations clear.</p></article><article><span>04</span><h3>Respectful</h3><p>Keep participation and follow-up consent-led.</p></article></section>
    <section class="section container closing-cta"><div>{eyebrow("A working name, an evolving idea")}<h2>Want to help shape<br><em>what comes next?</em></h2><p>Explore potential collaborations with activity hosts, campuses, venues and community groups.</p>{button("/partners/", "Explore partner ideas")}</div></section>'''


def faq_page() -> str:
    questions = [
        ("Can I come on my own?", "That is one of the main situations this concept is designed to welcome. A shared activity and a host-led start can make the first moments easier. Actual event formats and host arrangements will be confirmed before booking opens."),
        ("Are there live events to book right now?", "No. This website is a concept preview. The activity pages are examples of formats being explored, not scheduled or bookable events."),
        ("Who are the experiences for?", "The strategy focuses on two groups: students, interns and recent graduates, and young professionals, freelancers and people new to a city. Each future event should explain its intended audience and group feel."),
        ("Will I need experience with the activity?", "The concepts are intended to be approachable, but the final activity and skill level would be stated clearly on each event page."),
        ("What does the host do?", "The intended role is to welcome attendees, explain the flow and help people get started. Specific host standards and staffing arrangements have not yet been finalized."),
        ("Where and when will gatherings happen?", "No dates or venues are confirmed. Location, timing, duration, accessibility information and arrival details will be added only after they are set."),
        ("How much will it cost?", "Pricing has not been confirmed. Any price and inclusions would be shown before a future booking opens."),
        ("How will safety concerns be handled?", "A clear conduct policy, reporting route, host responsibilities and incident-response process need to be in place and published before launch. This preview does not claim a verified safety system."),
        ("Will my contact details be shared with other attendees?", "The intended principle is opt-in follow-up, with no automatic sharing of personal contact details. A final process and privacy notice would be published before any event launches."),
        ("Can I partner or host an experience?", "The site outlines potential collaboration formats. A real contact channel and partner process have not yet been added; the partner page explains the kinds of collaborations being considered."),
    ]
    return f'''<section class="page-hero container">{eyebrow("Good questions are part of a good welcome", "eyebrow--accent")}<h1>Before you say<br><em>hello, ask away.</em></h1><p class="page-intro">A few things are still taking shape. We’ll keep the difference between an idea and a confirmed event clear.</p></section>
    <section class="section section--paper"><div class="container faq-layout"><aside class="faq-aside"><p class="eyebrow">A quick note</p><h2>This is a<br><em>concept preview.</em></h2><p>There are no bookable events or confirmed logistics on the site yet.</p><a class="text-link" href="/experiences/">See the format ideas <span aria-hidden="true">→</span></a></aside><div class="faq-list">{''.join(f'<details class="faq-item" id="{"solo" if i == 0 else "faq-"+str(i)}"><summary><span>{e(q)}</span><span class="faq-plus" aria-hidden="true">+</span></summary><div class="faq-answer"><p>{e(a)}</p></div></details>' for i, (q, a) in enumerate(questions))}</div></div></section>
    <section class="section container small-cta"><div>{eyebrow("Still curious?")}<h2>See how the<br><em>experience could flow.</em></h2></div><div><p>From choosing an activity to optional follow-up, here’s the intended shape of a gathering.</p>{button("/how-it-works/", "How it works", "outline")}</div></section>'''


def partners_page() -> str:
    partners = [
        ("Activity hosts", "Bring a beginner-friendly skill, game, walk or creative session to a small group."),
        ("Venues & neighbourhood spaces", "Offer a welcoming setting that is easy to reach and comfortable for conversation."),
        ("Campuses & student communities", "Help shape formats that work for students, interns and new graduates."),
        ("Coworking & local groups", "Explore thoughtful ways to help newcomers meet people beyond work."),
    ]
    return f'''<section class="page-hero container">{eyebrow("Good experiences are made together", "eyebrow--accent")}<h1>Bring a place,<br><em>a practice, or an idea.</em></h1><p class="page-intro">Gatherly is exploring collaborations with people who know how to make an activity feel inviting and a space feel easy to enter.</p><div class="notice notice--soft"><span class="notice-icon" aria-hidden="true">✳</span><p><strong>Early-stage expression of interest.</strong> This page explains possible partnership types. A contact channel, selection process and commercial terms have not been set up yet.</p></div></section>
    <section class="section section--paper"><div class="container partner-grid">{''.join(f'<article class="partner-card"><span class="partner-number">{i:02}</span><h2>{e(title)}</h2><p>{e(copy)}</p><span class="partner-spark" aria-hidden="true">✳</span></article>' for i, (title, copy) in enumerate(partners, 1))}</div></section>
    <section class="section container partner-standards"><div>{eyebrow("What a good fit could look like")}<h2>Welcoming matters<br><em>as much as the activity.</em></h2></div><div><p>Potential collaborators should be comfortable with clear expectations, inclusive facilitation, respectful conduct and transparent event details. Host, venue and partner standards will need to be finalized before any collaboration is announced.</p><a class="text-link" href="/community/">Read the community principles <span aria-hidden="true">→</span></a></div></section>
    <section class="section section--ink"><div class="container small-cta small-cta--light"><div>{eyebrow("Keep exploring", "eyebrow--light")}<h2>Start with the<br><em>experience itself.</em></h2></div><div><p>See the activity formats the service is currently imagining.</p>{button("/experiences/", "Explore format ideas", "light")}</div></div></section>'''


def page_content(path: str) -> str:
    if path == "/":
        return home()
    if path == "/experiences/":
        return experiences_page()
    if path == "/how-it-works/":
        return how_page()
    if path == "/students/":
        return audience_page("students")
    if path == "/city-seekers/":
        return audience_page("city")
    if path == "/community/":
        return community_page()
    if path == "/about/":
        return about_page()
    if path == "/faq/":
        return faq_page()
    if path == "/partners/":
        return partners_page()
    if path.startswith("/experience/"):
        slug = path.strip("/").split("/")[-1]
        item = next((x for x in EXPERIENCES if x["slug"] == slug), None)
        if item:
            return experience_detail(item)
    raise KeyError(path)


def build() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "manus-routes.json").write_text(json.dumps({"routes": [{"path": r["path"], "title": r["title"]} for r in ROUTES]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for route in ROUTES:
        folder = PUBLIC / route["path"].strip("/") if route["path"] != "/" else PUBLIC
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(shell(route, page_content(route["path"])), encoding="utf-8")
    print(f"Built {len(ROUTES)} static pages in {PUBLIC}")


if __name__ == "__main__":
    build()
