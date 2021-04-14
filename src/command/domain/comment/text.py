from dataclasses import dataclass


@dataclass(frozen=True)
class Text:
    """文章"""

    value: str
