"""Test sample.py"""


class TestSample:
    """Test Sample"""

    def test_get_name(self):
        """Test get_name"""
        from sample import Sample

        sample: Sample = Sample("sample")
        assert sample.get_name() == "another"

    def test_print_name(self):
        """Test print_name"""
        pass
