from src.models import Site, BuildingVision


def build_initial_prompt(site: Site, vision: BuildingVision) -> str:
    """
    Creates a well-structured prompt for the LLM using 
    Site and BuildingVision data. Designed for better 
    reasoning and structured output.
    """
    prompt = f"""You are an expert architect and zoning compliance specialist.

Your task is to generate a **compliant building concept** based on the site details and user requirements below.

### SITE DETAILS:
- Location: {site.address}
- Plot Dimensions: {site.length} ft × {site.width} ft
- Orientation: {site.orientation or 'Not specified'}
- Topography: {site.slope or 'Flat'}
- Additional Information: {site.additional_info or 'None'}
- Known Constraints: {', '.join(site.constraints) if site.constraints else 'None'}

### USER REQUIREMENTS (Building Vision):
- Number of Stories: {vision.number_of_stories}
- Building Type: {vision.building_type}
- Desired Layout: {vision.desired_layout or 'Not specified'}
- Architectural Style: {vision.architectural_style or 'Modern'}
- Special Requirements: {', '.join(vision.special_requirements) if vision.special_requirements else 'None'}
- Expected Built-up Area per Floor: {vision.expected_built_up_area_per_floor or 'Flexible'} sq ft
- Total Carpet Area Target: {vision.total_carpet_area or 'Flexible'} sq ft

### INSTRUCTIONS:
1. Respect all site constraints and zoning regulations for the given location.
2. Balance the user's vision with practical and legal feasibility.
3. Think step by step before proposing a solution.
4. Clearly explain your reasoning.
5. Structure your response with the following sections:
   - **Concept Summary**
   - **Site Analysis & Zoning Considerations**
   - **Proposed Building Layout**
   - **Compliance Notes**
   - **Suggestions for Improvement** (if any)

Be precise and realistic.
"""
    return prompt.strip()
