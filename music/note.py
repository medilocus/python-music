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
    note_type: int
    dots: int

    def __init__(self, pitch: int, note_type: int = NOTE_QUARTER, dots: int = 0) -> None:
        """
        Initializes note.
        :param pitch: Integer pitch of note. The lowest note on piano is 21.
        :param note_type: Note length, defined in constants: music.NOTE_QUARTER, music.NOTE_HALF, ...
        """
        self.pitch = pitch
        self.note_type = note_type
        self.dots = dots

    @staticmethod
    def type_to_len(note_type: int) -> float:
        """
        Converts from a type (music.NOTE_QUARTER) to a length (1)
        :param note_type: Type of note.
        """
        if note_type == NOTE_QUARTER:
            return 1
        elif note_type == NOTE_HALF:
            return 2
        elif note_type == NOTE_WHOLE:
            return 4
        elif note_type == NOTE_DOUBLE_WHOLE:
            return 8
        elif note_type == NOTE_8TH:
            return 1 / 2
        elif note_type == NOTE_16TH:
            return 1 / 4
        elif note_type == NOTE_32TH:
            return 1 / 8
        elif note_type == NOTE_64TH:
            return 1 / 16

        raise TypeError(f"Note type {note_type} not implemented.")

    @staticmethod
    def type_to_name(note_type: int) -> str:
        """
        Converts from a type (music.NOTE_QUARTER) to a name ("Quarter")
        :param note_type: Type of note.
        """
        if note_type == NOTE_QUARTER:
            return "Quarter"
        elif note_type == NOTE_HALF:
            return "Half"
        elif note_type == NOTE_WHOLE:
            return "Whole"
        elif note_type == NOTE_DOUBLE_WHOLE:
            return "Double Whole"
        elif note_type == NOTE_8TH:
            return "8th"
        elif note_type == NOTE_16TH:
            return "16th"
        elif note_type == NOTE_32TH:
            return "32nd"
        elif note_type == NOTE_64TH:
            return "64th"

        raise ValueError(f"Note type {note_type} not implemented.")

    def base_length(self):
        """
        Returns this note's length without any dots.
        """
        return Note.type_to_len(self.note_type)

    def total_length(self):
        """
        Returns this note's total length (with dots).
        """
        length = self.base_length()
        add_len = length / 2
        for i in range(self.dots):
            length += add_len
            add_len /= 2
        return length
