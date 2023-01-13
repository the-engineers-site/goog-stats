from unittest.mock import patch

import pytest
import goog_stats


def test_spacy():
    detector = goog_stats.Stats("test")
    assert detector.is_enabled() is True

def test_spacy_disable():
    detector = goog_stats.Stats()
    detector.disable_stat()
    assert detector.is_enabled() is False
