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

## 🔄 How It Works

### 1. Input Collection
The user provides two types of information:

**A. Site Details**
- Address or location
- Plot dimensions (length × width)
- Any known constraints (slope, existing structures, orientation, etc.)

**B. Building Vision (Mind Map Style)**
- Number of stories (e.g., 2 stories, 3 stories, up to 5+ stories)
- Building type: Residential / Commercial / Mixed-use
- High-level layout preferences (e.g., open-plan living, multiple bedrooms, ground-floor retail, rooftop terrace)
- Elevation and style direction (modern, contemporary, traditional, specific roof form, materials)
- Any special requirements (EV charging, accessibility, sustainability goals, parking needs, etc.)

This combination acts like a **natural language project brief + structured parameters**.

### 2. Zoning Law Retrieval
The system identifies the municipality from the location and loads the relevant zoning regulations (setbacks, height limits, Floor Area Ratio, parking requirements, use restrictions, etc.).

### 3. Initial Plan Generation
An LLM agent creates a first draft of the building layout, massing, and key decisions, along with reasoning tied to the user’s vision and zoning rules.

### 4. Continuous Self-Correction Loop
The system runs a validation + revision cycle:
- A rule checker evaluates the current plan against all applicable zoning laws
- Any violations are fed back to the LLM with specific feedback
- The LLM revises the plan
- This loop continues until the plan is compliant or a maximum iteration limit is reached

### 5. Visualization & Output
Once compliant:
- **Matplotlib** generates clean, professional 2D drawings:
  - Site plan with setbacks and building footprint
  - Floor plans for each level
  - Elevation views (simple)
- Optional: Image generation models create more realistic conceptual renders
- A **Compliance Report** is produced explaining how the plan meets zoning requirements.

## 🛠️ Proposed Tech Stack

| Component              | Technology                              | Purpose                                      |
|------------------------|-----------------------------------------|----------------------------------------------|
| Core Language          | Python 3.11+                            | Main application logic                       |
| Agent Framework        | LangGraph (or CrewAI / LangChain)       | Building the self-correction loop            |
| LLM                    | OpenAI / Anthropic / Grok               | Plan generation + iterative fixing           |
| Visualization          | Matplotlib + Pillow                     | 2D architectural drawings                    |
| Image Generation       | Grok Imagine / Stable Diffusion API     | Optional photorealistic concept images       |
| User Interface (v2)    | Streamlit or Gradio                     | Web interface for input and results          |
| Zoning Data            | JSON + optional vector database         | Storing and retrieving municipal zoning laws |

## 🚀 Getting Started (Planned)

```bash
git clone https://github.com/balark1234/building-plans-generation.git
cd building-plans-generation
pip install -r requirements.txt
```

Example run (future):
```bash
python main.py --location "Austin, TX" --dimensions "60x90" --stories 3 --type residential
```

## 📁 Planned Project Structure

```
building-plans-generation/
├── src/
│   ├── agents/              # LLM agents and self-correction loop
│   ├── zoning/              # Zoning law loader + validator
│   ├── visualization/       # Matplotlib plan generators
│   ├── inputs/              # Input parsing (site + vision)
│   └── utils/
├── data/
│   └── zoning_laws/         # Sample zoning rules per city
├── examples/
├── tests/
├── app.py                   # Future web UI
├── main.py
├── requirements.txt
└── README.md
```

## 🗺️ Roadmap

- [x] Repository created
- [ ] Core input models (Site + Building Vision)
- [ ] LLM self-correction loop with zoning validation
- [ ] Matplotlib-based 2D plan visualizer
- [ ] Support for 2–3 sample cities’ zoning laws
- [ ] Streamlit web interface
- [ ] Integration with image generation models
- [ ] PDF export + compliance report generation
