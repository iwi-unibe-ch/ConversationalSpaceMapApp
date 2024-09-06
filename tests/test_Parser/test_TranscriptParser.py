import pathlib
import unittest

import conversationalspacemapapp.Parser.TranscriptParser as TranscriptParser


class TestTranscriptParser(unittest.TestCase):
    # Unlimited return of error messages
    maxDiff = None

    # Timestamps cleaned up files (timestamp file without time brackets)
    path_short_transcript_clean = pathlib.Path(__file__).parent / 'test_short_transcript/transcription_timestamps_clean.txt'
    content_short_transcript_clean = """SPEAKER_00 Ich habe noch nie so ein schlechtes Interview gesehen. Red jetzt nicht so klar, Mona.\n\nSPEAKER_01 Jetzt noch etwas nuscheln."""
    path_long_transcript_clean = pathlib.Path(__file__).parent / 'test_transcript/transcription_timestamps_clean.txt'

    # Define parser
    parser: TranscriptParser.AbstractParser

    @classmethod
    def setUpParser(cls, short=True):
        if short:
            return TranscriptParser.TimestampCleanParser(file=TestTranscriptParser.path_short_transcript_clean)
        else:
            return TranscriptParser.TimestampCleanParser(file=TestTranscriptParser.path_long_transcript_clean)

    def test_transcript_timestamp_clean_short(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.content,
            TestTranscriptParser.content_short_transcript_clean
        )

    def test_transcript_timestamp_clean_map_short(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.map,
            {
                1: {
                    "speaker": "SPEAKER_00",
                    "words": 15,
                },
                2: {
                    "speaker": "SPEAKER_01",
                    "words": 4,
                }
            }
        )

    def test_transcript_timestamp_clean_map_short_list(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.map_list,
            [-15, 4]
        )

    def test_transcript_timestamp_clean_map_long(self):
        parser = TestTranscriptParser.setUpParser(short=False)
        self.assertEqual(
            parser.map,
            {
                1: {'speaker': 'SPEAKER_00', 'words': 26},
                2: {'speaker': 'SPEAKER_01', 'words': 31},
                3: {'speaker': 'SPEAKER_00', 'words': 2}
            }
        )

    def test_transcript_timestamp_clean_map_long_list(self):
        parser = TestTranscriptParser.setUpParser(short=False)
        self.assertEqual(
            parser.map_list,
            [-26, 31, -2]
        )

    def test_transcript_timestamp_clean_speaker_words_short(self):
        parser = TestTranscriptParser.setUpParser()
        self.assertEqual(
            parser.number_of_words_by_speaker,
            [15, 4]
        )

    def test_transcript_timestamp_clean_speaker_words_long(self):
        parser = TestTranscriptParser.setUpParser(short=False)
        self.assertEqual(
            parser.number_of_words_by_speaker,
            [28, 31]
        )