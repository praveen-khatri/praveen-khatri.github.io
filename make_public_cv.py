"""Create a privacy-conscious public academic CV PDF (ReportLab)."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

HERE=Path(__file__).parent
OUT=HERE/'assets/docs/Praveen_Khatri_Public_CV_2026.pdf'
OUT.parent.mkdir(exist_ok=True,parents=True)
forest=colors.HexColor('#183c30'); muted=colors.HexColor('#536b5e'); mint=colors.HexColor('#d9efb6'); pale=colors.HexColor('#e3ece4')
regular='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if Path(regular).exists():
    pdfmetrics.registerFont(TTFont('DejaVu',regular));pdfmetrics.registerFont(TTFont('DejaVu-Bold',bold));font='DejaVu';boldfont='DejaVu-Bold'
else: font='Helvetica';boldfont='Helvetica-Bold'
styles={
 'name':ParagraphStyle('Name',fontName=boldfont,fontSize=23,leading=27,textColor=forest,spaceAfter=6),
 'subtitle':ParagraphStyle('Subtitle',fontName=font,fontSize=9.5,leading=15,textColor=muted,spaceAfter=7),
 'head':ParagraphStyle('Head',fontName=boldfont,fontSize=10.1,leading=14,textColor=forest,spaceBefore=15,spaceAfter=8,keepWithNext=True),
 'body':ParagraphStyle('Body',fontName=font,fontSize=8.5,leading=13.5,textColor=colors.HexColor('#243b30'),spaceAfter=5),
 'item':ParagraphStyle('Item',fontName=font,fontSize=8.2,leading=12.5,textColor=colors.HexColor('#273a30'),spaceAfter=7),
 'meta':ParagraphStyle('Meta',fontName=font,fontSize=7.9,leading=12.3,textColor=muted,spaceAfter=5),
 'small':ParagraphStyle('Small',fontName=font,fontSize=7.35,leading=11,textColor=muted,spaceAfter=5),
}
P=lambda s,sty='body':Paragraph(s,styles[sty])
story=[]

def addsection(title):
    story.append(P(escape(title).upper(),'head'))
    hr=HRFlowable(width='100%',thickness=.7,color=pale,spaceAfter=9)
    hr.keepWithNext=True
    story.append(hr)

def entry(date,header,desc):
    display=('<b>'+escape(header)+'</b><br/>' if header else '')+desc
    t=Table([[P(escape(date),'meta'),P(display,'item')]],colWidths=[105,420],hAlign='LEFT')
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    story.append(KeepTogether([t]))

story.append(P('Praveen Khatri','name'))
story.append(P('Postdoctoral Fellow | Plant Molecular Biology &amp; Specialized Metabolism<br/>Department of Biology, University of Toronto Mississauga, Canada','subtitle'))
story.append(P('<b>Email:</b> <link href="mailto:praveen.khatri@utoronto.ca" color="#24664b">praveen.khatri@utoronto.ca</link> &nbsp;&nbsp; <b>ORCID:</b> <link href="https://orcid.org/0000-0001-6589-3450" color="#24664b">0000-0001-6589-3450</link> &nbsp;&nbsp; <b>LinkedIn:</b> <link href="https://www.linkedin.com/in/pkhatri4/" color="#24664b">pkhatri4</link>','small'))
story.append(Spacer(1,12))
story.append(P('RESEARCH PROFILE','head'))
story.append(P('Plant molecular biologist and biochemist investigating the genetic, biochemical and evolutionary basis of plant specialized metabolism. Research integrates cytochrome P450 functional assays, comparative genomics, RNA-seq, heterologous enzyme characterization and metabolite analysis. Current focus: late-stage salvinorin A biosynthesis in <i>Salvia divinorum</i>; previous work: soybean phytoalexin pathways and pathogen resistance.'))
addsection('Research appointments')
entry('2025–Present','Postdoctoral Fellow, University of Toronto Mississauga','Specialized diterpenoid biosynthesis; gene prioritization and metabolic enzyme discovery. Supervisor: Michael A. Phillips.')
entry('Oct 2024–Mar 2025','Postdoctoral Fellow, Agriculture and Agri-Food Canada / Western University','Functional characterization of plant cytochrome P450 enzymes and heterologous-expression assays.')
entry('2020–2024','PhD Research Assistant, Agriculture and Agri-Food Canada / Western University','Soybean isoflavonoid defenses; glyceollin pathway discovery; functional and comparative genomics.')
entry('2018–2019','Junior Research Fellow, National Agri-Food Biotechnology Institute (India)','Plant aquaporins, metalloid transport, comparative genomics and stress biology.')
addsection('Education')
entry('2024','PhD, Biology | Western University, Canada','Thesis: Deciphering the Role of Cytochrome P450 Monooxygenases in Resistance to <i>Phytophthora sojae</i> in Soybean.')
entry('2018','MSc, Molecular Biology and Biotechnology | Dr. Y. S. Parmar University, India','Research training in molecular biology and biotechnology.')
entry('2016','BSc (Hons), Agriculture | SKRAU, Bikaner, India','University Gold Medal.')
addsection('Selected research contributions')
story.append(P('<b>Plant-defense enzyme discovery.</b> Discovery and functional characterization of three cytochrome P450 prenyl cyclases that catalyze the final reaction of soybean glyceollin biosynthesis (<i>Molecular Plant</i>, 2025).'))
story.append(P('<b>Isoflavone chemistry.</b> Characterization of CYP81E substrate and regioselectivity and resulting isoflavonoid diversity (bioRxiv preprint, 2026; peer review not completed).'))
story.append(P('<b>Natural-product biosynthesis.</b> Candidate discovery and biochemical strategies for previously unresolved salvinorin tailoring steps (ongoing research).'))
story.append(P('<b>Plant–microbe systems.</b> Time-resolved transcriptomics and pathway analysis in soybean roots challenged with <i>Phytophthora sojae</i> (ongoing analysis).'))
addsection('Selected publications and research outputs')
pubs=[
 ('2026 | Accepted review','Khatri, P. and Dhaubhadel, S. Biosynthetic architecture of glyceollins reveals central roles for cytochrome P450 monooxygenases in soybean defense. <i>Phytochemistry Reviews</i>. Accepted; not yet published.'),
 ('2026 | Preprint','Khatri, P., McDowell, T., Marsolais, F., Renaud, J. and Dhaubhadel, S. Multi-Substrate Specificity of Isoflavone Hydroxylases (GmIFH) Drive Isoflavonoid Diversification in Soybean. <i>bioRxiv</i>. DOI: 10.64898/2026.05.05.722824.'),
 ('2025 | Research article','Khatri, P., Kuflu, K., McDowell, T., Lin, J., Kovinich, N. and Dhaubhadel, S. Discovery of three cytochrome P450 monooxygenase prenyl cyclases that catalyze the final step of glyceollin biosynthesis in soybean. <i>Molecular Plant</i> 18:721–724. DOI: 10.1016/j.molp.2025.01.022.'),
 ('2023 | Research article','Khatri, P., Chen, L., Rajcan, I. and Dhaubhadel, S. Functional characterization of cinnamate 4-hydroxylase gene family in soybean (<i>Glycine max</i>). <i>PLOS ONE</i> 18:e0285698. DOI: 10.1371/journal.pone.0285698.'),
 ('2022 | Research article','Khatri, P., Wally, O., Rajcan, I. and Dhaubhadel, S. Comprehensive analysis of cytochrome P450 monooxygenases reveals insight into their role in partial resistance against <i>Phytophthora sojae</i> in soybean. <i>Frontiers in Plant Science</i> 13:862314. DOI: 10.3389/fpls.2022.862314.'),
 ('2022 | Coauthored','Mandlik, R., Singla, P., Kumawat, S., Khatri, P. et al. Understanding aquaporin regulation defining silicon uptake and role in arsenic, antimony, and germanium stress in pigeonpea. <i>Environmental Pollution</i> 294:118606.'),
]
for yr,txt in pubs:entry(yr,'',txt)
story.append(P('Additional peer-reviewed studies in <i>Journal of Hazardous Materials</i>, <i>Journal of Biotechnology</i>, <i>Plants</i>, <i>Physiologia Plantarum</i> and <i>Biology</i>. Full list: personal website / Google Scholar.','small'))
addsection('Selected honors & funding')
for d,t,desc in [
('2026','Postdoctoral Competitive Research Award','University of Toronto; CAD 30,000 support for an independent postdoctoral research program.'),
('2026','Exceptional Young Member Contribution Award','Phytochemical Society of North America.'),
('2026','Postdoctoral Leadership Recognition Prize','University of Toronto Mississauga.'),
('2025–2027','Postdoctoral Fellowship Award','University of Toronto Mississauga.'),
('2024','Chunfang Hu Graduate Prize','Western University; top graduate thesis in Biology (plant-science preference).'),
('2024','Best Poster Award','Phytochemical Society of North America Annual Meeting.'),
('2022–2023','Ontario Graduate Scholarship / QEII-GS','Merit-based doctoral scholarship.')]:entry(d,t,escape(desc))
addsection('Academic service and science communication')
for d,t,desc in [
('2026','Assistant Features Editor, Plant Physiology','Scientific News &amp; Views writing; five commentaries documented in 2026.'),
('2025–2026','Research Topic Editor, Frontiers in Plant Science','Discovery, Function, and Innovation in Plant Specialized Metabolism.'),
('Current','Webmaster, Phytochemical Society of North America','Scientific communications and society website.'),
('2024–2025','Chair, PSNA Young Members Committee','Early-career scientist events, engagement and community service.'),
('2025–2026','Guest lectures and mentoring','Medicinal plant chemistry; mass spectrometry for biological systems; student mentoring.')]:entry(d,t,desc)
addsection('Selected presentations')
for d,t,desc in [
('2026','Plant Biology 2026, Ottawa','Poster: Candidate tailoring enzymes for late-stage salvinorin A biosynthesis.'),
('2026','PSNA Annual Meeting, Madison','Poster: Candidate tailoring enzymes for late-stage salvinorin A biosynthesis.'),
('2024','PSNA Annual Meeting, Monterrey','Oral presentation: Decoding glyceollin biosynthesis and soybean isoflavone hydroxylases.'),
('2024','PSNA Annual Meeting, Monterrey','Best Poster: Soybean–<i>Phytophthora sojae</i> interaction: time is the winning tactic.')]:entry(d,t,desc)
addsection('Selected scientific commentaries')
for d,t,desc in [
('2026','Stolen chemistry, rewritten genes','Plant Physiology, News &amp; Views, kiag449.'),
('2026','The sweet smell of chemistry: from terpene genes to strawberry aroma','Plant Physiology, News &amp; Views, kiag345; with M. Teixeira.'),
('2026','Glycosylation and counter-glycosylation define an apple-insect chemical arms race','Plant Physiology, News &amp; Views, kiag308; with M. Teixeira.'),
('2026','The P450 EcCYP89B16 broadens the metabolic landscape of herbicide resistance in barnyardgrass','Plant Physiology, News &amp; Views, kiag192.'),
('2026','Specialized metabolism gets a MED regulator','Plant Physiology, News &amp; Views, kiag099.')]:entry(d,t,desc)
addsection('Selected expertise')
story.append(P('<b>Biochemistry:</b> Cytochrome P450s; heterologous yeast expression; substrate assays; metabolite pathway reconstruction.<br/><b>Analytical:</b> HPLC; LC–MS; GC–MS; RT-qPCR; metabolomics and chromatographic analysis.<br/><b>Computational:</b> RNA-seq; differential expression; WGCNA; phylogenomics; comparative genomics; functional annotation.'))
story.append(Spacer(1,12))
story.append(P('Public version prepared November 2026. Personal phone number, identification fields and referee information are intentionally omitted. Publication statuses should be rechecked before future distribution.','small'))

def page_canvas(canvas,doc):
    canvas.saveState()
    w,h=doc.pagesize
    canvas.setFillColor(forest);canvas.rect(0,h-7,w,7,fill=1,stroke=0)
    canvas.setStrokeColor(pale);canvas.line(42,44,w-42,44)
    canvas.setFont(font,7)
    canvas.setFillColor(muted)
    canvas.drawString(42,32,'PRAVEEN KHATRI  ·  PUBLIC ACADEMIC CV  ·  NOVEMBER 2026')
    canvas.drawRightString(w-42,32,f'{doc.page}')
    canvas.restoreState()

doc=SimpleDocTemplate(str(OUT),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=35,bottomMargin=57,title='Praveen Khatri — Public Academic CV (2026)',author='Praveen Khatri',subject='Academic research, publications, teaching and service')
doc.build(story,onFirstPage=page_canvas,onLaterPages=page_canvas)
print(OUT)
