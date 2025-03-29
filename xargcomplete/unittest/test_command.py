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
    @mock.patch.object(command.Bash, "enable", mock.MagicMock())
    def test_enable(self, mock_system):
        mock_system.side_effect = [0, 123]
        self.assertEqual(command.main(["enable"]), 0)
        self.assertEqual(command.main(["enable"]), 123)

    @mock.patch.object(command.Bash, "update", mock.MagicMock())
    @mock.patch.object(command.shutil, "which")
    @mock.patch.object(command, "Collections")
    def test_update(self, mock_collections, mock_which):
        fake_collections = mock.MagicMock()
        fake_collections.cmds = ["test", "unittest"]
        mock_collections.side_effect = [fake_collections]
        mock_which.side_effect = [None, "/bin/unittest"]
        self.assertEqual(command.main(["update"]), 0)

    @mock.patch.object(command.Bash, "list", mock.MagicMock(return_value={"test"}))  # noqa:E501
    @mock.patch.object(command.Bash, "remove", mock.MagicMock())
    def test_remove(self):
        self.assertEqual(command.main(["remove"]), 0)

    @mock.patch.object(command.shutil, "which", mock.MagicMock(side_effect=[None]))  # noqa:E501
    @mock.patch.object(command.Bash, "list", mock.MagicMock(return_value={"test"}))  # noqa:E501
    @mock.patch.object(command.Bash, "remove", mock.MagicMock())
    def test_remove_auto_clean(self):
        self.assertEqual(command.main(["remove", "--auto-clean"]), 0)

    @mock.patch.object(command.shutil, "which", mock.MagicMock(side_effect=["/bin/test"]))  # noqa:E501
    @mock.patch.object(command.Bash, "list", mock.MagicMock(return_value={"test"}))  # noqa:E501
    def test_list(self):
        self.assertEqual(command.main(["list"]), 0)


if __name__ == "__main__":
    unittest.main()
