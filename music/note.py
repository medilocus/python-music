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

from .constants import *


class Note:
    """Class for a single note."""

    pitch: int
    type: int
    dots: int

    def __init__(self, pitch: int, type: int, dots: int = 0) -> None:
        """
        Initializes note.
        :param pitch: Integer pitch of note. The lowest note on piano is 21.
        :param type: Note length, defined in constants: music.NOTE_QUARTER, music.NOTE_HALF, ...
        """
        self.pitch = pitch
        self.type = type
        self.dots = dots

    @staticmethod
    def type_to_len(type: int) -> float:
        """
        Converts from a type (music.NOTE_QUARTER) to a length (1)
        :param type: Type of note.
        """
        if type == NOTE_QUARTER:
            return 1
        elif type == NOTE_HALF:
            return 2
        elif type == NOTE_WHOLE:
            return 4
        elif type == NOTE_DOUBLE_WHOLE:
            return 8
        elif type == NOTE_8TH:
            return 1 / 2
        elif type == NOTE_16TH:
            return 1 / 4
        elif type == NOTE_32TH:
            return 1 / 8
        elif type == NOTE_64TH:
            return 1 / 16

        raise ValueError(f"Note type {type} not implemented.")
