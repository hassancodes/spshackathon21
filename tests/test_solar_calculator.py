import sys
from types import SimpleNamespace
import pytest
from unittest.mock import patch

sys.modules.setdefault("matplotlib", SimpleNamespace(pyplot=SimpleNamespace()))
sys.modules.setdefault("matplotlib.pyplot", sys.modules["matplotlib"].pyplot)

from src.core.solar_calculator import SolarDataCalculator


def test_calculate_average_power():
    sample_data = {
        "properties": {
            "parameter": {
                "PS": {
                    "JAN": 100,
                    "FEB": 200,
                    "MAR": 300,
                    "APR": 400,
                    "MAY": 500,
                    "JUN": 600,
                    "JUL": 700,
                    "AUG": 800,
                    "SEP": 900,
                    "OCT": 1000,
                    "NOV": 1100,
                    "DEC": 1200,
                }
            }
        }
    }
    expected_average = sum(sample_data["properties"]["parameter"]["PS"].values()) / 12

    with patch.object(SolarDataCalculator, "fetch_data", return_value=sample_data):
        calculator = SolarDataCalculator()
        result = calculator.calculate_average_power()
        assert result == expected_average
