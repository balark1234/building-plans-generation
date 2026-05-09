# 🏗️ Building Plans Generation

AI-powered application that generates compliant building plans from site details and user vision, while automatically respecting local municipal zoning laws.

## 📖 Overview

This project creates an intelligent system that turns your site information and building vision into compliant architectural plans.

**Core Idea:**
- You describe the **site** + your **desired building concept** (stories, type, style, layout ideas)
- The system retrieves relevant **zoning laws**
- An LLM generates plans in a **continuous self-correction loop** until they are fully compliant
- Finally, it produces clean visual building plans using matplotlib (and optionally image generation models)

## ✨ Key Features

- **Rich Input Support**:
  - Site details (dimensions, location, address)
  - Building vision / mind map:
    - Number of stories (e.g. 2 stories, 5 stories)
    - Building type (residential, commercial, mixed-use)
    - Desired layout and functional zones
    - Elevation / architectural style preferences
    - Special requirements (sustainability, accessibility, parking, etc.)
- **Automatic Zoning Compliance**: Integrates local municipal zoning laws for the given location
- **LLM Self-Correction Loop**: Iterative validation and revision until the plan passes all zoning rules
- **Visual Output**:
  - Professional 2D floor plans and site plans using matplotlib
  - Option for more realistic renders via image generation models
- **Compliance Report**: Clear breakdown of how the final plan satisfies (or still violates) zoning regulations
- **Extensible**: Easy to add support for new cities and zoning rule sets