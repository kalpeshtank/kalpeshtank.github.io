import { profile } from "../data/profile.js";

export function updateSeo(region) {
  document.title = region.seoTitle;
  setMeta("description", region.seoDescription);
  setMeta("keywords", profile.keywords.join(", "));
  setMeta("twitter:title", region.seoTitle);
  setMeta("twitter:description", region.seoDescription);
  setProperty("og:title", region.seoTitle);
  setProperty("og:description", region.seoDescription);

  const schema = {
    "@context": "https://schema.org",
    "@type": "ProfilePage",
    mainEntity: {
      "@type": "Person",
      name: profile.name,
      jobTitle: profile.role,
      email: profile.email,
      url: "https://kalpeshtank.github.io/",
      image: "https://kalpeshtank.github.io/assets/profile.jpeg",
      address: {
        "@type": "PostalAddress",
        addressLocality: "Ahmedabad",
        addressCountry: "IN"
      },
      sameAs: [profile.linkedin, profile.github],
      knowsAbout: profile.keywords
    }
  };

  const script = document.getElementById("person-schema");
  if (script) script.textContent = JSON.stringify(schema);
}

function setMeta(name, content) {
  const meta = document.querySelector(`meta[name="${name}"]`);
  if (meta) meta.setAttribute("content", content);
}

function setProperty(property, content) {
  const meta = document.querySelector(`meta[property="${property}"]`);
  if (meta) meta.setAttribute("content", content);
}
