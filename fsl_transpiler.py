# fsl_transpiler.py (com importação dos nós da AST)

# <<-- ADICIONE ESTA LINHA DE IMPORTAÇÃO NO TOPO DO ARQUIVO -->>
from fsl_parser import FunctionCallNode, ReturnNode

class Transpiler:
    def __init__(self):
        self.c_code = ""
        self.indent_level = 0

    def add_line(self, line):
        self.c_code += "    " * self.indent_level + line + "\n"
    
    def map_fsl_type_to_c(self, fsl_type_token_value):
        type_map = {'14': 'int', '16': 'float', 'Smith': 'char', 'Red Bull?': 'double', 'Katrina': 'void'}
        c_type = type_map.get(fsl_type_token_value)
        if c_type is None: raise ValueError(f"Tipo FSL desconhecido para mapeamento: {fsl_type_token_value}")
        return c_type

    def translate_expression(self, expression_node):
        # Se a expressão for uma chamada de função, traduza-a corretamente
        if isinstance(expression_node, FunctionCallNode):
            return self.translate_FunctionCallNode(expression_node, as_expression=True)
        return " ".join([token.value for token in expression_node.tokens])

    def translate_node(self, node):
        """Dispatcher principal que chama o método de tradução correto."""
        node_type = type(node).__name__
        method_name = f"translate_{node_type}"
        translator_method = getattr(self, method_name, self.unsupported_node)
        translator_method(node)

    def unsupported_node(self, node):
        node_type = type(node).__name__
        print(f"Aviso: Tradução não implementada para o tipo de nó: {node_type}")

    # --- MÉTODOS DE TRADUÇÃO PARA CADA TIPO DE NÓ ---

    def translate_ProgramNode(self, node):
        self.add_line("#include <stdio.h>")
        self.add_line("")
        for stmt in node.statements:
            self.translate_node(stmt)
            self.add_line("") # Espaço entre as funções

    def translate_PrintNode(self, node):
        expression_c = self.translate_expression(node.expression)
        self.add_line(f'printf({expression_c});')
    
    def translate_VariableDeclarationNode(self, node):
        c_type = self.map_fsl_type_to_c(node.var_type.value)
        line = f"{c_type} {node.var_name.value}"
        if node.expression:
            expression_c = self.translate_expression(node.expression)
            line += f" = {expression_c}"
        line += ";"
        self.add_line(line)

    def translate_AssignmentNode(self, node):
        expression_c = self.translate_expression(node.expression)
        line = f"{node.var_name.value} = {expression_c};"
        self.add_line(line)

    def translate_IfNode(self, node):
        condition_c = self.translate_expression(node.condition)
        self.add_line(f"if ({condition_c}) {{")
        self.indent_level += 1
        for stmt in node.if_block:
            self.translate_node(stmt)
        self.indent_level -= 1
        self.add_line("}")
        if node.else_block is not None:
            self.add_line("else {")
            self.indent_level += 1
            for stmt in node.else_block:
                self.translate_node(stmt)
            self.indent_level -= 1
            self.add_line("}")
    
    def translate_WhileNode(self, node):
        condition_c = self.translate_expression(node.condition)
        self.add_line(f"while ({condition_c}) {{")
        self.indent_level += 1
        for stmt in node.body_block:
            self.translate_node(stmt)
        self.indent_level -= 1
        self.add_line("}")

    def translate_ForNode(self, node):
        init_c = self.translate_expression(node.initialization)
        cond_c = self.translate_expression(node.condition)
        inc_c = self.translate_expression(node.increment)
        self.add_line(f"for ({init_c}; {cond_c}; {inc_c}) {{")
        self.indent_level += 1
        for stmt in node.body_block:
            self.translate_node(stmt)
        self.indent_level -= 1
        self.add_line("}")

    def translate_FunctionDeclarationNode(self, node):
        return_type_c = self.map_fsl_type_to_c(node.return_type.value)
        func_name_c = node.func_name.value
        params_c = []
        for param in node.params:
            param_type_c = self.map_fsl_type_to_c(param.param_type.value)
            params_c.append(f"{param_type_c} {param.param_name.value}")
        is_main = func_name_c == 'main'
        self.add_line(f"{return_type_c} {func_name_c}({', '.join(params_c)}) {{")
        self.indent_level += 1
        for stmt in node.body_block:
            self.translate_node(stmt)
        if is_main and not any(isinstance(s, ReturnNode) for s in node.body_block):
            self.add_line("return 0;")
        self.indent_level -= 1
        self.add_line("}")

    def translate_FunctionCallNode(self, node, as_expression=False):
        func_name_c = node.func_name
        args_c = [self.translate_expression(arg) for arg in node.args]
        call_str = f"{func_name_c}({', '.join(args_c)})"
        if as_expression:
            return call_str
        else:
            self.add_line(f"{call_str};")

    def translate_ReturnNode(self, node):
        expression_c = self.translate_expression(node.expression)
        self.add_line(f"return {expression_c};")

    def transpile(self, ast_root):
        self.c_code = ""
        self.translate_node(ast_root)
        return self.c_code