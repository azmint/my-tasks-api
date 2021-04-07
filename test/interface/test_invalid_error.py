class TestInvalidDetail:
    def test___repr__(self):
        from interface.invalid_error import InvalidDetail

        item_name = "sample_item_name"
        message = "sample message."
        detail: InvalidDetail = InvalidDetail(item_name, message)
        result: str = detail.__repr__()
        assert (
            result
            == f"{InvalidDetail.__module__}.{InvalidDetail.__qualname__}({item_name}, {message})"
        )
