document.addEventListener("DOMContentLoaded", () => {
    // DOM Elements
    const searchInput = document.getElementById("search-input");
    const regionSelect = document.getElementById("region-select");
    const citiesList = document.getElementById("cities-list");
    const viewportContent = document.getElementById("viewport-content");
    const mapToggleBtn = document.getElementById("map-toggle-btn");
    const mapModal = document.getElementById("map-modal");
    const closeModalBtn = document.getElementById("close-modal-btn");
    const statsPercentage = document.getElementById("stats-percentage");
    const statsProgress = document.getElementById("stats-progress");
    const statsProgressBar = document.getElementById("stats-progress-bar");

    // Initialize State
    let activeCity = null;

    // Load data from web_data.js
    const cities = TRAVEL_DATA || {};

    // Helper functions
    function calculateStats() {
        const total = 81;
        const visited = Object.keys(cities).length;
        const pct = ((visited / total) * 100).toFixed(1);

        statsPercentage.innerText = `%${pct}`;
        statsProgress.innerText = `(${visited}/81)`;
        statsProgressBar.style.width = `${pct}%`;
    }

    function renderCitiesList(filterText = "", filterRegion = "all") {
        citiesList.innerHTML = "";
        
        const sortedCities = Object.keys(cities).sort((a, b) => a.localeCompare(b, 'tr'));

        sortedCities.forEach(cityName => {
            const city = cities[cityName];
            
            // Search filter
            const matchesSearch = cityName.toLowerCase().includes(filterText.toLowerCase()) || 
                                  city.region.toLowerCase().includes(filterText.toLowerCase());
            
            // Region filter
            const matchesRegion = filterRegion === "all" || city.region === filterRegion;

            if (matchesSearch && matchesRegion) {
                const item = document.createElement("div");
                item.className = `city-list-item glass ${activeCity === cityName ? 'active' : ''}`;
                item.innerHTML = `
                    <div>
                        <div class="city-name">${cityName}</div>
                        <div class="city-region">${city.region}</div>
                    </div>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: var(--primary);">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                `;

                item.addEventListener("click", () => {
                    document.querySelectorAll(".city-list-item").forEach(el => el.classList.remove("active"));
                    item.classList.add("active");
                    renderCityDetails(cityName);
                });

                citiesList.appendChild(item);
            }
        });

        if (citiesList.innerHTML === "") {
            citiesList.innerHTML = `
                <div style="text-align: center; color: var(--text-muted); font-size: 12px; padding: 20px;">
                    Eşleşen şehir bulunamadı.
                </div>
            `;
        }
    }

    function renderCityDetails(cityName) {
        activeCity = cityName;
        const city = cities[cityName];

        if (!city) return;

        // Parse Gastronomy markdown bullet list
        let gastroHTML = "";
        if (city.gastronomi) {
            const items = city.gastronomi.split("\n");
            items.forEach(item => {
                if (item.trim()) {
                    // Remove markdown bullet and bold markers
                    const cleanItem = item.replace(/^-\s*\*\*/, "").replace(/\*\*/g, "").replace(/^-\s*/, "");
                    gastroHTML += `<div class="gastronomy-item">${cleanItem}</div>`;
                }
            });
        }

        // Parse Landmarks check list
        let landmarksHTML = "";
        if (city.landmarks && city.landmarks.length > 0) {
            city.landmarks.forEach(landmark => {
                landmarksHTML += `
                    <div class="landmark-item glass">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="20 6 9 17 4 12"></polyline>
                        </svg>
                        <span>${landmark}</span>
                    </div>
                `;
            });
        }

        // Build Library Notes
        let libraryHTML = "";
        if (city.library) {
            libraryHTML = `
                <div class="library-notes-card glass">
                    <div class="section-title">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                        </svg>
                        Seyyahın Kütüphane Notu
                    </div>
                    <p>${city.library}</p>
                </div>
            `;
        }

        viewportContent.innerHTML = `
            <div class="city-details">
                <div class="city-hero" style="background-image: url('${city.banner}')">
                    <div class="city-hero-text">
                        <span class="city-tag">${city.region}</span>
                        <h2>${cityName}</h2>
                    </div>
                </div>
                
                <div class="city-main-content">
                    <div class="quote-card glass">
                        <p class="hikmet">${city.hikmet}</p>
                        <p class="quote">"${city.quote}"</p>
                    </div>

                    <div class="city-text-section">
                        <div class="section-title">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="12" y1="16" x2="12" y2="12"></line>
                                <line x1="12" y1="8" x2="12.01" y2="8"></line>
                            </svg>
                            Şehrin Dokusu ve Hatırası
                        </div>
                        <p>${city.description.replace(/\n\n/g, "<br><br>")}</p>
                    </div>

                    <div class="city-text-section">
                        <div class="section-title">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                            </svg>
                            Gezginin Not Defterinden (İçsel Düşünceler)
                        </div>
                        <p>${city.sufi_notes.replace(/\n\n/g, "<br><br>")}</p>
                    </div>

                    ${libraryHTML}

                    <div class="info-columns">
                        ${gastroHTML ? `
                        <div class="column-card glass">
                            <div class="section-title">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                                </svg>
                                Yöresel Lezzet Tavsiyeleri
                            </div>
                            <div class="gastronomi-list">
                                ${gastroHTML}
                            </div>
                        </div>
                        ` : ''}

                        ${landmarksHTML ? `
                        <div class="column-card glass">
                            <div class="section-title">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                                    <circle cx="12" cy="10" r="3"></circle>
                                </svg>
                                Keşfedilesi Duraklar
                            </div>
                            <div class="landmarks-list">
                                ${landmarksHTML}
                            </div>
                        </div>
                        ` : ''}
                    </div>
                </div>
            </div>
        `;
        // Scroll viewport to top smoothly
        viewportContent.scrollTo({ top: 0, behavior: "smooth" });
    }

    // Populate Region Dropdown dynamically based on data
    function populateRegionFilter() {
        const uniqueRegions = new Set();
        Object.keys(cities).forEach(key => {
            uniqueRegions.add(cities[key].region);
        });

        uniqueRegions.forEach(region => {
            const opt = document.createElement("option");
            opt.value = region;
            opt.innerText = region;
            regionSelect.appendChild(opt);
        });
    }

    // Event Listeners
    searchInput.addEventListener("input", (e) => {
        renderCitiesList(e.target.value, regionSelect.value);
    });

    regionSelect.addEventListener("change", (e) => {
        renderCitiesList(searchInput.value, e.target.value);
    });

    mapToggleBtn.addEventListener("click", () => {
        mapModal.style.display = "flex";
    });

    closeModalBtn.addEventListener("click", () => {
        mapModal.style.display = "none";
    });

    mapModal.addEventListener("click", (e) => {
        if (e.target === mapModal) {
            mapModal.style.display = "none";
        }
    });

    // Run Initializations
    calculateStats();
    populateRegionFilter();
    renderCitiesList();

    // Auto-select first city on load
    const firstCity = Object.keys(cities).sort((a, b) => a.localeCompare(b, 'tr'))[0];
    if (firstCity) {
        renderCityDetails(firstCity);
    }
});
