import csv
from captions_data import CAPTIONS, BRAND, BRAND_DESC

# Generates captions.md, captions.csv and the PDF report from captions_data.py
L = [f"# 10 Social Media Captions with CTAs - {BRAND}\n",
     f"**Brand:** {BRAND} - {BRAND_DESC}\n",
     "| # | Objective | Platform | CTA |", "|---|---|---|---|"]
for c in CAPTIONS:
    L.append(f"| {c['n']} | {c['objective']} | {c['platform']} | {c['cta']} |")
L.append("")
for c in CAPTIONS:
    L += [f"---\n\n## Caption {c['n']} - {c['objective']}\n",
          f"- **Marketing objective:** {c['objective']}",
          f"- **Platform:** {c['platform']}",
          f"- **Target audience:** {c['audience']}\n",
          "**Caption:**\n",
          f"> {c['hook']}\n>\n> {c['body']}\n>\n> **{c['cta']}**\n>\n> {c['hashtags']}\n",
          f"**CTA:** {c['cta']}\n",
          f"**Why it works:** {c['why']}\n"]
open("captions.md","w").write("\n".join(L))

# captions.csv
with open("captions.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["No","Objective","Platform","Target Audience","Opening Hook","Body","CTA","Hashtags"])
    for c in CAPTIONS:
        w.writerow([c['n'],c['objective'],c['platform'],c['audience'],c['hook'],c['body'],c['cta'],c['hashtags']])

# PDF report
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from xml.sax.saxutils import escape as e

NAVY=colors.HexColor("#1B2A6B"); ORANGE=colors.HexColor("#E8711A"); LIGHT=colors.HexColor("#F2F5FC")
ss=getSampleStyleSheet()
T=ParagraphStyle("t",parent=ss["Title"],textColor=NAVY,fontSize=22,leading=27)
H=ParagraphStyle("h",parent=ss["Heading2"],textColor=NAVY,spaceBefore=10)
H3=ParagraphStyle("h3",parent=ss["Heading3"],textColor=ORANGE,spaceBefore=4,spaceAfter=4)
B=ParagraphStyle("b",parent=ss["BodyText"],fontSize=10,leading=14)
S=ParagraphStyle("s",parent=B,fontSize=8.5,leading=11)
Q=ParagraphStyle("q",parent=B,leftIndent=8,backColor=LIGHT,borderPadding=6,spaceBefore=4,spaceAfter=8)

doc=SimpleDocTemplate("Task_Report_Social_Media_Captions.pdf",pagesize=A4,
    leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=16*mm,
    title="Social Media Captions with CTAs - Task Report",author="Sadhanala Nischay Prasad")
st=[]
st+= [Paragraph("Create Social Media Captions with CTAs",T),
      Paragraph("Task Report &nbsp;|&nbsp; Sadhanala Nischay Prasad &nbsp;|&nbsp; October 2026",B),Spacer(1,10)]
st.append(Paragraph("1. Task Overview",H))
st.append(Paragraph("<b>Description:</b> Write 10 social media captions for different marketing objectives such as "
    "awareness, engagement, traffic, and lead generation.",B))
st.append(Paragraph("<b>Objective:</b> Develop conversion-focused social media copywriting skills.",B))
st.append(Paragraph("<b>Tools:</b> Google Docs (drafting and editing), Canva (post visuals).",B))
st.append(Paragraph("2. Brand Context",H))
st.append(Paragraph(f"All captions are written for <b>{BRAND}</b>, {e(BRAND_DESC)} Using one brand across all ten "
    "captions keeps the voice consistent and shows how the same brand adapts its message to each stage of the funnel.",B))
st.append(Paragraph("3. Approach",H))
st.append(Paragraph("Each caption follows a <b>Hook - Value - CTA</b> structure. The opening line names a pain point, "
    "makes a bold claim or asks a question so the reader stops scrolling. The body delivers one clear piece of value. "
    "The CTA asks for exactly one action, and that action matches the objective: follow or share for awareness, "
    "comment or vote for engagement, click for traffic, and register or fill a form for lead generation. "
    "The tone and length are adjusted per platform (short and playful on X and Stories, professional on LinkedIn).",B))
st.append(Paragraph("4. Caption Summary",H))
rows=[[Paragraph(f"<b>{h}</b>",S) for h in ["#","Objective","Platform","CTA"]]]
for c in CAPTIONS:
    rows.append([Paragraph(str(c['n']),S),Paragraph(c['objective'],S),Paragraph(e(c['platform']),S),Paragraph(e(c['cta']),S)])
t=Table(rows,colWidths=[8*mm,28*mm,38*mm,100*mm],repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),LIGHT),("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#C9D3EA")),
    ("VALIGN",(0,0),(-1,-1),"TOP")]))
st.append(t)
st.append(PageBreak())
st.append(Paragraph("5. The 10 Captions",H))
for c in CAPTIONS:
    blk=[Paragraph(f"Caption {c['n']} - {c['objective']}",H3),
         Paragraph(f"<b>Platform:</b> {e(c['platform'])}",B),
         Paragraph(f"<b>Target audience:</b> {e(c['audience'])}",B),
         Paragraph(f"<b>{e(c['hook'])}</b><br/><br/>{e(c['body'])}<br/><br/><b>{e(c['cta'])}</b><br/>"
                   f"<font color='#5A6A9A'>{e(c['hashtags'])}</font>",Q),
         Paragraph(f"<b>CTA:</b> {e(c['cta'])}",B),
         Paragraph(f"<b>Why it works:</b> {e(c['why'])}",B),Spacer(1,8)]
    st.append(KeepTogether(blk))
st.append(Paragraph("6. Key Learnings",H))
for x in ["The first line decides whether the rest is read, so it should carry the strongest idea.",
          "One caption, one CTA. Multiple asks split attention and lower conversion.",
          "The CTA must match the objective: asking for a sign-up in an awareness post feels pushy, while a lead-gen post without a clear form wastes intent.",
          "Friction reducers (\"free\", \"30-second form\", \"no sign-up\") and honest urgency (seat limits, dates) noticeably strengthen lead-generation copy.",
          "Platform norms matter: LinkedIn rewards insight and professional tone, Instagram rewards visuals and relatability, X rewards brevity and wit."]:
    st.append(Paragraph("&bull; "+e(x),B))
st.append(Paragraph("7. Conclusion",H))
st.append(Paragraph("This task produced ten platform-specific captions covering the full marketing funnel, each with a defined "
    "target audience, objective and aligned CTA. It strengthened my ability to write concise, conversion-focused copy and to "
    "choose the right call to action for each business goal.",B))
doc.build(st)
