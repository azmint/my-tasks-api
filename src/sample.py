"""Sample"""


class Sample:
    def __init__(self, name: str):
        self.name: str = name

    def get_name(self) -> str:
        """sample

        :return: name
        """
        return self.name

    def print_name(self):
        """print name"""
        print(self.name)
