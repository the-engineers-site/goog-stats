from unittest.mock import patch

import pytest
import goog_stats


def test_spacy():
    detector = goog_stats.Stats("UA-148590293-1")
    detector.enable_stat()
    assert detector.is_enabled() is True
    detector.disable_stat()
    assert detector.is_enabled() is False

def test_spacy_disable():
    detector = goog_stats.Stats()
    detector.disable_stat()
    assert detector.is_enabled() is False
