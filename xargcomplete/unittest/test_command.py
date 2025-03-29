# coding:utf-8

import unittest
from unittest import mock

from xargcomplete import command


class TestCommand(unittest.TestCase):

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

    @mock.patch.object(command.os, "system")
    def test_enable(self, mock_system):
        mock_system.side_effect = [0, 123]
        self.assertEqual(command.main(["enable"]), 0)
        self.assertEqual(command.main(["enable"]), 123)

    @mock.patch.object(command.Bash, "update", mock.MagicMock())
    def test_update(self):
        self.assertEqual(command.main(["update"]), 0)

    @mock.patch.object(command.shutil, "which", mock.MagicMock(return_value=None))  # noqa:E501
    def test_update_which_None(self):
        self.assertEqual(command.main(["update"]), 0)

    @mock.patch.object(command.Bash, "remove", mock.MagicMock())
    def test_remove(self):
        self.assertEqual(command.main(["remove"]), 0)

    @mock.patch.object(command.Bash, "remove", mock.MagicMock())
    def test_remove_auto_clean(self):
        self.assertEqual(command.main(["remove", "--auto-clean"]), 0)

    def test_list(self):
        self.assertEqual(command.main(["list"]), 0)


if __name__ == "__main__":
    unittest.main()
