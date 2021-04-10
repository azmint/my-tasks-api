class TaskID(str):
    """タスクID"""

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}" + f"('{self}')"
