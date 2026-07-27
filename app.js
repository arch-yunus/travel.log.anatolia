document.addEventListener("DOMContentLoaded", () => {
    // DOM Elements
    const searchInput = document.getElementById("search-input");
    const regionSelect = document.getElementById("region-select");
    const citiesList = document.getElementById("cities-list");
    const viewportContent = document.getElementById("viewport-content");
    const mapToggleBtn = document.getElementById("map-toggle-btn");
    const dashboardBtn = document.getElementById("dashboard-btn");
    const logoSection = document.getElementById("logo-section");
    const mapModal = document.getElementById("map-modal");
    const closeModalBtn = document.getElementById("close-modal-btn");
    const statsPercentage = document.getElementById("stats-percentage");
    const statsProgress = document.getElementById("stats-progress");
    const statsProgressBar = document.getElementById("stats-progress-bar");

    // Initialize State
    let activeCity = null;
    let activeTab = "portre"; // Options: portre, kesif, gastronomi, manevi

    // Load data from web_data.js
    const cities = TRAVEL_DATA || {};

    // Region configuration and total cities lists
    const REGION_TOTALS = {
        "Marmara Bölgesi": ["Balıkesir", "Bilecik", "Bursa", "Edirne", "Kocaeli", "Kırklareli", "Sakarya", "Tekirdağ", "Yalova", "Çanakkale", "İstanbul"],
        "Ege Bölgesi": ["Afyonkarahisar", "Aydın", "Denizli", "Kütahya", "Manisa", "Muğla", "Uşak", "İzmir"],
        "Akdeniz Bölgesi": ["Adana", "Antalya", "Burdur", "Hatay", "Isparta", "Kahramanmaraş", "Mersin", "Osmaniye"],
        "İç Anadolu Bölgesi": ["Aksaray", "Ankara", "Eskişehir", "Karaman", "Kayseri", "Konya", "Kırıkkale", "Kırşehir", "Nevşehir", "Niğde", "Sivas", "Yozgat", "Çankırı"],
        "Karadeniz Bölgesi": ["Amasya", "Artvin", "Bartın", "Bayburt", "Bolu", "Düzce", "Giresun", "Gümüşhane", "Karabük", "Kastamonu", "Ordu", "Rize", "Samsun", "Sinop", "Tokat", "Trabzon", "Zonguldak", "Çorum"],
        "Doğu Anadolu Bölgesi": ["Ardahan", "Ağrı", "Bingöl", "Bitlis", "Elazığ", "Erzincan", "Erzurum", "Hakkari", "Iğdır", "Kars", "Malatya", "Muş", "Tunceli", "Van"],
        "Güneydoğu Anadolu Bölgesi": ["Adıyaman", "Batman", "Diyarbakır", "Gaziantep", "Kilis", "Mardin", "Siirt", "Şanlıurfa", "Şırnak"]
    };

    // Helper functions for state
    function calculateStats() {
        const total = 81;
        const visited = Object.keys(cities).length;
        const pct = ((visited / total) * 100).toFixed(1);

        statsPercentage.innerText = `%${pct}`;
        statsProgress.innerText = `(${visited}/81)`;
        statsProgressBar.style.width = `${pct}%`;
    }

    // LocalStorage helpers for landmark checklists
    function toggleLandmark(cityName, landmarkName, isChecked) {
        const key = `travel_landmark_${cityName}_${landmarkName}`;
        if (isChecked) {
            localStorage.setItem(key, "true");
        } else {
            localStorage.removeItem(key);
        }
    }

    function isLandmarkChecked(cityName, landmarkName) {
        const key = `travel_landmark_${cityName}_${landmarkName}`;
        return localStorage.getItem(key) === "true";
    }

    function getLandmarkProgress(cityName) {
        const city = cities[cityName];
        if (!city || !city.landmarks || city.landmarks.length === 0) return { checked: 0, total: 0, pct: 0 };
        
        let checked = 0;
        city.landmarks.forEach(l => {
            if (isLandmarkChecked(cityName, l)) checked++;
        });
        return {
            checked,
            total: city.landmarks.length,
            pct: Math.round((checked / city.landmarks.length) * 100)
        };
    }

    // Render cities on the sidebar
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
                
                const progress = getLandmarkProgress(cityName);
                const progressIndicator = progress.total > 0 
                    ? `<div class="city-landmark-bullet">${progress.checked}/${progress.total} Durak</div>` 
                    : '';

                item.innerHTML = `
                    <div>
                        <div class="city-name">${cityName}</div>
                        <div class="city-region">${city.region}</div>
                    </div>
                    <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 4px;">
                        ${progressIndicator}
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: var(--primary);">
                            <polyline points="9 18 15 12 9 6"></polyline>
                        </svg>
                    </div>
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

    // Interactive Calculator Logic
    function initCalculator() {
        const hotelInput = document.getElementById("hotel-rate");
        const foodInput = document.getElementById("food-rate");
        const travelInput = document.getElementById("travel-rate");
        
        if (!hotelInput || !foodInput || !travelInput) return;
        
        const hotelVal = document.getElementById("hotel-rate-val");
        const foodVal = document.getElementById("food-rate-val");
        const travelVal = document.getElementById("travel-rate-val");
        
        const savingsEl = document.getElementById("calc-savings");
        const costEl = document.getElementById("calc-cost");
        const profitEl = document.getElementById("calc-profit");
        
        const visitedCount = Object.keys(cities).length;
        
        function updateCalculations() {
            const hotelRate = parseInt(hotelInput.value);
            const foodRate = parseInt(foodInput.value);
            const travelRate = parseInt(travelInput.value);
            
            // Update labels
            hotelVal.innerText = hotelRate;
            foodVal.innerText = foodRate;
            travelVal.innerText = travelRate;
            
            // Calculate
            const totalDays = visitedCount * 5;
            const savings = totalDays * hotelRate;
            const cost = (totalDays * foodRate) + (visitedCount * travelRate);
            const profit = savings - cost;
            
            // Format currency helper
            const formatCurrency = (val) => {
                return new Intl.NumberFormat('tr-TR', { 
                    style: 'currency', 
                    currency: 'TRY', 
                    maximumFractionDigits: 0 
                }).format(val);
            };
            
            savingsEl.innerText = formatCurrency(savings);
            costEl.innerText = formatCurrency(cost);
            profitEl.innerText = formatCurrency(profit);
        }
        
        hotelInput.addEventListener("input", updateCalculations);
        foodInput.addEventListener("input", updateCalculations);
        travelInput.addEventListener("input", updateCalculations);
        
        updateCalculations();
    }

    // Render dashboard overview (Landing page when no city is active)
    function renderDashboard() {
        activeCity = null;
        
        // Remove active class from sidebar list
        document.querySelectorAll(".city-list-item").forEach(el => el.classList.remove("active"));

        const visitedCount = Object.keys(cities).length;
        const totalCount = 81;
        const generalPct = ((visitedCount / totalCount) * 100).toFixed(1);

        // Compute regional details
        let regionsHTML = "";
        Object.keys(REGION_TOTALS).forEach(regionName => {
            const totalInRegion = REGION_TOTALS[regionName].length;
            const visitedInRegion = Object.keys(cities).filter(cityName => cities[cityName].region === regionName).length;
            const pctRegion = ((visitedInRegion / totalInRegion) * 100).toFixed(0);

            regionsHTML += `
                <div class="region-card glass">
                    <div class="region-header">
                        <span class="region-title-text">${regionName}</span>
                        <span class="region-count-badge">${visitedInRegion} / ${totalInRegion} İl</span>
                    </div>
                    <div class="progress-bar-bg" style="height: 6px; margin: 8px 0;">
                        <div class="progress-bar-fill" style="width: ${pctRegion}%; background: linear-gradient(90deg, var(--primary), var(--secondary));"></div>
                    </div>
                    <div class="region-percentage-text">%${pctRegion} Keşfedildi</div>
                </div>
            `;
        });

        // Compute highlights (3 visited cities for landing page show-offs)
        let highlightsHTML = "";
        const visitedCityNames = Object.keys(cities);
        const shuffled = visitedCityNames.sort(() => 0.5 - Math.random());
        const selectedHighlights = shuffled.slice(0, 3);

        selectedHighlights.forEach(cName => {
            const city = cities[cName];
            highlightsHTML += `
                <div class="highlight-card glass" style="background-image: linear-gradient(180deg, rgba(12, 18, 37, 0.4) 0%, rgba(12, 18, 37, 0.9) 100%), url('${city.banner}');" onclick="selectCityFromDashboard('${cName}')">
                    <div class="highlight-info">
                        <span class="highlight-region">${city.region}</span>
                        <h4>${cName}</h4>
                        <p class="highlight-desc">"${city.hikmet}"</p>
                    </div>
                </div>
            `;
        });

        // Set viewport content
        viewportContent.innerHTML = `
            <div class="dashboard-view">
                <!-- Welcome Banner -->
                <div class="dashboard-hero">
                    <div class="dashboard-hero-text">
                        <span class="dashboard-badge">YOL NOTLARI vPRO</span>
                        <h2>ANADOLU SEYAHATNAMESİ</h2>
                        <p>Biz, yolların bitmediği, keşfin son bulmadığı bir dünyanın yolcularıyız. Her durak yeni bir hikaye, her şehir içsel bir tefekkürdür.</p>
                    </div>
                </div>

                <!-- Stats Grid -->
                <div class="stats-grid">
                    <div class="stat-card glass">
                        <div class="stat-icon-wrapper" style="background: rgba(46, 204, 113, 0.15); color: var(--primary);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                        </div>
                        <div class="stat-val">%${generalPct}</div>
                        <div class="stat-label">Toplam İlerleme</div>
                    </div>
                    <div class="stat-card glass">
                        <div class="stat-icon-wrapper" style="background: rgba(0, 242, 254, 0.15); color: var(--secondary);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                        </div>
                        <div class="stat-val">${visitedCount} / ${totalCount}</div>
                        <div class="stat-label">Ziyaret Edilen İl</div>
                    </div>
                    <div class="stat-card glass">
                        <div class="stat-icon-wrapper" style="background: rgba(155, 89, 182, 0.15); color: #9b59b6;">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                        </div>
                        <div class="stat-val">${visitedCount * 5} Gün</div>
                        <div class="stat-label">Sahadaki Rota Süresi</div>
                    </div>
                    <div class="stat-card glass">
                        <div class="stat-icon-wrapper" style="background: rgba(230, 126, 34, 0.15); color: #e67e22;">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                        </div>
                        <div class="stat-val">${visitedCount * 4 * 5} Saat</div>
                        <div class="stat-label">Kütüphane Çalışması</div>
                    </div>
                </div>

                <!-- Interactive Budget Calculator -->
                <div class="calculator-card glass">
                    <h4>💰 GSB Seyahatsever & Bütçe Analizi</h4>
                    <p class="calc-subtitle">KYK yurtlarında konaklayarak sağladığınız tasarrufu ve seyahat bütçenizi simüle edin.</p>
                    
                    <div class="calc-inputs">
                        <div class="calc-input-group">
                            <label for="hotel-rate">Otel Gecelik Ücreti (TL): <span id="hotel-rate-val">1500</span> TL</label>
                            <input type="range" id="hotel-rate" min="500" max="5000" step="100" value="1500">
                        </div>
                        <div class="calc-input-group">
                            <label for="food-rate">Günlük Yemek Bütçesi (TL): <span id="food-rate-val">300</span> TL</label>
                            <input type="range" id="food-rate" min="100" max="1500" step="50" value="300">
                        </div>
                        <div class="calc-input-group">
                            <label for="travel-rate">Şehirlerarası Ulaşım (TL): <span id="travel-rate-val">500</span> TL</label>
                            <input type="range" id="travel-rate" min="100" max="2500" step="50" value="500">
                        </div>
                    </div>
                    
                    <div class="calc-results">
                        <div class="calc-result-item">
                            <span class="calc-result-label">🏠 KYK Konaklama Tasarrufu:</span>
                            <span class="calc-result-val savings" id="calc-savings">0 TL</span>
                        </div>
                        <div class="calc-result-item">
                            <span class="calc-result-label">🚌 Ulaşım & Yemek Maliyeti:</span>
                            <span class="calc-result-val cost" id="calc-cost">0 TL</span>
                        </div>
                        <div class="calc-result-item highlight">
                            <span class="calc-result-label">💡 Net Finansal Kazanç:</span>
                            <span class="calc-result-val profit" id="calc-profit">0 TL</span>
                        </div>
                    </div>
                </div>

                <!-- Two-Column Layout -->
                <div class="dashboard-panels">
                    <!-- Left: Region Breakdown -->
                    <div class="dashboard-panel-left">
                        <h3 class="panel-title-heading">Bölgesel Keşif Dağılımı</h3>
                        <div class="regions-grid-container">
                            ${regionsHTML}
                        </div>
                    </div>

                    <!-- Right: Travel Methodology -->
                    <div class="dashboard-panel-right">
                        <h3 class="panel-title-heading">Seyahat Disiplini ve Manifesto</h3>
                        <div class="methodology-card glass">
                            <div class="methodology-item">
                                <strong>🎒 Yarı Göçebe, Tam Seyyah:</strong> Her yaz dönemi 45 günlük komşu il rotası çizilerek yol yorgunluğu ve maliyeti minimize edilir.
                            </div>
                            <div class="methodology-item">
                                <strong>🏠 Sıfır Bütçeli Konaklama:</strong> T.C. GSB "Seyahatsever" projesi kapsamında KYK yurtlarında kalınarak bütçe korunur.
                            </div>
                            <div class="methodology-item">
                                <strong>💻 Kütüphane & Keşif Dengesi:</strong> Günün ilk yarısı (09:00-13:00) kütüphanede kodlama ve gelişime, ikinci yarısı ise coğrafi keşfe ayrılır.
                            </div>
                        </div>

                        ${selectedHighlights.length > 0 ? `
                        <h3 class="panel-title-heading" style="margin-top: 24px;">Derin Keşiflerden Seçmeler</h3>
                        <div class="highlights-container">
                            ${highlightsHTML}
                        </div>
                        ` : ''}
                    </div>
                </div>
            </div>
        `;
        
        initCalculator();
    }

    // Exposed function for highlight clicks
    window.selectCityFromDashboard = (cityName) => {
        activeCity = cityName;
        // Find in sidebar list and trigger click highlight
        renderCitiesList(searchInput.value, regionSelect.value);
        renderCityDetails(cityName);
    };

    // Render city details view (Tabbed Layout)
    function renderCityDetails(cityName) {
        activeCity = cityName;
        const city = cities[cityName];

        if (!city) return;

        // Build Coordinates / Map UI Elements
        let mapLinkHTML = "";
        if (city.coords && city.coords.length === 2) {
            const lat = city.coords[0];
            const lng = city.coords[1];
            mapLinkHTML = `
                <a href="https://www.google.com/maps/search/?api=1&query=${lat},${lng}" target="_blank" class="maps-btn glass">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/>
                        <circle cx="12" cy="10" r="3"/>
                    </svg>
                    Google Haritalar'da Gör (${lat.toFixed(4)}, ${lng.toFixed(4)})
                </a>
            `;
        }

        // Render Tabs Navigation Header
        const tabsHeaderHTML = `
            <div class="details-tabs glass">
                <button class="tab-btn ${activeTab === 'portre' ? 'active' : ''}" onclick="switchTab('${cityName}', 'portre')">
                    📜 Şehir Portresi
                </button>
                <button class="tab-btn ${activeTab === 'kesif' ? 'active' : ''}" onclick="switchTab('${cityName}', 'kesif')">
                    🗺️ Keşif Rotaları
                </button>
                <button class="tab-btn ${activeTab === 'gastronomi' ? 'active' : ''}" onclick="switchTab('${cityName}', 'gastronomi')">
                    🍲 Yöresel Lezzetler
                </button>
                <button class="tab-btn ${activeTab === 'manevi' ? 'active' : ''}" onclick="switchTab('${cityName}', 'manevi')">
                    📿 Sufi Notları
                </button>
            </div>
        `;

        // Render Active Tab Content
        let tabContentHTML = "";
        
        if (activeTab === "portre") {
            // Build Library Notes card
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

            tabContentHTML = `
                <div class="tab-pane-content fade-in">
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

                    ${libraryHTML}
                </div>
            `;
        } 
        else if (activeTab === "kesif") {
            const progress = getLandmarkProgress(cityName);
            
            let landmarksListHTML = "";
            if (city.landmarks && city.landmarks.length > 0) {
                city.landmarks.forEach((landmark, index) => {
                    const checked = isLandmarkChecked(cityName, landmark);
                    landmarksListHTML += `
                        <label class="landmark-checkbox-card glass ${checked ? 'checked' : ''}">
                            <input type="checkbox" 
                                   ${checked ? 'checked' : ''} 
                                   onchange="toggleLandmarkState('${cityName}', '${landmark.replace(/'/g, "\\'")}', this)">
                            <div class="checkbox-custom">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="20 6 9 17 4 12"></polyline>
                                </svg>
                            </div>
                            <span class="landmark-name-label">${landmark}</span>
                        </label>
                    `;
                });
            } else {
                landmarksListHTML = `<div class="empty-tab-message">Henüz keşif durağı eklenmedi.</div>`;
            }

            tabContentHTML = `
                <div class="tab-pane-content fade-in">
                    <div class="landmark-progress-container glass">
                        <div class="landmark-progress-header">
                            <span>Keşif Tamamlama Raporu</span>
                            <strong id="landmark-progress-text">${progress.checked} / ${progress.total} Durak (%${progress.pct})</strong>
                        </div>
                        <div class="progress-bar-bg" style="height: 10px; margin-top: 8px;">
                            <div class="progress-bar-fill" id="landmark-progress-bar-fill" style="width: ${progress.pct}%; background: linear-gradient(90deg, #2ecc71, #00f2fe);"></div>
                        </div>
                    </div>

                    <div class="landmarks-grid-layout" style="margin-top: 20px;">
                        ${landmarksListHTML}
                    </div>
                </div>
            `;
        } 
        else if (activeTab === "gastronomi") {
            let gastroCardsHTML = "";
            if (city.gastronomi) {
                const items = city.gastronomi.split("\n");
                items.forEach(item => {
                    if (item.trim()) {
                        // Parse name and description from format: "- **Title:** Description"
                        const cleanItem = item.replace(/^-\s*/, "");
                        const parts = cleanItem.split(":**");
                        let title = "";
                        let desc = "";

                        if (parts.length >= 2) {
                            title = parts[0].replace(/\*\*/g, "").trim();
                            desc = parts.slice(1).join(":**").trim();
                        } else {
                            title = cleanItem.replace(/\*\*/g, "").trim();
                            desc = "Yöresel lezzet tavsiyesi.";
                        }

                        gastroCardsHTML += `
                            <div class="gastro-card glass">
                                <div class="gastro-icon">🍲</div>
                                <div class="gastro-body">
                                    <h5>${title}</h5>
                                    <p>${desc}</p>
                                </div>
                            </div>
                        `;
                    }
                });
            } else {
                gastroCardsHTML = `<div class="empty-tab-message">Henüz lezzet tavsiyesi eklenmedi.</div>`;
            }

            tabContentHTML = `
                <div class="tab-pane-content fade-in">
                    <div class="gastro-grid-layout">
                        ${gastroCardsHTML}
                    </div>
                </div>
            `;
        } 
        else if (activeTab === "manevi") {
            tabContentHTML = `
                <div class="tab-pane-content fade-in">
                    <div class="spiritual-parchment glass">
                        <div class="parchment-border">
                            <h4 class="parchment-title">Dervişin Tefekkür Günlüğü</h4>
                            <p class="parchment-content">${city.sufi_notes.replace(/\n\n/g, "<br><br>")}</p>
                        </div>
                    </div>
                </div>
            `;
        }

        // Render main wrapper in Viewport
        viewportContent.innerHTML = `
            <div class="city-details">
                <div class="city-hero" style="background-image: linear-gradient(180deg, rgba(6, 9, 19, 0.1) 0%, rgba(6, 9, 19, 0.8) 100%), url('${city.banner}')">
                    <div class="city-hero-text">
                        <div style="display: flex; justify-content: space-between; align-items: flex-end; width: 100%; flex-wrap: wrap; gap: 16px;">
                            <div>
                                <span class="city-tag">${city.region}</span>
                                <h2>${cityName}</h2>
                            </div>
                            ${mapLinkHTML}
                        </div>
                    </div>
                </div>
                
                <div class="city-main-content">
                    ${tabsHeaderHTML}
                    ${tabContentHTML}
                </div>
            </div>
        `;

        // Scroll viewport to top smoothly
        viewportContent.scrollTo({ top: 0, behavior: "smooth" });
    }

    // Exposed function for Tab toggles
    window.switchTab = (cityName, tabName) => {
        activeTab = tabName;
        renderCityDetails(cityName);
    };

    // Exposed function for Landmark checklist toggles
    window.toggleLandmarkState = (cityName, landmarkName, checkboxEl) => {
        const isChecked = checkboxEl.checked;
        toggleLandmark(cityName, landmarkName, isChecked);
        
        // Find and toggle card class
        const card = checkboxEl.closest(".landmark-checkbox-card");
        if (card) {
            if (isChecked) card.classList.add("checked");
            else card.classList.remove("checked");
        }

        // Update progress UI dynamically without full re-render
        const progress = getLandmarkProgress(cityName);
        
        const progressTextEl = document.getElementById("landmark-progress-text");
        const progressBarFillEl = document.getElementById("landmark-progress-bar-fill");
        
        if (progressTextEl) {
            progressTextEl.innerText = `${progress.checked} / ${progress.total} Durak (%${progress.pct})`;
        }
        if (progressBarFillEl) {
            progressBarFillEl.style.width = `${progress.pct}%`;
        }

        // Update lists in sidebar
        renderCitiesList(searchInput.value, regionSelect.value);
    };

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

    dashboardBtn.addEventListener("click", () => {
        renderDashboard();
    });

    logoSection.addEventListener("click", () => {
        renderDashboard();
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
    renderDashboard(); // Open dashboard by default on startup
});
