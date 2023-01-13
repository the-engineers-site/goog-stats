from unittest.mock import patch

import pytest
from goog_stats import Stats


def test_reset_env():
    Stats.reset()


def test_init_exception():
    try:
        Stats()
    except Exception as e:
        assert e.__str__() == 'tid mandatory for starting collection'


def test_default_enable():
    detector = Stats("UA-148590293-1")
    assert detector.is_enabled() is True


def test_reset_pref():
    detector = Stats()
    assert detector.is_enabled() is True
    detector.disable_stat()
    assert detector.is_enabled() is False
    detector = Stats("UA-148590293-1", reset_pref=True)
    assert detector.is_enabled() is True


def test_spacy_disable():
    detector = Stats()
    detector.disable_stat()
    assert detector.is_enabled() is False


def test_disable_status_post_disable():
    detector = Stats()
    assert detector.is_enabled() is False


def test_enable_status_post_disable():
    detector = Stats()
    detector.enable_stat()
    assert detector.is_enabled() is True


def test_collect_stats():
    detector = Stats()
    detector.enable_stat()
    resp = detector.record_event("/unit-test", "test case test_collect_stats")
    assert resp.status_code is 200


def test_record_status():
    detector = Stats()
    detector.disable_stat()
    response = detector.record_event("/access-page", "user tried to access page which named test")
    assert response == 'collection disabled'
