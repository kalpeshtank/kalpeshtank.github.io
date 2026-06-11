import { experience, projects, skills } from "./data/profile.js";
import { regions, resumes } from "./data/regions.js";
import { detectRegion } from "./utils/geoLocation.js";
import { updateSeo } from "./utils/seo.js";

const supportedLanguages = ["en", "de"];
const savedLanguage = localStorage.getItem("preferredLanguage");

const state = {
  region: "global",
  language: supportedLanguages.includes(savedLanguage) ? savedLanguage : "en",
  translations: {}
};

let revealObserver;

document.addEventListener("DOMContentLoaded", async () => {
  document.getElementById("year").textContent = new Date().getFullYear();
  setupTheme();
  setupNavigation();
  setupScrollUi();
  setupStatCounters();

  state.region = await detectRegion();
  if (!regions[state.region]) state.region = "global";

  const regionSelect = document.getElementById("region-select");
  const languageSelect = document.getElementById("language-select");
  regionSelect.value = state.region;
  languageSelect.value = state.language;

  regionSelect.addEventListener("change", (event) => {
    state.region = event.target.value;
    localStorage.setItem("preferredRegion", state.region);
    render();
  });

  languageSelect.addEventListener("change", async (event) => {
    state.language = event.target.value;
    localStorage.setItem("preferredLanguage", state.language);
    await loadTranslations();
    render();
  });

  await loadTranslations();
  render();
  document.body.classList.remove("preload");
});

async function loadTranslations() {
  try {
    const response = await fetch(`src/i18n/${state.language}.json`);
    state.translations = response.ok ? await response.json() : {};
  } catch {
    state.translations = {};
  }
}

function render() {
  const region = regions[state.region] || regions.global;
  updateTranslations();
  updateRegion(region);
  renderSkills();
  renderExperience();
  renderProjects();
  renderResumes();
  updateSeo(region);
  refreshIcons();
  applyRevealStagger();
  revealVisibleElements();
}

function updateTranslations() {
  document.documentElement.lang = state.language;
  document.querySelectorAll("[data-i18n]").forEach((node) => {
    const value = getTranslation(node.dataset.i18n);
    if (value) node.textContent = value;
  });
}

function getTranslation(path) {
  return path.split(".").reduce((value, key) => value?.[key], state.translations);
}

function updateRegion(region) {
  document.getElementById("region-label").textContent = region.label;
  document.getElementById("about-summary").textContent = region.summary;

  const primaryResume = document.getElementById("primary-resume");
  primaryResume.href = region.resumePath;
  primaryResume.querySelector("span").textContent = region.resumeLabel;
}

function renderSkills() {
  const container = document.getElementById("skills-grid");
  container.innerHTML = Object.entries(skills)
    .map(
      ([group, items]) => `
        <article class="skills-card">
          <h3>${group}</h3>
          <div class="badges">
            ${items.map((item) => `<span>${item}</span>`).join("")}
          </div>
        </article>
      `
    )
    .join("");
}

function renderExperience() {
  const container = document.getElementById("experience-list");
  container.innerHTML = experience
    .map(
      (job) => {
        const localized = state.language === "de" ? job.de || {} : {};
        const title = localized.title || job.title;
        const bullets = localized.bullets || job.bullets;
        return `
        <article class="job">
          <div class="job-top">
            <div>
              <h3>${title}</h3>
              <strong>${job.company}</strong>
            </div>
            <span>${job.period}</span>
          </div>
          <p class="job-location">${job.location}</p>
          <ul>
            ${bullets.map((bullet) => `<li>${bullet}</li>`).join("")}
          </ul>
        </article>
      `;
      }
    )
    .join("");
}

function renderProjects() {
  const labels = labelTranslations();
  const container = document.getElementById("projects-grid");
  container.innerHTML = projects
    .map((project, index) => {
      const localized = state.language === "de" ? project.de || {} : {};
      const name = localized.name || project.name;
      const role = localized.role || project.role;
      const features = localized.features || project.features;
      const impact = localized.impact || project.impact;
      return `
        <article class="project-card">
          <span class="project-kicker">0${index + 1}</span>
          <h3>${name}</h3>
          <div class="project-meta">
            <span><strong>${labels.stack}:</strong> ${project.stack}</span>
            <span><strong>${labels.role}:</strong> ${role}</span>
          </div>
          <p class="project-impact"><strong>${labels.impact}:</strong> ${impact}</p>
          <ul>
            ${features.map((feature) => `<li>${feature}</li>`).join("")}
          </ul>
        </article>
      `;
    })
    .join("");
}

function renderResumes() {
  const labels = labelTranslations();
  const container = document.getElementById("resume-grid");
  container.innerHTML = resumes
    .map((resume) => {
      const region = regions[resume.region];
      return `
        <article class="resume-card">
          <div>
            <h3>${resume.title}</h3>
            <p>${resume.description}</p>
          </div>
          <a class="button secondary" href="${region.resumePath}" download>
            <i data-feather="download"></i>
            <span>${labels.download}</span>
          </a>
        </article>
      `;
    })
    .join("");
}

function labelTranslations() {
  return {
    role: getTranslation("labels.role") || "Role",
    stack: getTranslation("labels.stack") || "Tech stack",
    impact: getTranslation("labels.impact") || "Business impact",
    download: getTranslation("labels.download") || "Download"
  };
}

function setupTheme() {
  const toggle = document.getElementById("theme-toggle");
  if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light");
    toggle.innerHTML = '<i data-feather="sun"></i>';
  }

  toggle.addEventListener("click", () => {
    const isLight = document.body.classList.toggle("light");
    localStorage.setItem("theme", isLight ? "light" : "dark");
    toggle.innerHTML = isLight ? '<i data-feather="sun"></i>' : '<i data-feather="moon"></i>';
    refreshIcons();
  });
}

function setupNavigation() {
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.getElementById("nav-menu");

  toggle.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });

  menu.addEventListener("click", (event) => {
    if (event.target.matches("a")) {
      menu.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    }
  });
}

function setupScrollUi() {
  const progress = document.getElementById("scroll-progress");
  const backToTop = document.getElementById("back-to-top");
  const navLinks = [...document.querySelectorAll(".nav-menu a")];
  const sections = [...document.querySelectorAll("main section")];
  revealObserver = new IntersectionObserver(
    (entries) => entries.forEach((entry) => entry.isIntersecting && entry.target.classList.add("visible")),
    { threshold: 0.12 }
  );

  document.querySelectorAll(".fade-up").forEach((element) => revealObserver.observe(element));

  window.addEventListener("scroll", () => {
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = maxScroll > 0 ? `${(window.scrollY / maxScroll) * 100}%` : "0";
    backToTop.classList.toggle("show", window.scrollY > 420);

    let current = "";
    sections.forEach((section) => {
      if (window.scrollY >= section.offsetTop - 150) current = section.id;
    });
    navLinks.forEach((link) => link.classList.toggle("active", link.getAttribute("href") === `#${current}`));
  });

  backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
}

function setupStatCounters() {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const statNumbers = [...document.querySelectorAll(".stats-band strong")];

  if (prefersReducedMotion) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        animateStat(entry.target);
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.4 }
  );

  statNumbers.forEach((stat) => observer.observe(stat));
}

function animateStat(stat) {
  const rawValue = stat.textContent.trim();
  const match = rawValue.match(/^(\d+)(\+?)$/);
  if (!match) return;

  const target = Number(match[1]);
  const suffix = match[2] || "";
  const duration = 900;
  const start = performance.now();

  function tick(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    stat.textContent = `${Math.round(target * eased)}${suffix}`;
    if (progress < 1) requestAnimationFrame(tick);
  }

  stat.textContent = `0${suffix}`;
  requestAnimationFrame(tick);
}

function applyRevealStagger() {
  const groups = [
    ...document.querySelectorAll(".skills-grid, .project-grid, .resume-grid, .info-grid, .timeline")
  ];

  groups.forEach((group) => {
    [...group.children].forEach((child, index) => {
      child.classList.add("fade-up");
      child.style.setProperty("--reveal-delay", `${Math.min(index * 70, 280)}ms`);
      revealObserver?.observe(child);
    });
  });
}

function revealVisibleElements() {
  document.querySelectorAll(".fade-up").forEach((element) => {
    const rect = element.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.9) element.classList.add("visible");
  });
}

function refreshIcons() {
  if (window.feather) window.feather.replace();
}
