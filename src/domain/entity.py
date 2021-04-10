from dataclasses import dataclass, field


@dataclass
class Entity:
    """エンティティ"""

    id: str = field(compare=True)

    def __setattr__(self, name, value):
        if name == "id" and hasattr(self, name):
            raise SystemError()

        super().__setattr__(name, value)
