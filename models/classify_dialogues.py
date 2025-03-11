from pydantic import BaseModel, Field
from typing import Literal, List, Optional

class StructuredResponse(BaseModel):
    response: Literal["yes", "no"] = Field(..., description="Structured output constrained to 'yes' or 'no'.")

class DatsetGrouper(BaseModel):
    professional_group: Optional[List[int]] = Field([], description = "A list of integer ids of professional dialogues")
    casual_group: Optional[List[int]] = Field([], description = "A list of integer ids of casual dialogues")


if __name__ == "__main__":
    try:
        result = DatsetGrouper(professional_group=[1,2,3,4], casual_group = [])  # ✅ Valid
        print(result)
        
        invalid_result = DatsetGrouper(professional_group=[])  # ❌ Raises validation error
    except Exception as e:
        print(f"Validation Error: {e}")