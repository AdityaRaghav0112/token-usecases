import ast

class VariableRenamer(ast.NodeTransformer):
    def __init__(self):
        self.mapping = {}
        self.counter = 0

    def _new_name(self):
        name = chr(97 + self.counter)  # a, b, c...
        self.counter += 1
        return name

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):  # variable being assigned
            if node.id not in self.mapping:
                self.mapping[node.id] = self._new_name()
        if node.id in self.mapping:
            node.id = self.mapping[node.id]
        return node


def rename_variables(code: str) -> str:
    tree = ast.parse(code)
    renamer = VariableRenamer()
    tree = renamer.visit(tree)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)