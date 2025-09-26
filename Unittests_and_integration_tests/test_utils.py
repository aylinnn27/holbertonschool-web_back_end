#!/usr/bin/env python3
"""
Unit tests for utils.memoize.
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test class for the memoize decorator."""

    def test_memoize(self):
        """Test that a_method is only called once with @memoize."""

        class TestClass:
            """Test class with a method and a memoized property."""

            def a_method(self):
                """Return a fixed integer.""
