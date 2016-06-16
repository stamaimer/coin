# -*- coding: utf-8 -*-

import unittest

from coin import coin


class CoinTestCase(unittest.TestCase):

    def setUp(self):

        self.coin = coin.test_client()

        with coin.app_context():

            pass

    def tearDown(self):

        pass

    def login(self, username, password):

        return self.coin.post("/login", data=dict(
            username=username,
            password=password), follow_redirects=True)

    def logout(self):

        return self.coin.get("/logout", follow_redirects=True)
