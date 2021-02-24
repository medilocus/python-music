#
#  Python-music
#  Python music module.
#  Copyright Medilocus 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# Script to generate constants.py

import os

constants = (
    "BLACK",
    "WHITE",

    "L_DOUBLE_WHOLE",
    "L_WHOLE",
    "L_HALF",
    "L_QUARTER",
    "L_8TH",
    "L_16TH",
    "L_32TH",
    "L_64TH",

    "NATURAL",
    "SHARP",
    "DOUBLE_SHARP",
    "FLAT",
    "DOUBLE_FLAT",

    "N_A",
    "N_B",
    "N_C",
    "N_D",
    "N_E",
    "N_F",
    "N_G",

    "N_OCT0",
    "N_OCT1",
    "N_OCT2",
    "N_OCT3",
    "N_OCT4",
    "N_OCT5",
    "N_OCT6",
    "N_OCT7",
    "N_OCT8",
    "N_OCT9",
)

consts_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "constants.py")

with open(os.path.realpath(__file__), "r") as file:
    gpl = "".join([file.readline() for i in range(18)])

with open(consts_path, "w") as file:
    file.write(gpl)
    file.write("\n\n")
    for i, c in enumerate(constants):
        file.write(f"{c}: int = {i}\n")
