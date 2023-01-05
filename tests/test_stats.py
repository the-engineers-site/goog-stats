from unittest.mock import patch

import pytest
import goog_stats


@pytest.mark.parametrize(
    'text, expected'
)
def test_spacy(text, expected):
    detector = goog_stats.Stats()
    detector.enable_stat()
    assert detector.is_enabled() is True

@pytest.mark.parametrize(
    'text, expected'
)
def test_spacy_disable(text, expected):
    detector = goog_stats.Stats()
    detector.disable_stat()
    assert detector.is_enabled() is False
