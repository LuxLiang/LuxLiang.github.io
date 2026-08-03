const pages = [...document.querySelectorAll("[data-page]")];
const navLinks = [...document.querySelectorAll("[data-page-link]")];
const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.getElementById("primary-nav");
const validPages = new Set(pages.map((page) => page.dataset.page));

function pageFromHash() {
  const requestedPage = window.location.hash.slice(1);
  return validPages.has(requestedPage) ? requestedPage : "home";
}

function showPage(pageName, moveFocus = false) {
  const selectedPage = validPages.has(pageName) ? pageName : "home";

  pages.forEach((page) => {
    page.hidden = page.dataset.page !== selectedPage;
  });

  navLinks.forEach((link) => {
    if (link.dataset.pageLink === selectedPage) {
      link.setAttribute("aria-current", "page");
    } else {
      link.removeAttribute("aria-current");
    }
  });

  navigation.classList.remove("open");
  menuToggle.setAttribute("aria-expanded", "false");

  if (moveFocus) {
    document.getElementById("main-content").focus({ preventScroll: true });
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
}

document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", () => {
    const target = link.getAttribute("href").slice(1);
    if (validPages.has(target)) showPage(target, true);
  });
});

menuToggle.addEventListener("click", () => {
  const isOpen = navigation.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
});

window.addEventListener("hashchange", () => showPage(pageFromHash(), true));
document.getElementById("year").textContent = new Date().getFullYear();
showPage(pageFromHash());
