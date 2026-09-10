# CINEMAIF-v2 — UI/UX Design System Specification & Redesign Plan

**Target Architecture:** Django Web Application (Templates + Static Assets)

**Design Reference:** Premium Streaming Aesthetics (Disney+ dynamic layouts & ambient lighting, Netflix content organization)

**Theme Strategy:** Deep Space Blue (`#040714`) & Radiant Warm Gold (`#FFB800` / `#FFC700`) Gradients

**Strict Directives:** Zero Emojis, Clean Glassmorphism, Dynamic Micro-interactions, High-density Responsive Carousels

---

## 1. Vision & Core Principles

The goal of **CINEMAIF-v2** is to elevate the platform into a visually captivating, content-first cinematic environment. Drawing heavy design language from high-end streaming platforms like Disney+ and Netflix, the interface relies on deep dark backdrops, ambient gradient glows, glassmorphism UI overlays, and rich horizontal media carousels.

### Core Design Pillars

1. **Cinematic Canvas:** Deep space navy and slate black surfaces that make movie poster artwork, backdrop images, and video teasers pop off the screen.
2. **Gold & Cyan High Contrast:** Functional accents using rich warm gold gradients for primary actions (play, subscribe, highlight) and vibrant cyan-blue gradients for secondary highlights and interactive states.
3. **Dynamic Home Catalog:** A fluid home screen featuring rich hero banners, recent uploads, and automatically generated content carousels grouped by genres, categories, and viewing state.
4. **Precision Typography & Structure:** High-contrast sans-serif typography paired with rigid structural grids, rounded container boundaries (`12px` border-radius), and layered lighting effects.
5. **Zero Visual Noise (No Emojis):** Strictly **no emojis**, informal emoticons, or decorative text symbols anywhere in the interface. All iconography must be vector SVG glyphs (Lucide/Feather stroke family).

---

## 2. Color Palette & Gradient Systems

The color architecture is built around deep dark backgrounds paired with luminous gradients. Primary structural elements inhabit dark blue tones, while key interaction points utilize intense gold-yellow gradients.

### 2.1 Color Tokens & Variables

```css
:root {
  /* Core Canvas & Surfaces */
  --bg-canvas:             #040714;
  --bg-surface-primary:    #090E25;
  --bg-surface-secondary:  #101835;
  --bg-surface-tertiary:   #182449;
  --bg-glass:              rgba(16, 24, 53, 0.75);
  --bg-glass-card:         rgba(255, 255, 255, 0.04);
  
  /* Brand Blue Palette */
  --color-brand-blue-900: #040714;
  --color-brand-blue-800: #0B132B;
  --color-brand-blue-700: #111D4A;
  --color-brand-blue-600: #1C2D6B;
  --color-brand-blue-500: #2541B2;
  --color-brand-blue-400: #0072FF;
  --color-brand-blue-300: #00C6FF;

  /* Accent Gold & Amber Palette */
  --color-accent-gold-500: #FF9900;
  --color-accent-gold-400: #FFB800;
  --color-accent-gold-300: #FFC700;
  --color-accent-gold-200: #FFE169;
  --color-accent-amber:    #F59E0B;

  /* Neutrals & Text */
  --text-primary:          #FFFFFF;
  --text-secondary:        #9CA3AF;
  --text-muted:            #6B7280;
  --text-inverse:          #040714;
  
  /* Borders & Highlights */
  --border-subtle:         rgba(255, 255, 255, 0.08);
  --border-medium:         rgba(255, 255, 255, 0.16);
  --border-active:         rgba(0, 198, 255, 0.6);
  --border-gold-active:    rgba(255, 184, 0, 0.8);

  /* Functional Status */
  --status-success:        #10B981;
  --status-warning:        #F59E0B;
  --status-error:          #EF4444;
  --status-info:           #3B82F6;

  /* Cinema Gradients */
  --gradient-hero-overlay: linear-gradient(180deg, rgba(4,7,20,0) 0%, rgba(4,7,20,0.6) 50%, #040714 100%),
                           linear-gradient(90deg, #040714 0%, rgba(4,7,20,0.7) 45%, transparent 100%);
  --gradient-brand-blue:   linear-gradient(135deg, #0072FF 0%, #00C6FF 100%);
  --gradient-gold-primary:  linear-gradient(135deg, #FF9900 0%, #FFB800 50%, #FFE169 100%);
  --gradient-gold-hover:    linear-gradient(135deg, #FFB800 0%, #FFE169 100%);
  --gradient-card-overlay: linear-gradient(180deg, rgba(4,7,20,0) 20%, rgba(4,7,20,0.95) 100%);
  --gradient-ambient-glow: radial-gradient(circle at top right, rgba(0, 114, 255, 0.15), transparent 60%),
                           radial-gradient(circle at top left, rgba(255, 184, 0, 0.1), transparent 50%);

  /* Shadows & Glows */
  --shadow-sm:             0 2px 8px rgba(0, 0, 0, 0.5);
  --shadow-lg:             0 12px 32px rgba(0, 0, 0, 0.8);
  --glow-blue:             0 0 25px rgba(0, 198, 255, 0.4);
  --glow-gold:             0 0 25px rgba(255, 184, 0, 0.4);
}
```

---

## 3. Typography Hierarchy

Typography utilizes clean modern sans-serif typefaces with defined weights to guarantee legibility across all screen sizes.

### 3.1 Font Families

* **Primary Sans-Serif:** `'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif`
* **Display / Headings:** `'Outfit', 'Plus Jakarta Sans', sans-serif`
* **Monospace:** `'JetBrains Mono', monospace`

### 3.2 Type Rules

| Element | Font Size | Line Height | Weight | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Hero Title** | `3.5rem` (56px) | 1.1 | 800 | Main Hero banner movie titles |
| **H1 Title** | `2.25rem` (36px) | 1.2 | 700 | Detail page main titles, page headers |
| **Carousel Title**| `1.5rem` (24px) | 1.3 | 700 | Section and category row headings |
| **Card Title** | `1rem` (16px) | 1.4 | 600 | Movie poster titles on hover/modal |
| **Body Text** | `1rem` (16px) | 1.6 | 400 | Synopsis, paragraphs, main descriptions |
| **Meta Info** | `0.875rem` (14px)| 1.4 | 500 | Movie duration, release year, genre tags |
| **Badge / Label** | `0.75rem` (12px) | 1.2 | 700 | HD, 4K, Age ratings, Category pills |

---

## 4. Home Screen Catalog & Layout Architecture

The main catalog page is modeled after Disney+ and Netflix, acting as the central hub for video discovery.

```
+-------------------------------------------------------------------------------+
| [LOGO] CINEMAIF    Início   Filmes   Séries   Categorias    [Busca]  (Perfil) |  <-- Glass Navbar
+-------------------------------------------------------------------------------+
|                                                                               |
|                            HERO SPOTLIGHT BANNER                              |
|           [ Destaque Principal: Filme / Série em Alta ]                        |
|           Sino do filme + Meta Tags + Botões: [ ASSISTIR ] [ MAIS INFO ]      |
|                                                                               |
+-------------------------------------------------------------------------------+
|  PROMO / BRAND TILES                                                          |
|  [ Disney+ Style Glass Category Cards: Ação, Sci-Fi, Animação, Originais ]    |
+-------------------------------------------------------------------------------+
|                                                                               |
|  Recém-Adicionados (Lançamentos Recentes)                     [Ver Todos >]   |
|  < [Card 1]  [Card 2]  [Card 3]  [Card 4]  [Card 5]  [Card 6] >               |
|                                                                               |
|  Continuar Assistindo                                                         |
|  < [Card Progress 1]  [Card Progress 2]  [Card Progress 3] >                  |
|                                                                               |
|  Ação & Aventura (Gerado Automaticamente por Categoria)        [Ver Todos >]   |
|  < [Card 1]  [Card 2]  [Card 3]  [Card 4]  [Card 5]  [Card 6] >               |
|                                                                               |
|  Ficção Científica (Gerado Automaticamente por Categoria)     [Ver Todos >]   |
|  < [Card 1]  [Card 2]  [Card 3]  [Card 4]  [Card 5]  [Card 6] >               |
|                                                                               |
+-------------------------------------------------------------------------------+
|  Footer CINEMAIF — Direitos Reservados                                   2026 |
+-------------------------------------------------------------------------------+
```

### 4.1 Home Screen Structure & Dynamic Logic

1. **Hero Spotlight Banner (Top Page):**
   * Displays the top featured or newest release.
   * Background features full-width backdrop imagery with dynamic gradient overlays on the bottom and left edges (`var(--gradient-hero-overlay)`).
   * Displays title, synopsis excerpt, resolution badge (4K, HD), release year, and actionable CTA buttons (Watch Now, Details).

2. **Quick Brand / Category Navigation Bar:**
   * Horizontal row of interactive glass tiles right below the hero.
   * Clicking a tile filters or scrolls directly to a specific category/genre.

3. **Dynamic Carousel Engine (Auto-Generated via Django Backend):**
   * **Row 1: Recém-Adicionados (Recent Releases):** Automatically populated using Django ORM querying the newest added movies (`Movie.objects.order_by('-created_at')[:15]`).
   * **Row 2: Continuar Assistindo (Continue Watching):** Shows movies the logged-in user started watching, complete with a gold progress bar on the card base.
   * **Rows 3+: Auto-Generated Category Carousels:** Django template loops through all active categories/genres in the database (`{% for category in categories %}`). For each category with available movies, a dedicated carousel row is constructed dynamically (`category.movies.all`).

---

## 5. UI Component Specifications

### 5.1 Movie Cards & Poster Elements

Movie cards support two primary formats: **Vertical Posters (2:3 aspect ratio)** for traditional catalog rows, and **Horizontal Backdrops (16:9 aspect ratio)** for "Continue Watching" or "Trending" rows.

#### Vertical Card CSS Architecture

```css
.movie-card {
  position: relative;
  aspect-ratio: 2 / 3;
  border-radius: 12px;
  overflow: hidden;
  background-color: var(--bg-surface-secondary);
  border: 1px solid var(--border-subtle);
  transition: transform 0.35s cubic-bezier(0.25, 1, 0.5, 1),
              box-shadow 0.35s cubic-bezier(0.25, 1, 0.5, 1),
              border-color 0.35s cubic-bezier(0.25, 1, 0.5, 1);
  cursor: pointer;
}

.movie-card:hover {
  transform: scale(1.06) translateY(-6px);
  border-color: var(--color-brand-blue-300);
  box-shadow: var(--glow-blue), var(--shadow-lg);
  z-index: 10;
}

.movie-card-overlay {
  position: absolute;
  inset: 0;
  background: var(--gradient-card-overlay);
  opacity: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 1rem;
  transition: opacity 0.3s ease;
}

.movie-card:hover .movie-card-overlay {
  opacity: 1;
}
```

### 5.2 Dynamic Horizontal Carousel Component

Carousels feature smooth horizontal scrolling with glass directional control buttons (Previous / Next).

* **Scroll Behavior:** Smooth native momentum scrolling (`scroll-behavior: smooth`) paired with flexbox row layout (`display: flex; gap: 1.25rem; overflow-x: auto`).
* **Scrollbars:** Custom slim scrollbar styled in dark slate and gold accent on hover, or hidden for a touch-native feel.
* **Control Buttons:** Floating glassmorphic arrow controls using SVG vectors (`chevron-left`, `chevron-right`).

### 5.3 Button Systems

#### Primary Gold Action Button

```css
.btn-primary-gold {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  background: var(--gradient-gold-primary);
  color: var(--text-inverse);
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 700;
  font-size: 0.95rem;
  letter-spacing: 0.03em;
  padding: 0.85rem 2rem;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(255, 184, 0, 0.3);
  transition: all 0.25s ease-in-out;
}

.btn-primary-gold:hover {
  background: var(--gradient-gold-hover);
  transform: translateY(-2px);
  box-shadow: var(--glow-gold);
}
```

#### Secondary Glass Action Button

```css
.btn-secondary-glass {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(255, 255, 255, 0.08);
  color: var(--text-primary);
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.85rem 2rem;
  border-radius: 8px;
  border: 1px solid var(--border-medium);
  backdrop-filter: blur(12px);
  transition: all 0.25s ease-in-out;
}

.btn-secondary-glass:hover {
  background: rgba(255, 255, 255, 0.18);
  border-color: var(--color-brand-blue-300);
  transform: translateY(-2px);
}
```

---

## 6. Django Template Integration Strategy

To ensure seamless automatic category carousels and consistent theme application, Django views pass context to modular templates.

### 6.1 Home Screen Template Structure (`templates/home.html`)

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}CINEMAIF — Início{% endblock %}

{% block content %}
  <!-- Hero Banner -->
  {% include 'components/hero_banner.html' with movie=featured_movie %}

  <!-- Category Quick Links -->
  {% include 'components/category_bar.html' %}

  <!-- Main Content Carousels Container -->
  <div class="catalog-container space-y-10 py-8 px-6 lg:px-16">

    <!-- Recent Releases Carousel -->
    {% if recent_movies %}
      {% include 'components/carousel_row.html' with title="Recém-Adicionados" movies=recent_movies %}
    {% endif %}

    <!-- Continue Watching Carousel (For Authenticated Users) -->
    {% if user.is_authenticated and continue_watching %}
      {% include 'components/carousel_row.html' with title="Continuar Assistindo" movies=continue_watching is_progress=True %}
    {% endif %}

    <!-- Auto-Generated Genre / Category Carousels -->
    {% for category in categories %}
      {% if category.movies.all %}
        {% include 'components/carousel_row.html' with title=category.name movies=category.movies.all %}
      {% endif %}
    {% endfor %}

  </div>
{% endblock %}
```

---

## 7. Zero Emoji Policy & Vector Icon Strategy

To ensure a clean, modern aesthetic, **emojis are strictly prohibited** across all interface labels, error messages, navigation links, and dynamic titles.

### Permitted Iconography (Pure Vector SVG)

Icons must utilize crisp SVG vectors with uniform stroke widths (`2px`), scaling dynamically with CSS `currentColor`.

#### Example Standard SVG Usage:

```html
<!-- Play Icon SVG -->
<button class="btn-primary-gold">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
    <polygon points="5 3 19 12 5 21 5 3"></polygon>
  </svg>
  <span>ASSISTIR AGORA</span>
</button>

<!-- Info Icon SVG -->
<button class="btn-secondary-glass">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="10"></circle>
    <line x1="12" y1="16" x2="12" y2="12"></line>
    <line x1="12" y1="8" x2="12.01" y2="8"></line>
  </svg>
  <span>MAIS INFORMAÇÕES</span>
</button>
```

---

## 8. Refactoring Execution Checklist

1. **Static Stylesheet setup:** Create `static/css/cinemaif-v2.css` containing all root color variables, glassmorphism resets, custom scrollbars, and button rules.
2. **Layout Overhaul:** Update `base.html`, `navbar.html`, and `footer.html` with deep space background colors and frosted glass header elements.
3. **Carousel Component Modularization:** Create `components/carousel_row.html` and `components/movie_card.html` to standardize movie item rendering.
4. **Django Views Update:** Ensure the index/home view passes `featured_movie`, `recent_movies`, and `categories` (with prefetched movies) to `home.html`.
5. **Interactive Fine-Tuning:** Add smooth hover transitions, glow effects, and responsive carousel scroll controls.