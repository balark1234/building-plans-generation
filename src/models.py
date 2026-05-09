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
