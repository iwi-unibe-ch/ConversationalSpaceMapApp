from dataclasses import dataclass

import conversationalspacemapapp.Types.Constants as Constants

@dataclass
class Utterance:
    number: int
    speaker: str
    words: int

    def __lt__(self, other):
        return self.number < other.number