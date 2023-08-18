"""Provides input and output schemas for calculating CHA₂DS₂-VASc score."""
from typing import Literal

from pydantic import BaseModel
from pydantic import Field


class ChadsVascInput(BaseModel):
    """Defines the input parameters for calculating CHA₂DS₂-VASc score."""

    age: int = Field(
        title="Age",
        ge=1,
        le=150,
        example=25,
        description="Age of individual.",
    )
    biological_sex: Literal["male", "female", "intersex"] = Field(
        title="Biological Sex",
        example="male",
        description="Biological sex of individual.",
    )
    congestive_heart_failure: bool = Field(
        title="Congestive Heart Failure",
        example=True,
        description="Whether individual presents with congestive heart failure.",
    )

    hypertension: bool = Field(
        title="Hypertension",
        example=True,
        description="Whether individual presents with  hypertension.",
    )
    stroke_tia: bool = Field(
        title="Stroke / TIA",
        example=True,
        description="Whether individual presents with  experienced stroke/TIA.",
    )
    vascular_disease: bool = Field(
        title="Vascular Disease",
        example=True,
        description="Whether individual presents with  vascular disease.",
    )
    diabetes: bool = Field(
        title="Diabetes",
        example=True,
        description="Whether individual presents with diabetes.",
    )


class ChadsVascScore(BaseModel):
    """Defines output for CHA₂DS₂-VASc score."""

    score: int = Field(
        title="CHA₂DS₂-VASc Score",
        example=1,
        description="CHA₂DS₂-VASc score for atrial fibrillation stroke risk.",
    )
