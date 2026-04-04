from __future__ import annotations

import pandas as pd
import pytest


@pytest.fixture
def heroes_before():
    return pd.DataFrame(
        [
            {"hero": "hulk", "power": "strength"},
            {"hero": "black_widow", "power": "spy"},
            {"hero": "thor", "hammers": 0},
        ]
    )


@pytest.fixture
def heroes_after():
    return pd.DataFrame(
        [
            {"hero": "hulk", "power": "smart"},
            {"hero": "captain marvel", "power": "strength"},
            {"hero": "thor", "hammers": 2},
        ]
    )
