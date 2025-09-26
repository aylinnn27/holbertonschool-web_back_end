#!/usr/bin/env python3
"""
Unit tests for utils.memoize
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test class for the memoize decorator"""

    def test_memoize(self):
        """Test that a_method is only called once when using @memoize"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            result1 = test_obj.a_property   # no ()
            result2 = test_obj.a_property   # no ()

            # Both results should be correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # a_method should only be called once due to memoization
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
