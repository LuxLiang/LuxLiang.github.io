document.documentElement.classList.add("has-js");

const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.getElementById("primary-nav");

menuToggle.addEventListener("click", () => {
  const isOpen = navigation.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
});

// Keep previously shared links such as /#cv working after the move to HTML pages.
const legacyPages = {
  home: "index.html",
  research: "research.html",
  cv: "cv.html",
  contact: "contact.html",
};

function redirectLegacyPage() {
  const name = window.location.hash.slice(1);
  if (!Object.prototype.hasOwnProperty.call(legacyPages, name)) return;
  const target = new URL(legacyPages[name], window.location.href);
  if (target.pathname !== window.location.pathname) {
    window.location.replace(target.href);
  }
}

window.addEventListener("hashchange", redirectLegacyPage);
redirectLegacyPage();
document.getElementById("year").textContent = new Date().getFullYear();
