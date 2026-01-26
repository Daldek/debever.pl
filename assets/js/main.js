/**
 * main.js - Skrypty strony debever.pl
 */

document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu toggle
  const navToggle = document.querySelector('.nav__toggle');
  const navList = document.querySelector('.nav__list');

  if (navToggle && navList) {
    navToggle.addEventListener('click', () => {
      const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', !isExpanded);
      navList.classList.toggle('is-active');
    });

    // Close menu when clicking a link
    navList.querySelectorAll('.nav__link').forEach(link => {
      link.addEventListener('click', () => {
        navToggle.setAttribute('aria-expanded', 'false');
        navList.classList.remove('is-active');
      });
    });
  }

  // Close menu when clicking outside
  document.addEventListener('click', (e) => {
    if (navList && navList.classList.contains('is-active')) {
      if (!e.target.closest('.nav')) {
        navToggle.setAttribute('aria-expanded', 'false');
        navList.classList.remove('is-active');
      }
    }
  });

  // Cookie Consent & Google Analytics
  initCookieConsent();
});

/**
 * Cookie Consent Management
 */
function initCookieConsent() {
  const COOKIE_KEY = 'cookie_consent';
  const banner = document.getElementById('cookie-banner');
  const acceptBtn = document.getElementById('cookie-accept');
  const rejectBtn = document.getElementById('cookie-reject');

  if (!banner) return;

  const consent = localStorage.getItem(COOKIE_KEY);

  if (consent === null) {
    banner.hidden = false;
  } else if (consent === 'accepted') {
    loadGoogleAnalytics();
  }

  acceptBtn?.addEventListener('click', () => {
    localStorage.setItem(COOKIE_KEY, 'accepted');
    banner.hidden = true;
    loadGoogleAnalytics();
  });

  rejectBtn?.addEventListener('click', () => {
    localStorage.setItem(COOKIE_KEY, 'rejected');
    banner.hidden = true;
  });
}

/**
 * Load Google Analytics 4
 */
function loadGoogleAnalytics() {
  const measurementId = window.GA_MEASUREMENT_ID;

  // Validate Measurement ID format (G-XXXXXXXXXX or GT-XXXXXXXXXX)
  const GA_ID_PATTERN = /^(G|GT)-[A-Z0-9]{10,12}$/;

  if (!measurementId || measurementId === 'G-XXXXXXXXXX') {
    console.warn('Google Analytics: Measurement ID not configured');
    return;
  }

  if (!GA_ID_PATTERN.test(measurementId)) {
    console.error('Google Analytics: Invalid Measurement ID format');
    return;
  }

  // Load gtag.js
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(measurementId)}`;
  document.head.appendChild(script);

  // Initialize gtag
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  gtag('js', new Date());
  gtag('config', measurementId, {
    anonymize_ip: true
  });

  window.gtag = gtag;
}
