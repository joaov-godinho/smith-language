class Transpiler:
    def __init__(self):
        self.c_code = ""
        self.indent_level = 0

    def add_line(self, line):
        self.c_code += "    " * self.indent_level + line + "\n"

    def translate_node(self, node):
        node_type = type(node).__name__
        #print(f"Translating node: {node_type}") # Debug
        if node_type == 'ProgramNode':
            self.add_line("#include <stdio.h> // Incluído por padrão")
            self.add_line("#include <string.h> // Para manipulação de strings se necessário")
            self.add_line("")
            self.add_line("int main() {")
            self.indent_level += 1
            for stmt in node.statements:
                self.translate_node(stmt)
            self.indent_level -= 1
            self.add_line("return 0;")
            self.add_line("}")
        elif node_type == 'PrintNode':
            expression_c = node.expression_to_print 
            self.add_line(f'printf({expression_c});')

        # Adicionar tradução para outros tipos de nós da AST aqui
        # elif node_type == 'VariableDeclarationNode':
        #    c_type = self.map_fsl_type_to_c(node.var_type)
        #    self.add_line(f"{c_type} {node.var_name};") # Se não houver inicialização
        # ... e assim por diante

        else:
            print(f"Aviso: Tradução não implementada para o tipo de nó: {node_type}")


    def map_fsl_type_to_c(self, fsl_type_token_value):
        if fsl_type_token_value == '14': return 'int'
        if fsl_type_token_value == '16': return 'float'
        if fsl_type_token_value == 'Smith': return 'char'
        if fsl_type_token_value == 'Red Bull?': return 'double'
        if fsl_type_token_value == 'Katrina': return 'void'
        raise ValueError(f"Tipo FSL desconhecido para mapeamento: {fsl_type_token_value}")

    def transpile(self, ast_root):
        self.c_code = "" 
        self.translate_node(ast_root)
        return self.c_code

# Exemplo de uso (para testar o transpiler isoladamente com AST mockada)
if __name__ == '__main__':
    class ASTNode: pass
    class ProgramNode(ASTNode):
        def __init__(self, statements): self.statements = statements
    class PrintNode(ASTNode):
        def __init__(self, expression_to_print): self.expression_to_print = expression_to_print

    mock_ast = ProgramNode(statements=[
        PrintNode(expression_to_print='"Teste FSL para C"')
    ])

    transpiler = Transpiler()
    c_code_output = transpiler.transpile(mock_ast)
    print("--- Código C Gerado ---")
    print(c_code_output)