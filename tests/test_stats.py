from unittest.mock import patch

import pytest
import goog_stats


def test_spacy():
    detector = goog_stats.Stats("test")
    assert detector.is_enabled() is True


def test_spacy_disable():
    detector = goog_stats.Stats("test")
    detector.disable_stat()
    assert detector.is_enabled() is False


def test_disable_status_post_disable():
    detector = goog_stats.Stats("test")
    assert detector.is_enabled() is False


def test_enable_status_post_disable():
    detector = goog_stats.Stats("test")
    detector.enable_stat()
    assert detector.is_enabled() is True
