import pathlib
import abc
import re

import conversationalspacemapapp.Types.Data as Data
import conversationalspacemapapp.Types.Constants as Constants

class AbstractParser(abc.ABC):
    """
    Converts aTrain transcripts into a dictionary containing the data for a conversational space map.
    """

    def __init__(self, file: pathlib.Path) -> None:
        self._file = file
        self._content = self._read_file()
        self._map: [Data.Utterance] = self._convert_text()

    @property
    def file(self) -> pathlib.Path:
        return self._file

    @property
    def map(self) -> [Data.Utterance]:
        return sorted(self._map)

    @property
    def content(self) -> str:
        return self._content

    @property
    def participants(self) -> list:
        return sorted(list(set([utterance.speaker for utterance in self._map])))

    @abc.abstractmethod
    def number_of_words_by_speaker(self) -> [int, int]:
        raise NotImplementedError

    def _read_file(self) -> str:
        return self._file.read_text()

    def _clean_transcript(self) -> str:
        return self._content

    @abc.abstractmethod
    def _convert_text(self) -> dict[int:dict]:
        raise NotImplementedError

    @property
    def map_list(self) -> list[int]:
        """
        Return lists of words by utterance by speaker (only applies for two speakers), whereas the first speaker is the
        interviewer and the second speaker is the interviewee.
        """
        output = []
        for utterance in self._map:
            if utterance.number % 2 == 1:
                output.append(-utterance.words)
            else:
                output.append(utterance.words)
        return output


class TimestampCleanParser(AbstractParser):

    @property
    def number_of_words_by_speaker(self) -> [int, int]:
        return [
            abs(sum(self.map_list[::2])),
            abs(sum(self.map_list[1::2])),
        ]

    def _clean_transcript(self) -> str:
        cleaned_transcript = re.sub(r'\n\[.*?] ', '\n', self._content)
        cleaned_transcript = cleaned_transcript.replace("\n-", "")
        return cleaned_transcript

    def _convert_text(self) -> dict[int:dict]:
        self._content = self._clean_transcript()
        tokens = self._content.split("\n\n")
        output = []
        counter = 0
        for token in tokens:
            segments = token.split(" ")
            number_of_words = len(segments) - 1
            if number_of_words > 0:
                counter += 1
                output.append(
                    Data.Utterance(
                        number=counter,
                        speaker=segments[0],
                        words=number_of_words
                    )
                )
        return output
