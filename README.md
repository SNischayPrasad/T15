# 📣 Social Media Captions with CTAs

> 10 conversion-focused social media captions, each mapped to a marketing objective, a target audience and a matching call-to-action.

**Author:** Sadhanala Nischay Prasad  
**Brand used:** *CodeNest Academy* — a fictional ed-tech platform that helps engineering students build real, deployable projects and become job-ready full-stack developers.

---

## 🎯 Objective
Develop conversion-focused social media copywriting skills by writing captions for different stages of the marketing funnel: **awareness, engagement, traffic and lead generation**.

## 🛠️ Tools
| Tool | Used for |
|---|---|
| Google Docs | Drafting, editing and reviewing captions |
| Canva | Designing post visuals (see `canva-design-brief.md`) |
| Python + ReportLab | Generating the task report PDF and CSV from one data file |

## 📦 Deliverables
- ✅ 10 captions
- ✅ A CTA for every caption
- ✅ Target audience for every caption
- ✅ Marketing objective for every caption

## 📊 Caption Overview

| # | Objective | Platform | CTA |
|---|---|---|---|
| 1 | Awareness | Instagram (Carousel) | Follow for one real project idea every day |
| 2 | Awareness | LinkedIn | Follow the page for weekly portfolio & hiring tips |
| 3 | Awareness | Reels / Shorts | Share with your project partner |
| 4 | Engagement | Instagram | Drop your number in the comments |
| 5 | Engagement | Story / LinkedIn Poll | Vote and comment why |
| 6 | Engagement | X (Twitter) | Reply with your first bug in 3 words |
| 7 | Traffic | Instagram (Carousel) | Tap link in bio for the full 90-day roadmap |
| 8 | Traffic | LinkedIn | Read the full article (link in comments) |
| 9 | Lead Generation | Instagram / Facebook Ad | Register for the free masterclass |
| 10 | Lead Generation | LinkedIn Lead Gen Form | Fill the 30-second form for a free resume review |

Full captions, audiences and reasoning → **[captions.md](captions.md)**

## ✍️ Copywriting Framework
Every caption follows **Hook → Value → CTA**:

1. **Hook** – a strong opening line (pain point, bold claim or question) that stops the scroll.
2. **Value** – one clear idea, tip or offer.
3. **CTA** – exactly one action, aligned with the objective:

| Objective | Desired action | CTA style |
|---|---|---|
| Awareness | Reach new people | Follow / Share |
| Engagement | Start a conversation | Comment / Vote / Reply |
| Traffic | Send people off-platform | Click link / Read more |
| Lead Generation | Capture contact details | Register / Fill form |

## 📁 Repository Structure
```
social-media-captions-ctas/
├── README.md                               # Project overview (this file)
├── captions.md                             # All 10 captions with audience, objective, CTA
├── captions.csv                            # Same captions as a content-calendar sheet
├── canva-design-brief.md                   # Visual direction for Canva creatives
├── linkedin-post.md                        # LinkedIn post used to share this project
├── Task_Report_Social_Media_Captions.pdf   # Final task report
├── captions_data.py                        # Single source of truth for caption content
└── generate_report.py                      # Builds captions.md, captions.csv and the PDF
```

## ▶️ Regenerate the files (optional)
```bash
pip install reportlab
python generate_report.py
```

## 💡 Key Learnings
- The first line decides whether the rest gets read.
- One caption = one CTA. Multiple asks split attention.
- The CTA must match the objective — a sign-up ask in an awareness post feels pushy.
- Friction reducers ("free", "30-second form", "no sign-up") and honest urgency lift lead-gen copy.
- Each platform has its own norms: LinkedIn → insight, Instagram → relatability, X → brevity.

---
⭐ If you found this useful, feel free to star the repo!
