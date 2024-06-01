from lark.visitors import Transformer_InPlace
from lark import Tree, Token, v_args

token_generic = Token('NAME', 'Generic')

class GenTransformer(Transformer_InPlace):
    @v_args(tree=True)
    def classdef(self, tree):
        name, generics, arguments, suite = tree.children
        if not arguments:
            return tree
        
        types = []
        to_filter = []
        # find all getitem in class arguments
        for getitem in filter(lambda child: child.data == "getitem", arguments.children):

            #collect all generic type names into types[] list
            func_var, func_arguments = getitem.children
            var_tokens = func_var.scan_values(lambda x: isinstance(x, Token))
            
            arg_tokens = list(func_arguments.scan_values(lambda x: isinstance(x, Token)))
            for t in var_tokens:
                if t == token_generic:
                    types += [tk.value for tk in arg_tokens]
                    to_filter.append(getitem)
        if not types:
            return tree
        
        #clear arguments of a class from Generic[T]
        for f in to_filter:
            arguments.children.remove(f)

        generics_children = []
        for t in types:
            generics_children.append(Tree("name", [Token("NAME", t)]))

        # это делалалось в попытке поправить падающие тесты
        if not generics:
            generics = Tree("generics", generics_children)
        else:
            generics.children += generics_children
        if arguments.children:
            return Tree("classdef", [name, generics, arguments, suite])
        return Tree("classdef", [name, generics, suite])
    