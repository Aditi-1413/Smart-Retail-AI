def load_css():

    return """
<style>

@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root{
    --ink:#0B0E14;
    --ink-soft:#161B26;
    --porcelain:#FAF8F4;
    --brass:#B08D57;
    --brass-light:#D9BA85;
    --brass-dim:rgba(176,141,87,.35);
    --emerald:#31543F;
    --wine:#8C3B3B;
    --text:#1C1B18;
    --text-muted:#6E6A61;
    --border:rgba(11,14,20,.08);
}

/* ===========================
   GENERAL
=========================== */

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
    color:var(--text);
}

.stApp{
    background:var(--porcelain);
}

h1, h2, h3{
    font-family:'Fraunces', serif;
    font-weight:500;
}

/* ===========================
   SIDEBAR
=========================== */

[data-testid="stSidebar"]{
    background:linear-gradient(180deg, var(--ink) 0%, var(--ink-soft) 100%);
    border-right:1px solid var(--brass-dim);
}

[data-testid="stSidebar"] *{
    color:#EDE7DA !important;
}

[data-testid="stSidebar"] h1{
    font-family:'Fraunces', serif;
    letter-spacing:.5px;
}

/* ===========================
   EYEBROW LABEL
=========================== */

.eyebrow{
    font-family:'JetBrains Mono', monospace;
    font-size:12px;
    letter-spacing:3px;
    text-transform:uppercase;
    color:var(--brass);
    display:inline-block;
    margin-bottom:16px;
}

/* ===========================
   HERO
=========================== */

@keyframes riseIn{
    from{ opacity:0; transform:translateY(14px); }
    to{ opacity:1; transform:translateY(0); }
}

.hero{
    background:radial-gradient(120% 140% at 12% 0%, #1B2130 0%, var(--ink) 60%);
    padding:56px 48px;
    border-radius:6px;
    color:#F4EFE4;
    border:1px solid var(--brass-dim);
    margin-bottom:26px;
    animation:riseIn .6s ease-out;
    position:relative;
    overflow:hidden;
}

.hero::after{
    content:"";
    position:absolute;
    right:-70px;
    top:-70px;
    width:220px;
    height:220px;
    border:1px solid var(--brass-dim);
    border-radius:50%;
}

.hero h1{
    font-size:44px;
    font-weight:500;
    line-height:1.18;
    margin:0 0 16px 0;
    color:#FBF7EE;
}

.hero h1 em{
    color:var(--brass-light);
    font-style:italic;
}

.hero p{
    font-family:'Inter', sans-serif;
    font-size:17px;
    color:#C9C2B2;
    max-width:640px;
    line-height:1.65;
    margin:0 0 6px 0;
}

.hero .hero-divider{
    width:64px;
    height:2px;
    background:var(--brass);
    margin:24px 0 0 0;
}

/* ===========================
   KPI TICKER
=========================== */

.ticker{
    display:flex;
    background:var(--ink);
    border:1px solid var(--brass-dim);
    border-radius:6px;
    overflow:hidden;
    margin-bottom:6px;
}

.ticker-item{
    flex:1;
    padding:22px 20px;
    text-align:left;
    border-right:1px solid var(--brass-dim);
}

.ticker-item:last-child{
    border-right:none;
}

.tick-value{
    font-family:'JetBrains Mono', monospace;
    font-size:28px;
    font-weight:600;
    color:var(--brass-light);
    display:block;
    line-height:1;
}

.tick-label{
    font-family:'Inter', sans-serif;
    font-size:12.5px;
    letter-spacing:.6px;
    color:#A9A290;
    text-transform:uppercase;
    display:block;
    margin-top:9px;
}

/* ===========================
   CATALOGUE CARDS
=========================== */

.card{
    background:#FFFFFF;
    padding:26px;
    border-radius:6px;
    border:1px solid var(--border);
    border-left:2px solid var(--brass);
    margin-bottom:18px;
    transition:.25s ease;
}

.card:hover{
    transform:translateY(-4px);
    box-shadow:0 16px 32px rgba(11,14,20,.09);
}

.card .index-num{
    font-family:'JetBrains Mono', monospace;
    color:var(--brass);
    font-size:12.5px;
    letter-spacing:2px;
    display:block;
    margin-bottom:8px;
}

.card h3{
    font-size:21px;
    margin:0 0 8px 0;
    color:var(--text);
}

.card h2{
    font-size:26px;
    margin:0 0 8px 0;
    color:var(--text);
}

.card p{
    font-size:15px;
    color:var(--text-muted);
    line-height:1.6;
    margin:0;
}

/* ===========================
   VALUE PROPS
=========================== */

.value-strip{
    display:flex;
    gap:18px;
    margin:6px 0 30px 0;
}

.value-item{
    flex:1;
    background:#FFFFFF;
    border:1px solid var(--border);
    border-top:2px solid var(--brass);
    padding:22px;
    border-radius:6px;
}

.value-item h4{
    font-family:'Fraunces', serif;
    font-size:17px;
    margin:0 0 8px 0;
    color:var(--text);
}

.value-item p{
    font-size:13.5px;
    color:var(--text-muted);
    margin:0;
    line-height:1.55;
}

/* ===========================
   BUTTONS
=========================== */

div.stButton>button{
    background:var(--ink);
    color:var(--brass-light);
    height:52px;
    width:100%;
    border-radius:4px;
    border:1px solid var(--brass);
    font-family:'Inter', sans-serif;
    font-size:15px;
    font-weight:600;
    letter-spacing:.3px;
    transition:.2s ease;
}

div.stButton>button:hover{
    background:var(--brass);
    color:var(--ink);
    border-color:var(--brass);
    transform:scale(1.01);
}

/* ===========================
   FILE UPLOADER
=========================== */

[data-testid="stFileUploader"]{
    background:#FFFFFF;
    padding:20px;
    border-radius:6px;
    border:1px dashed var(--brass);
}

/* ===========================
   CHAT
=========================== */

[data-testid="stChatMessage"]{
    border-radius:6px;
    padding:16px;
    border:1px solid var(--border);
}

/* ===========================
   FOOTER
=========================== */

.footer{
    text-align:center;
    background:var(--ink);
    color:#A9A290;
    padding:36px 20px;
    margin-top:36px;
    border-radius:6px;
    border-top:2px solid var(--brass);
}

.footer hr{
    border-color:var(--brass-dim);
    margin-bottom:20px;
}

.footer h4{
    font-family:'Fraunces', serif;
    color:#F4EFE4;
    font-weight:500;
    letter-spacing:.5px;
    margin-bottom:10px;
}

.footer p{
    font-family:'JetBrains Mono', monospace;
    font-size:12px;
    letter-spacing:1.5px;
    text-transform:uppercase;
    color:#8A8272;
    margin:4px 0;
}

/* ===========================
   SUCCESS / ERROR
=========================== */

.success-box{
    background:#F2F6F1;
    padding:20px;
    border-radius:6px;
    border-left:3px solid var(--emerald);
}

.success-box h3{
    font-family:'Inter', sans-serif;
    font-size:13px;
    letter-spacing:1.2px;
    text-transform:uppercase;
    color:var(--emerald);
    margin:0 0 6px 0;
}

.success-box h2{
    font-family:'Fraunces', serif;
    font-size:26px;
    margin:0;
    color:var(--text);
}

.error-box{
    background:#F8F1F1;
    padding:20px;
    border-radius:6px;
    border-left:3px solid var(--wine);
}

</style>
"""