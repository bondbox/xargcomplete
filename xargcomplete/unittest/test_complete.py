# coding:utf-8

import unittest
from unittest import mock

from xargcomplete import complete


class TestBash(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch.object(complete.os.path, "exists", mock.MagicMock(side_effect=[True]))  # noqa:E501
    @mock.patch.object(complete, "open")
    def test_enable(self, mock_open):
        with mock.mock_open(mock_open, read_data=complete.Bash.COMPLETION_CODE):  # noqa:E501
            self.assertIsNone(complete.Bash.enable())

    @mock.patch.object(complete.os.path, "exists", mock.MagicMock(side_effect=[False]))  # noqa:E501
    @mock.patch.object(complete.os, "makedirs", mock.MagicMock())
    @mock.patch.object(complete, "open")
    def test_enable_skip(self, mock_open):
        with mock.mock_open(mock_open, read_data=""):
            self.assertIsNone(complete.Bash.enable())

    @mock.patch.object(complete.os.path, "exists", mock.MagicMock(side_effect=[False]))  # noqa:E501
    @mock.patch.object(complete.os.path, "isfile", mock.MagicMock(side_effect=[True]))  # noqa:E501
    @mock.patch.object(complete.os, "remove", mock.MagicMock())
    def test_remove_success(self):
        self.assertTrue(complete.Bash.remove("test"))

    @mock.patch.object(complete.os.path, "exists", mock.MagicMock(side_effect=[True]))  # noqa:E501
    @mock.patch.object(complete.os.path, "isfile", mock.MagicMock(side_effect=[True]))  # noqa:E501
    @mock.patch.object(complete.os, "remove", mock.MagicMock())
    def test_remove_failure(self):
        self.assertFalse(complete.Bash.remove("test"))

    @mock.patch.object(complete.os, "listdir", mock.MagicMock(side_effect=[["test"]]))  # noqa:E501
    @mock.patch.object(complete.os.path, "exists", mock.MagicMock(side_effect=[True]))  # noqa:E501
    @mock.patch.object(complete.os.path, "isfile", mock.MagicMock(return_value=False))  # noqa:E501
    def test_list_null(self):
        self.assertEqual(complete.Bash.list(), set())

    @mock.patch.object(complete.os, "listdir", mock.MagicMock(side_effect=[[f"{complete.__project__}-78737973"]]))  # noqa:E501
    @mock.patch.object(complete.os.path, "exists", mock.MagicMock(side_effect=[False]))  # noqa:E501
    @mock.patch.object(complete.os.path, "isfile", mock.MagicMock(return_value=True))  # noqa:E501
    @mock.patch.object(complete.os, "makedirs", mock.MagicMock())
    def test_list(self):
        self.assertEqual(complete.Bash.list(), {"xsys"})


if __name__ == "__main__":
    unittest.main()
