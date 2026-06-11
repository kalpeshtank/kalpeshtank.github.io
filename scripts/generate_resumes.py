from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "resumes"
OUT.mkdir(parents=True, exist_ok=True)

CONTACT = {
    "default": "Ahmedabad, India | +91 89055 78128 | k.p.tank.143@gmail.com | linkedin.com/in/kalpesh-tank-133654125 | github.com/kalpeshtank",
    "de": "Ahmedabad, Indien | +91 89055 78128 | k.p.tank.143@gmail.com | linkedin.com/in/kalpesh-tank-133654125 | github.com/kalpeshtank",
    "india": "Ahmedabad, India | Permanent: Surat, Gujarat, India 394130 | +91 89055 78128 | k.p.tank.143@gmail.com | linkedin.com/in/kalpesh-tank-133654125 | github.com/kalpeshtank",
}

SKILLS = {
    "Frontend": "Angular, React, Next.js, TypeScript, JavaScript, HTML5, CSS3, jQuery",
    "Backend": "Node.js, MongoDB, PHP, Laravel, CodeIgniter, REST APIs",
    "Cloud & DevOps": "AWS, EC2, DigitalOcean, GoDaddy, CI/CD, Google Cloud basics, CentOS 7, server management",
    "Tools": "Git, GitHub, Jira, Trello, Agile delivery",
    "Leadership": "Team leadership, 5+ developer teams, 6-developer team handling, mentoring, code review, technical training, delivery ownership",
}

SKILLS_DE = {
    "Frontend": "Angular, React, Next.js, TypeScript, JavaScript, HTML5, CSS3, jQuery",
    "Backend": "Node.js, MongoDB, PHP, Laravel, CodeIgniter, REST APIs",
    "Cloud & DevOps": "AWS, EC2, DigitalOcean, GoDaddy, CI/CD, Google Cloud Grundlagen, CentOS 7, Server Management",
    "Tools": "Git, GitHub, Jira, Trello, Agile Delivery",
    "Fuehrung": "Teamleitung, Teams mit 5+ Entwicklern, Betreuung eines 6-Entwickler-Teams, Mentoring, Code Reviews, technisches Training, Delivery Ownership",
}

EXPERIENCE = [
    {
        "title": "Angular Team Lead",
        "company": "Procure IT",
        "period": "Nov 2025 - Present",
        "location": "Ahmedabad, India | Remote",
        "bullets": [
            "Lead Angular engineering for Procure IT's Managed Intelligence platform, supporting SaaS, cloud, systems data, contract, expense, and supplier intelligence workflows.",
            "Build scalable frontend modules for Asset Management, Cloud FinOps, SaaS FinOps, Contract Management, Supplier Analytics, and Technology Expense Management experiences.",
            "Lead and mentor a frontend team of 5 developers, driving architecture, code quality, TypeScript standards, API integration patterns, sprint delivery, and technical reviews.",
            "Convert complex product requirements into reusable Angular components, stable workflows, and production-ready releases.",
        ],
    },
    {
        "title": "Frontend Team Lead",
        "company": "Pingtree",
        "period": "Oct 2024 - Nov 2025",
        "location": "Ahmedabad, India | Hybrid",
        "bullets": [
            "Spearheaded frontend delivery for Pingtree traffic management modules, including funnel builder, form flows, source management, lead routing, analytics, and reporting screens.",
            "Improved delivery quality through code reviews, reusable Angular UI patterns, technical training, and close collaboration with backend teams.",
            "Led and mentored a team of 5 frontend developers, assigning tasks, reviewing pull requests, removing blockers, and maintaining consistent Angular delivery standards.",
            "Owned issue resolution, UI/UX improvements, and performance-focused delivery for campaign, tracking, distribution, and monetization workflows.",
        ],
    },
    {
        "title": "Senior Angular Developer",
        "company": "Pingtree",
        "period": "Sep 2023 - Oct 2024",
        "location": "Ahmedabad, India | On-site",
        "bullets": [
            "Delivered Angular modules for Pingtree's lead generation and traffic management platform, including landing page, tracking, source, form, and distribution workflows.",
            "Built reliable API integrations and supported production issue resolution across customer-facing funnel and reporting modules.",
            "Mentored developers on Angular implementation quality, component structure, and maintainable frontend delivery.",
        ],
    },
    {
        "title": "Senior Software Engineer",
        "company": "Rysun Labs",
        "period": "Jun 2021 - Sep 2023",
        "location": "Ahmedabad, India",
        "bullets": [
            "Delivered Angular-based enterprise applications in collaboration with backend, QA, and project management teams.",
            "Handled and mentored a team of 6 developers, including junior developers and freshers, on frontend standards, REST integration, and delivery practices.",
            "Supported predictable delivery by breaking requirements into frontend tasks, debugging complex issues, and validating implementation quality.",
        ],
    },
    {
        "title": "Senior Software Engineer",
        "company": "Moon Technolabs Pvt. Ltd",
        "period": "Dec 2017 - Jun 2021",
        "location": "Ahmedabad, India",
        "bullets": [
            "Built enterprise web solutions using Angular, Laravel, CodeIgniter, JavaScript, and cloud-hosted services.",
            "Developed document management workflows similar to Google Drive, including file organization and user access flows.",
            "Contributed to SILQ project delivery for 2000+ active users and supported production/server issue resolution.",
        ],
    },
    {
        "title": "Jr. PHP Developer",
        "company": "C S Tech Solutions",
        "period": "Aug 2016 - Dec 2017",
        "location": "Surat, India",
        "bullets": [
            "Started professional development with PHP, CodeIgniter, HTML5, CSS3, JavaScript, and jQuery.",
            "Built responsive interfaces and supported backend integration for client web applications.",
        ],
    },
]

EXPERIENCE_DE = [
    {
        "title": "Angular Team Lead",
        "company": "Procure IT",
        "period": "Nov 2025 - heute",
        "location": "Ahmedabad, Indien | Remote",
        "bullets": [
            "Leite Angular-Engineering fuer Procure ITs Managed-Intelligence-Plattform mit SaaS-, Cloud-, Systemdaten-, Vertrags-, Kosten- und Supplier-Intelligence-Workflows.",
            "Erstelle skalierbare Frontend-Module fuer Asset Management, Cloud FinOps, SaaS FinOps, Contract Management, Supplier Analytics und Technology Expense Management.",
            "Leite und mentore ein Frontend-Team von 5 Entwicklern und verantworte Architektur, Codequalitaet, TypeScript-Standards, API-Integration und technische Reviews.",
            "Verbessere Lieferergebnisse durch wiederverwendbare Angular-Komponenten, stabile Workflows und produktionsreife Releases.",
        ],
    },
    {
        "title": "Frontend Team Lead",
        "company": "Pingtree",
        "period": "Okt 2024 - Nov 2025",
        "location": "Ahmedabad, Indien | Hybrid",
        "bullets": [
            "Fuehrte die Frontend-Lieferung fuer Pingtree-Traffic-Management-Module wie Funnel Builder, Form Flows, Source Management, Lead Routing, Analytics und Reporting.",
            "Verbesserte Lieferqualitaet durch Code Reviews, wiederverwendbare Angular-UI-Patterns, technisches Training und enge Zusammenarbeit mit Backend-Teams.",
            "Leitete und mentorte ein Team von 5 Frontend-Entwicklern, verteilte Aufgaben, pruefte Pull Requests, entfernte Blocker und sicherte Angular-Standards.",
            "Verantwortete Fehlerbehebung, UI/UX-Verbesserungen und performanceorientierte Lieferung fuer Kampagnen-, Tracking-, Distribution- und Monetarisierungs-Workflows.",
        ],
    },
    {
        "title": "Senior Angular Developer",
        "company": "Pingtree",
        "period": "Sep 2023 - Okt 2024",
        "location": "Ahmedabad, Indien | Vor Ort",
        "bullets": [
            "Lieferte Angular-Module fuer Pingtrees Lead-Generation- und Traffic-Management-Plattform, darunter Landing-Page-, Tracking-, Source-, Form- und Distribution-Workflows.",
            "Erstellte stabile API-Integrationen und unterstuetzte die Behebung produktiver Probleme in Funnel- und Reporting-Modulen.",
            "Mentorte Entwickler zu Angular-Qualitaet, Komponentenstruktur und wartbarer Frontend-Lieferung.",
        ],
    },
    {
        "title": "Senior Software Engineer",
        "company": "Rysun Labs",
        "period": "Jun 2021 - Sep 2023",
        "location": "Ahmedabad, Indien",
        "bullets": [
            "Lieferte Angular-basierte Enterprise-Anwendungen in Zusammenarbeit mit Backend-, QA- und Projektmanagement-Teams.",
            "Betreute und mentorte ein Team von 6 Entwicklern, darunter Junior-Entwickler und Berufseinsteiger, zu Frontend-Standards, REST-Integration und Lieferprozessen.",
            "Unterstuetzte planbare Lieferung durch Aufteilung von Anforderungen in Frontend-Aufgaben, Debugging und Qualitaetspruefung.",
        ],
    },
    {
        "title": "Senior Software Engineer",
        "company": "Moon Technolabs Pvt. Ltd",
        "period": "Dez 2017 - Jun 2021",
        "location": "Ahmedabad, Indien",
        "bullets": [
            "Entwickelte Enterprise-Webloesungen mit Angular, Laravel, CodeIgniter, JavaScript und Cloud-Services.",
            "Baute Dokumentenmanagement-Workflows aehnlich Google Drive mit Dateiorganisation und Benutzerzugriffen.",
            "Unterstuetzte die SILQ-Projektlieferung fuer 2000+ aktive Nutzer sowie produktive Server- und Softwarethemen.",
        ],
    },
    {
        "title": "Jr. PHP Developer",
        "company": "C S Tech Solutions",
        "period": "Aug 2016 - Dez 2017",
        "location": "Surat, Indien",
        "bullets": [
            "Startete die professionelle Entwicklung mit PHP, CodeIgniter, HTML5, CSS3, JavaScript und jQuery.",
            "Erstellte responsive Oberflaechen und unterstuetzte Backend-Integration fuer Kunden-Webanwendungen.",
        ],
    },
]

PROJECTS = [
    "Procure IT Managed Intelligence Platform - SaaS, cloud, systems data, contract, invoice, IT asset, resource usage, Cloud FinOps, SaaS FinOps, supplier analytics, and technology expense management workflows.",
    "Pingtree Traffic Management Platform - lead generation campaigns, funnel builder, landing pages, form flows, source tracking, media analytics, split testing, lead routing, monetization, and reporting UI.",
    "OneBooks GST - SaaS accounting/GST workflows, dashboard modules, role-based admin UI, Angular/TypeScript/REST APIs.",
    "Enterprise Angular Applications - reusable UI components, API integrations, performance improvements, delivery mentoring.",
    "Document Management System - Drive-like file workflows, access flows, search-ready structure, Angular/Laravel/CodeIgniter.",
    "SaaS Dashboard / Admin Panel - analytics, data tables, authentication-aware UI, responsive admin operations.",
]

PROJECTS_DE = [
    "Procure IT Managed-Intelligence-Plattform - SaaS-, Cloud-, Systemdaten-, Vertrags-, Rechnungs-, IT-Asset-, Nutzungs-, Cloud-FinOps-, SaaS-FinOps-, Supplier-Analytics- und Technology-Expense-Management-Workflows.",
    "Pingtree Traffic-Management-Plattform - Lead-Generation-Kampagnen, Funnel Builder, Landing Pages, Form Flows, Source Tracking, Media Analytics, Split Testing, Lead Routing, Monetarisierung und Reporting UI.",
    "OneBooks GST - SaaS-Accounting/GST-Workflows, Dashboard-Module, rollenbasierte Admin-UI, Angular/TypeScript/REST APIs.",
    "Enterprise Angular Applications - wiederverwendbare UI-Komponenten, API-Integrationen, Performance-Verbesserungen und Delivery Mentoring.",
    "Document Management System - Drive-aehnliche Datei-Workflows, Zugriffskonzepte, suchfreundliche Struktur, Angular/Laravel/CodeIgniter.",
    "SaaS Dashboard / Admin Panel - Analytics, Datentabellen, authentifizierungsbewusste UI und responsive Admin-Prozesse.",
]

EDUCATION = [
    "MCA - Master of Computer Applications, Suresh Gyan Vihar University, Rajasthan, March 2020",
    "BCA - Bachelor of Computer Applications, Veer Narmad South Gujarat University, Gujarat, March 2016",
]

EDUCATION_INDIA = EDUCATION + [
    "HSC - I.P. Savani Science School, Gujarat, March 2013",
    "SSC - Shree Abhinav Vidhyamandir, Gujarat, March 2011",
]

EDUCATION_DE = [
    "MCA - Master of Computer Applications, Suresh Gyan Vihar University, Rajasthan, Maerz 2020",
    "BCA - Bachelor of Computer Applications, Veer Narmad South Gujarat University, Gujarat, Maerz 2016",
]

AWARDS = [
    "JavaScript Intermediate - HackerRank",
    "REST API Intermediate - HackerRank",
    "Employee of the Month - Moon Technolabs, June 2018",
    "Best Newcomer - Moon Technolabs, July 2018",
    "Best Attendance and Performance - Moon Technolabs, July 2018",
]

AWARDS_DE = [
    "JavaScript Intermediate - HackerRank",
    "REST API Intermediate - HackerRank",
    "Employee of the Month - Moon Technolabs, Juni 2018",
    "Best Newcomer - Moon Technolabs, Juli 2018",
    "Best Attendance and Performance - Moon Technolabs, Juli 2018",
]

REGIONS = {
    "uk": {
        "filename": "kalpesh-tank-uk-cv.pdf",
        "title": "UK CV - Angular Team Lead / Senior Frontend Developer",
        "summary": "ATS-friendly UK CV for Angular Team Lead, Frontend Team Lead, Senior Angular Developer, and Skilled Worker sponsorship-aware roles.",
        "sections": ["Profile", "Core Skills", "Professional Experience", "Projects", "Education", "Certifications & Awards"],
    },
    "germany": {
        "filename": "kalpesh-tank-germany-cv.pdf",
        "title": "Germany CV / Lebenslauf - Angular Team Lead",
        "summary": "Strukturierter Lebenslauf fuer deutsche IT-Rollen mit klarer Chronologie, MCA-Ausbildung, Angular/TypeScript-Expertise, Teamleitung und internationaler Projekterfahrung.",
        "sections": ["Profil", "Kernkompetenzen", "Berufserfahrung", "Projekte", "Ausbildung", "Zertifikate & Auszeichnungen"],
        "language": "de",
    },
    "usa": {
        "filename": "kalpesh-tank-usa-resume.pdf",
        "title": "USA Resume - Angular Team Lead / Senior Frontend Engineer",
        "summary": "Impact-focused resume for Senior Frontend Engineer and Frontend Lead roles, emphasizing enterprise delivery, TypeScript quality, and team leadership.",
        "sections": ["Summary", "Technical Skills", "Professional Experience", "Selected Projects", "Education", "Certifications & Awards"],
    },
    "india": {
        "filename": "kalpesh-tank-india-resume.pdf",
        "title": "India Resume - Angular Team Lead / Frontend Team Lead",
        "summary": "Detailed India resume covering 10+ years in IT, MCA education, latest Procure IT role, certifications, awards, and project delivery.",
        "sections": ["Professional Summary", "Technical Skills", "Work Experience", "Project Details", "Education", "Certifications, Awards & Interests"],
        "include_interests": True,
    },
}


def clean(value):
    replacements = {
        "\\": "\\\\",
        "(": "\\(",
        ")": "\\)",
        "•": "-",
        "–": "-",
        "—": "-",
        "’": "'",
        "“": '"',
        "”": '"',
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value.encode("latin-1", "ignore").decode("latin-1")


class Pdf:
    width = 612
    height = 792
    margin = 42

    def __init__(self, title, contact):
        self.title = title
        self.contact = contact
        self.pages = []
        self.ops = []
        self.page_no = 0
        self.y = 0
        self.new_page(first=True)

    def add(self, op):
        self.ops.append(op)

    def color(self, hex_value):
        hex_value = hex_value.lstrip("#")
        return tuple(int(hex_value[i : i + 2], 16) / 255 for i in (0, 2, 4))

    def fill(self, hex_value):
        r, g, b = self.color(hex_value)
        self.add(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def stroke(self, hex_value):
        r, g, b = self.color(hex_value)
        self.add(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def rect(self, x, y, w, h, fill="#ffffff", stroke=None):
        self.add("q")
        self.fill(fill)
        if stroke:
            self.stroke(stroke)
            self.add(f"{x} {y} {w} {h} re B")
        else:
            self.add(f"{x} {y} {w} {h} re f")
        self.add("Q")

    def line(self, x1, y1, x2, y2, color="#d9e2e7", width=1):
        self.add("q")
        self.stroke(color)
        self.add(f"{width} w")
        self.add(f"{x1} {y1} m {x2} {y2} l S")
        self.add("Q")

    def text_at(self, x, y, value, size=10, bold=False, color="#111827"):
        font = "F2" if bold else "F1"
        self.add("BT")
        self.fill(color)
        self.add(f"/{font} {size} Tf")
        self.add(f"1 0 0 1 {x} {y} Tm ({clean(value)}) Tj")
        self.add("ET")

    def new_page(self, first=False):
        if self.ops:
            self.pages.append(self.ops)
        self.page_no += 1
        self.ops = []
        self.rect(0, 0, self.width, self.height, "#ffffff")
        if first:
            self.header()
            self.y = 622
        else:
            self.text_at(self.margin, 752, "Kalpesh Tank", 11, True, "#0f172a")
            self.text_at(self.margin, 736, self.title, 8.5, False, "#64748b")
            self.line(self.margin, 724, self.width - self.margin, 724, "#cbd5e1", 0.8)
            self.y = 704

    def header(self):
        self.rect(0, 674, self.width, 118, "#102a43")
        self.rect(0, 674, 148, 118, "#2f7f8d")
        self.text_at(self.margin, 742, "Kalpesh Tank", 28, True, "#ffffff")
        self.text_at(self.margin, 716, self.title, 12.5, True, "#e6f6f8")
        for line_index, line in enumerate(textwrap.wrap(self.contact, width=118)[:2]):
            self.text_at(self.margin, 694 - line_index * 13, line, 8.3, False, "#dbeafe")
        x = 316
        for label in ["10+ years", "Angular Lead", "5-6 devs led"]:
            self.rect(x, 748, 82, 18, "#eff8f9")
            self.text_at(x + 8, 754, label, 7.3, True, "#1f6f7c")
            x += 100

    def footer(self):
        for index, page in enumerate(self.pages, 1):
            self.ops = page
            self.line(self.margin, 34, self.width - self.margin, 34, "#e2e8f0", 0.7)
            self.text_at(self.margin, 20, "ATS-readable text resume | Designed for recruiter review", 7.5, False, "#64748b")
            self.text_at(self.width - 74, 20, f"Page {index}", 7.5, False, "#64748b")
            self.pages[index - 1] = self.ops
        self.ops = []

    def ensure(self, height=36):
        if self.y - height < 56:
            self.new_page()

    def section(self, title):
        self.ensure(46)
        self.y -= 10
        self.rect(self.margin, self.y - 5, 5, 17, "#2f7f8d")
        self.text_at(self.margin + 13, self.y, title.upper(), 10.5, True, "#0f172a")
        self.line(self.margin + 160, self.y + 4, self.width - self.margin, self.y + 4, "#d7e5e8", 0.8)
        self.y -= 22

    def wrapped(self, value, x=None, width=90, size=9.2, bold=False, bullet=False, color="#334155", leading=12):
        x = self.margin if x is None else x
        prefix = "- " if bullet else ""
        lines = textwrap.wrap(value, width=width) or [""]
        for index, line in enumerate(lines):
            self.ensure(leading + 6)
            text = (prefix if index == 0 else "  ") + line
            self.text_at(x, self.y, text, size, bold and index == 0, color)
            self.y -= leading
        self.y -= 3

    def profile(self, summary):
        self.section("Profile")
        self.wrapped(summary, width=104, size=10, color="#263548", leading=13)

    def skill_grid(self, skills):
        self.section("Core Skills")
        left = self.margin
        right = self.margin + 266
        box_w = 250
        box_h = 72
        items = list(skills.items())
        for index, (group, value) in enumerate(items):
            x = left if index % 2 == 0 else right
            if index % 2 == 0:
                self.ensure(box_h + 16)
                row_y = self.y
            y = row_y - box_h + 10
            self.rect(x, y, box_w, box_h, "#f7fbfc", "#d6e7eb")
            self.text_at(x + 12, row_y - 10, group, 9.5, True, "#1f6f7c")
            for line_index, line in enumerate(textwrap.wrap(value, width=42)[:4]):
                self.text_at(x + 12, row_y - 24 - line_index * 11, line, 8.2, False, "#334155")
            if index % 2 == 1 or index == len(items) - 1:
                self.y = y - 12

    def experience(self, jobs, title):
        self.section(title)
        for job in jobs:
            self.ensure(92)
            self.text_at(self.margin, self.y, f"{job['title']} | {job['company']}", 11, True, "#17324d")
            self.text_at(self.margin, self.y - 14, f"{job['period']} | {job['location']}", 8.8, False, "#64748b")
            self.y -= 32
            for bullet in job["bullets"]:
                self.wrapped(bullet, x=self.margin + 10, width=96, size=8.8, bullet=True, color="#334155", leading=11.3)
            self.y -= 5

    def list_section(self, title, items, width=100):
        self.section(title)
        for item in items:
            self.wrapped(item, x=self.margin + 10, width=width, size=8.9, bullet=True, color="#334155", leading=11.6)

    def save(self, path):
        if self.ops:
            self.pages.append(self.ops)
            self.ops = []
        self.footer()

        objects = [
            "<< /Type /Catalog /Pages 2 0 R >>",
            f"<< /Type /Pages /Kids [{' '.join(f'{3 + i * 2} 0 R' for i in range(len(self.pages)))}] /Count {len(self.pages)} >>",
        ]

        for i, page in enumerate(self.pages):
            content_id = 4 + i * 2
            objects.append(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                f"/Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> "
                f"/F2 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> >> >> "
                f"/Contents {content_id} 0 R >>"
            )
            stream = "\n".join(page)
            objects.append(f"<< /Length {len(stream.encode('latin-1'))} >>\nstream\n{stream}\nendstream")

        body = ["%PDF-1.4\n"]
        offsets = [0]
        for idx, obj in enumerate(objects, start=1):
            offsets.append(sum(len(part.encode("latin-1")) for part in body))
            body.append(f"{idx} 0 obj\n{obj}\nendobj\n")
        xref = sum(len(part.encode("latin-1")) for part in body)
        body.append(f"xref\n0 {len(objects)+1}\n0000000000 65535 f\n")
        for offset in offsets[1:]:
            body.append(f"{offset:010d} 00000 n\n")
        body.append(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF")
        path.write_bytes("".join(body).encode("latin-1"))


def build_resume(key, config):
    is_german = config.get("language") == "de"
    contact = CONTACT["de"] if is_german else CONTACT["india"] if key == "india" else CONTACT["default"]
    skills = SKILLS_DE if is_german else SKILLS
    experience = EXPERIENCE_DE if is_german else EXPERIENCE
    projects = PROJECTS_DE if is_german else PROJECTS
    education = EDUCATION_DE if is_german else EDUCATION_INDIA if key == "india" else EDUCATION
    awards = AWARDS_DE if is_german else AWARDS

    section_profile, section_skills, section_exp, section_projects, section_edu, section_awards = config["sections"]
    pdf = Pdf(config["title"], contact)
    pdf.profile(config["summary"])
    pdf.skill_grid(skills)
    pdf.experience(experience, section_exp)
    pdf.list_section(section_projects, projects, width=98)
    pdf.list_section(section_edu, education, width=98)
    if config.get("include_interests"):
        awards = awards + ["Interests: Traveling, cricket, music, mountain trekking, cooking, games"]
    pdf.list_section(section_awards, awards, width=98)
    pdf.save(OUT / config["filename"])


for region_key, region in REGIONS.items():
    build_resume(region_key, region)
    print(f"generated {region['filename']}")
