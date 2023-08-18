"""Provides utilities and dependency injection for CHA₂DS₂-VASc score calculation."""
from typing import Literal

import pandas as pd

from schemas.chads_vasc_score import ChadsVascInput


def unpack_and_calc_cvs(cvs_data: ChadsVascInput) -> int:
    """Dependency inject for unpacking schema and calculating CHA₂DS₂-VASc score.

    Args:
        cvs_data: Input parameters for calculating CHA₂DS₂-VASc score.

    Returns:
        Calculated CHA₂DS₂-VASc score.
    """
    return _calculate_cvs(**cvs_data.model_dump())


def _calculate_cvs(
    age: int,
    biological_sex: Literal["male", "female", "intersex"],
    congestive_heart_failure: bool,
    hypertension: bool,
    stroke_tia: bool,
    vascular_disease: bool,
    diabetes: bool,
) -> int:
    """Calculates the CHA2DS2-VASc score based on input parameters.

    Args:
        age: Age of individual.
        biological_sex: Biological sex of individual.
        congestive_heart_failure: Whether individual presents with congestive heart failure.
        hypertension: Whether individual presents with  hypertension.
        stroke_tia: Whether individual presents with  experienced stroke/TIA.
        vascular_disease: Whether individual presents with  vascular disease.
        diabetes: Whether individual presents with diabetes.

    Returns:
        CHA2DS2-VASc score.
    """

    is_female = True if biological_sex == "female" else False
    score = (65 <= age < 75) + 2 * (age >= 75)
    score += (
        is_female
        + congestive_heart_failure
        + hypertension
        + 2 * stroke_tia
        + vascular_disease
        + diabetes
    )
    return score


# Interpretation table from https://pubmed.ncbi.nlm.nih.gov/22246443/

data = [
    [0, 0.2, 0.3],
    [1, 0.6, 0.9],
    [2, 2.2, 2.9],
    [3, 3.2, 4.6],
    [4, 4.8, 6.7],
    [5, 7.2, 10.0],
    [6, 9.7, 13.6],
    [7, 11.2, 15.7],
    [8, 10.8, 15.2],
    [9, 12.2, 17.4],
]

df = pd.DataFrame(
    data,
    columns=[
        "CHA₂DS₂-VASc Score",
        "Risk of Ischemic Stroke",
        "Risk of Stroke/TIA/Systemic Embolism",
    ],
)
