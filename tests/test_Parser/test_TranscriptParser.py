import pathlib
import unittest

import conversationalspacemapapp.Parser.TranscriptParser as TranscriptParser
import conversationalspacemapapp.Types.Data as Data
import conversationalspacemapapp.Types.Constants as Constants


class TestTranscriptParser(unittest.TestCase):
    # Unlimited return of error messages
    maxDiff = None

    # Timestamps cleaned up files (timestamp file without time brackets)
    path_short_transcript = pathlib.Path(__file__).parent / 'test_short_transcript/transcription_timestamps.txt'
    content_short_transcript = """Interviewer Ich habe noch nie so ein schlechtes Interview gesehen. Red jetzt nicht so klar, Mona.\n\nInterviewee Jetzt noch etwas nuscheln.\n\n"""
    path_long_transcript = pathlib.Path(__file__).parent / 'test_transcript/transcription_timestamps.txt'
    path_multiple_speaker_transcript = pathlib.Path(__file__).parent / 'test_transcript_multiple_speakers/transcription_timestamps.txt'

    # Define parser
    parser: TranscriptParser.AbstractParser

    @classmethod
    def setUpParser(cls, short=True, multiple_speaker=False):
        if multiple_speaker: # Long transcript with multiple speakers
            return TranscriptParser.TimestampCleanParser(file=TestTranscriptParser.path_multiple_speaker_transcript)
        elif short:
            return TranscriptParser.TimestampCleanParser(file=TestTranscriptParser.path_short_transcript)
        else:
            return TranscriptParser.TimestampCleanParser(file=TestTranscriptParser.path_long_transcript)

    def test_transcript_timestamp_short(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.content,
            TestTranscriptParser.content_short_transcript
        )

    def test_transcript_timestamp_map_short(self):
        parser = TestTranscriptParser.setUpParser()
        sut: [Data.Utterance] = parser.map
        utterance1, utterance2 = sut[0], sut[1]

        # Test first utterance
        self.assertEqual(utterance1.number, 1)
        self.assertEqual(utterance1.speaker, "Interviewer")
        self.assertEqual(utterance1.role, Constants.Participant.Undefined)
        self.assertEqual(utterance1.words, 15)

        # Test second utterance
        self.assertEqual(utterance2.number, 2)
        self.assertEqual(utterance2.speaker, "Interviewee")
        self.assertEqual(utterance2.role, Constants.Participant.Undefined)
        self.assertEqual(utterance2.words, 4)

    def test_transcript_timestamp_map_short_list(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.map_list,
            [-15, 4]
        )

    def test_transcript_timestamp_map_long(self):
        parser = TestTranscriptParser.setUpParser(short=False)
        sut: [Data.Utterance] = parser.map
        utterance1, utterance2, utterance3 = sut[0], sut[1], sut[2]

        # Test first utterance
        self.assertEqual(utterance1.number, 1)
        self.assertEqual(utterance1.speaker, "SPEAKER_00")
        self.assertEqual(utterance1.role, Constants.Participant.Undefined)
        self.assertEqual(utterance1.words, 26)

        # Test second utterance
        self.assertEqual(utterance2.number, 2)
        self.assertEqual(utterance2.speaker, "SPEAKER_01")
        self.assertEqual(utterance2.role, Constants.Participant.Undefined)
        self.assertEqual(utterance2.words, 31)

        # Test third utterance
        self.assertEqual(utterance3.number, 3)
        self.assertEqual(utterance3.speaker, "SPEAKER_00")
        self.assertEqual(utterance3.role, Constants.Participant.Undefined)
        self.assertEqual(utterance3.words, 2)

    def test_transcript_timestamp_map_long_list(self):
        parser = TestTranscriptParser.setUpParser(short=False)
        self.assertEqual(
            parser.map_list,
            [-26, 31, -2]
        )

    def test_transcript_timestamp_speaker_words_short(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.number_of_words_by_speaker,
            [15, 4]
        )

    def test_transcript_timestamp_speaker_words_long(self):
        parser = TestTranscriptParser.setUpParser(short=False)
        self.assertEqual(
            parser.number_of_words_by_speaker,
            [28, 31]
        )

    def test_transcript_timestamp_participants_short(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.participants,
            [
                "Interviewee", "Interviewer"
            ]
        )

    def test_transcript_timestamp_participants_multiple_speakers(self):
        parser = TestTranscriptParser.setUpParser(multiple_speaker=True)
        self.assertEqual(
            parser.participants,
            [
                "SPEAKER_00", "SPEAKER_01", "SPEAKER_02"
            ]
        )