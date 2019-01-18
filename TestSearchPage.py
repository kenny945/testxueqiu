# -*- coding=utf-8 -*-
import pytest

from Base import *
from driver import Driver


class TestSearch(object):


    mainPage  = None
    Dev = None
    #searchPage = None

    data_test_search=[
        ("pdd", u"拼多多"),
        ("alibaba", u"阿里巴巴")
    ]

    def setup_method(self, method):
        self.Dev = Driver()
        self.Dev.start()
        self.mainPage = MainPage(self.Dev.get_curr_driver())
        print("成功进入MainPage")


    @pytest.mark.parametrize("keyword, name", data_test_search)
    def test_search(self, keyword, name):
        searchPage = self.mainPage.goto_search()
        content = searchPage.search(keyword).get_all()[0];
        assert  content == name


    def teardown_method(self, method):
        self.Dev.stop()
