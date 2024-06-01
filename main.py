from lark import Lark
from lark.indenter import PythonIndenter
from generic_transformer import GenTransformer

kwargs = dict(postlex=PythonIndenter(), start='file_input', maybe_placeholders=False, parser='lalr')

python_parser = Lark.open('python_grammar.lark', **kwargs)

program = open("generic_user.py").read()

p = python_parser.parse(program)

GenTransformer().transform(p)
print(p.pretty())
