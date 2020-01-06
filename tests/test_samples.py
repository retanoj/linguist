# -*- coding: utf-8 -*-

from .framework import LinguistTestBase, main
from linguist.libs.samples import DATA
from functools import reduce


class TestSamples(LinguistTestBase):

    def test_verify(self):
        data = DATA
        assert data['languages_total'] == sum(data['languages'].values())
        assert data['tokens_total'] == sum(data['language_tokens'].values())
        assert data['tokens_total'] == sum(reduce(lambda x, y: x + y,
                                                  [list(token.values()) for token in list(data['tokens'].values())]))

if __name__ == '__main__':
    main()
