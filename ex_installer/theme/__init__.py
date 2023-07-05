"""
Set up theme

© 2023, Peter Cole. All rights reserved.

This file is part of EX-Installer.

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

It is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CommandStation.  If not, see <https://www.gnu.org/licenses/>.
"""

from pathlib import Path
import sys

try:
    THEME_PATH = Path(sys._MEIPASS) / "theme"
except Exception:
    if getattr(sys, "frozen", False):
        THEME_PATH = Path(sys.executable).parent / "theme"
    else:
        THEME_PATH = Path(__file__).parent

"""DCC-EX theme"""
DCC_EX_THEME = THEME_PATH / "dcc-ex-theme.json"
