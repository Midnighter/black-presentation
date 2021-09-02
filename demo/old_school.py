# -*- coding: utf-8 -*-


class ImPython2NewStyle(object):

    def __init__(self, first, second, **kwargs):
        """Initialize the demo class."""
        super(ImPython2NewStyle, self).__init__(**kwargs)
        self.first  = first
        self.second = second

    def get_tuple(self):
        return (
            "who",
                "would",
                    "do",
                        "such",
                            "a",
                                "thing",
                                    "?"
                                        )


if __name__ == '__main__':
    print ImPython2NewStyle(3, 4).get_tuple()
