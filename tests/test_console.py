#!/usr/bin/python3
""" test for console """

import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """ Test cases """
    @unittest.skip(" ")
    def test_quit_command(self):
        """ test quit """
        cmd = HBNBCommand()
        self.assertTrue(cmd.onecmd('quit'))

    @unittest.skip(" ")
    def test_help_quit_command(self):
        """ Test help quit """
        cmd = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            expected_output = "Quit command to exit the program"
            cmd.onecmd("help quit")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @unittest.skip(" ")
    def test_EOF_command(self):
        """ Test EOF command """
        cmd = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            expected_output = ""
            cmd.onecmd("EOF")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_emptyline(self):
        """ Test empty line """
        cmd = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            expected_output = ""
            cmd.emptyline()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_doc_string(self):
        """ test docstring """
        self.assertIsNotNone(HBNBCommand.__doc__, True)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__, True)
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__, True)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__, True)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__, True)

    def test_do_create_missing_class_name(self):
        cmd = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            expected_output = "** class name missing **"
            cmd.do_create("")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_do_create_non_existing_class(self):
        cmd = HBNBCommand()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            expected_output = "** class doesn't exist **"
            cmd.do_create("NonExistingClass")
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
