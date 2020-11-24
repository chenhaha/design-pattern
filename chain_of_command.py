# 责任链模式

import abc


class ISensitiveWordFilter(metaclass=abc.ABCMeta):
    def filter(string: str) -> str:
        pass


class RudeWordFilter(ISensitiveWordFilter):
    def filter(string: str) -> str:
        print("filter rule words")
        return string


class SexyWordFilter(ISensitiveWordFilter):
    def filter(string: str) -> str:
        print("filter sexy words")
        return string


class AdWordFilter(ISensitiveWordFilter):
    def filter(string: str) -> str:
        print("filter advertisement words")
        return string


class SensitiveWordFilterChain(object):
    # 包含过滤器的责任链
    def __init__(self) -> None:
        self.filters = []

    def add_filter(self, filter: ISensitiveWordFilter) -> None:
        self.filters.append(filter)

    def filter(self, string: str) -> str:
        for filter in self.filters:
            string = filter.filter(string)

        return string


chain = SensitiveWordFilterChain()
chain.add_filter(RudeWordFilter())
chain.add_filter(SexyWordFilter())
chain.add_filter(AdWordFilter())
sentence = "This sentence contains rude, sexy words and advertisement"
new_sentence = chain.filter(sentence)
