import unittest
from lark import Lark
from lark.indenter import PythonIndenter
from generic_transformer import GenTransformer
import test_input


class GenericUserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.input_python_parser = Lark.open('python_grammar.lark', start='file_input', postlex=PythonIndenter())        
        self.transformer = GenTransformer()

    def test_single_parameter(self):
        input_tree = self.input_python_parser.parse(test_input.single_parameter_user)
        expected_tree = self.input_python_parser.parse(test_input.single_parameter_user_expected)
        self.transformer.transform(input_tree)
        expected, result = expected_tree.pretty().replace("None", ""), input_tree.pretty()
        self.assertEqual(expected.split(), result.split())
    
    def test_multiple_parameter_user(self):
        input_tree = self.input_python_parser.parse(test_input.multiple_parameter_user)
        expected_tree = self.input_python_parser.parse(test_input.multiple_parameter_user_expected)
        self.transformer.transform(input_tree)
        expected, result = expected_tree.pretty(), input_tree.pretty()
        self.assertEqual(expected.split(), result.split())
    
    def test_multiple_parameter_user_2(self):
        input_tree = self.input_python_parser.parse(test_input.multiple_parameter_user_2)
        expected_tree = self.input_python_parser.parse(test_input.multiple_parameter_user_2_expected)
        self.transformer.transform(input_tree)
        expected, result = expected_tree.pretty().replace("None", ""), input_tree.pretty()
        self.assertEqual(expected.split(), result.split())
    
    def test_multiple_parameter_user_v2(self):
        input_tree = self.input_python_parser.parse(test_input.multiple_parameter_user_v2)
        expected_tree = self.input_python_parser.parse(test_input.multiple_parameter_user_v2_expected)
        self.transformer.transform(input_tree)
        expected, result = expected_tree.pretty().replace("None", ""), input_tree.pretty()
        self.assertEqual(expected.split(), result.split())

    def test_no_generic_user(self):
        input_tree = self.input_python_parser.parse(test_input.no_generic_user)
        expected_tree = self.input_python_parser.parse(test_input.no_generic_user_expected)
        self.transformer.transform(input_tree)
        expected, result = expected_tree.pretty().replace("None", ""), input_tree.pretty().replace("None", "")
        self.assertEqual(result.split(), expected.split())


if __name__ == '__main__':
    unittest.main()