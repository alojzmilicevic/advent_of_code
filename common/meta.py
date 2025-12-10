from year2019.metadata import get_metadata as meta2019
from year2021.metadata import get_metadata as meta2021
from year2022.metadata import get_metadata as meta2022
from year2025.metadata import get_metadata as meta2025

def get_metadata(year):
    if year == 2019:
        return meta2019()
    if year == 2021:
        return meta2021()
    if year == 2022:
        return meta2022()
    if year == 2025:
        return meta2025()
