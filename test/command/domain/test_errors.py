from typing import Dict, Any

import pytest


class TestBaseError:
    """BaseErrorのテスト"""

    def test___repr__(self):
        """__repr__のテスト"""
        from command.domain.errors import BaseError

        try:
            var = 1 / 0
            pytest.fail("not raised.")
        except ZeroDivisionError as e:
            message: str = "sample message."
            values: Dict[str, Any] = {"reference item": "reference value"}
            error: BaseError = BaseError(message, values, e)
            result: str = error.__repr__()
            module_name: str = error.__module__
            qualified_name: str = error.__class__.__qualname__
            assert result == f"{module_name}.{qualified_name}({message}, {values}, {e})"
