from pydantic import BaseModel, Field
from typing import Optional, List


class Site(BaseModel):
    """Represents the physical site/plot details."""
    address: str
    length: float
    width: float
    orientation: Optional[str] = None
    slope: Optional[str] = None
    existing_structures: bool = False
    constraints: List[str] = Field(default_factory=list)
    
    # Extra site-specific information
    additional_info: Optional[str] = None


class BuildingVision(BaseModel):
    """Represents the user's desired building vision / mind map."""
    number_of_stories: int
    building_type: str
    desired_layout: Optional[str] = None
    architectural_style: Optional[str] = None
    special_requirements: List[str] = Field(default_factory=list)
    description: Optional[str] = None

    # Area-related requirements
    expected_built_up_area_per_floor: Optional[float] = None
    total_carpet_area: Optional[float] = None
    total_built_up_area: Optional[float] = None
