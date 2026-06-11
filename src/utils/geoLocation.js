const COUNTRY_REGION_MAP = {
  GB: "uk",
  UK: "uk",
  DE: "germany",
  US: "usa",
  IN: "india"
};

export async function detectRegion() {
  const storedRegion = localStorage.getItem("preferredRegion");
  if (storedRegion) return storedRegion;

  const geoRegion = await regionFromCoordinates();
  if (geoRegion) return geoRegion;

  const browserRegion = regionFromBrowserLanguage();
  if (browserRegion) return browserRegion;

  const ipRegion = await regionFromIp();
  return ipRegion || "global";
}

async function regionFromCoordinates() {
  if (!("geolocation" in navigator)) return Promise.resolve("");
  if ("permissions" in navigator) {
    try {
      const permission = await navigator.permissions.query({ name: "geolocation" });
      if (permission.state !== "granted") return "";
    } catch {
      return "";
    }
  }

  return new Promise((resolve) => {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        resolve(matchRegionByBounds(latitude, longitude));
      },
      () => resolve(""),
      { enableHighAccuracy: false, maximumAge: 86400000, timeout: 1600 }
    );
  });
}

function matchRegionByBounds(latitude, longitude) {
  const inBox = ([minLat, maxLat, minLng, maxLng]) =>
    latitude >= minLat && latitude <= maxLat && longitude >= minLng && longitude <= maxLng;

  if (inBox([49.8, 60.9, -8.7, 2.2])) return "uk";
  if (inBox([47.2, 55.1, 5.8, 15.1])) return "germany";
  if (inBox([24.4, 49.4, -125, -66.8])) return "usa";
  if (inBox([6.5, 35.7, 68.1, 97.4])) return "india";
  return "";
}

function regionFromBrowserLanguage() {
  const locales = navigator.languages?.length ? navigator.languages : [navigator.language];
  for (const locale of locales.filter(Boolean)) {
    const country = locale.split("-")[1]?.toUpperCase();
    if (country && COUNTRY_REGION_MAP[country]) return COUNTRY_REGION_MAP[country];
  }
  return "";
}

async function regionFromIp() {
  try {
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 1200);
    const response = await fetch("https://ipapi.co/json/", { signal: controller.signal });
    window.clearTimeout(timeout);
    if (!response.ok) return "";
    const data = await response.json();
    return COUNTRY_REGION_MAP[String(data.country_code || "").toUpperCase()] || "";
  } catch {
    return "";
  }
}
