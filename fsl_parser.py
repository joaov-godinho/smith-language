from fsl_lexer import Token

class ASTNode:
    pass 

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements 

class PrintNode(ASTNode):
    def __init__(self, expression_to_print):
        self.expression_to_print = expression_to_print 

# ... Outros nós: VariableDeclarationNode, IfNode, FunctionCallNode, etc.

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token('EOF', '', 0, 0) 

    def expect(self, token_type, error_message):
        if self.current_token and self.current_token.type == token_type:
            token_value = self.current_token.value
            self.advance()
            return token_value 
        else:
            line = self.current_token.line if self.current_token else 'desconhecida'
            col = self.current_token.column if self.current_token else 'desconhecido'
            current_type = self.current_token.type if self.current_token else 'Nenhum (EOF talvez?)'
            raise SyntaxError(f"Erro Sintático na Linha {line}, Col {col}: {error_message}. "
                              f"Esperava '{token_type}', mas encontrou '{current_type}' com valor '{self.current_token.value if self.current_token else ''}'.")


    def parse_statement(self):
        # Exemplo MUITO simplificado para um print
        if self.current_token and self.current_token.type == 'PRINTAR':
            self.advance() 
            self.expect('LPAREN', "Esperava '(' após 'Que foi cabeleira?'")
            if self.current_token and self.current_token.type == 'STRING_LITERAL':
                string_val = self.current_token.value
                self.advance()
                self.expect('RPAREN', "Esperava ')' após a string no 'Que foi cabeleira?'")
                self.expect('SEMICOLON', "Esperava ';' no final da instrução 'Que foi cabeleira?'")
                return PrintNode(string_val)
            else:
                raise SyntaxError("Esperava uma string literal dentro de 'Que foi cabeleira?(...)' por enquanto.")
            
        # Adicionar outras regras de parsing aqui (if, while, declarações, etc.)

        return None

    def parse(self):
        statements = []
        self.expect('INICIO_PROGRAMA', "O código deve começar com 'Eu juro vo sair cagando'")

        while self.current_token and self.current_token.type != 'FIM_PROGRAMA' and self.current_token.type != 'EOF':
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
            else:
                if self.current_token.type not in ['FIM_PROGRAMA', 'EOF']:
                    raise SyntaxError(f"Instrução não reconhecida ou erro na linha {self.current_token.line}: {self.current_token.value}")
                elif self.current_token.type == 'EOF' and self.tokens[self.pos-1].type != 'FIM_PROGRAMA':
                    self.expect('FIM_PROGRAMA', "O código deve terminar com 'Ta branco tiro na cabeça'")


        if self.current_token and self.current_token.type == 'FIM_PROGRAMA':
             self.advance()
        else:
            self.expect('FIM_PROGRAMA', "O código deve terminar com 'Ta branco tiro na cabeça'")

        self.expect('EOF', "Esperava fim de arquivo após 'Ta branco tiro na cabeça'")
        return ProgramNode(statements)

# Exemplo de uso (para testar o parser isoladamente com tokens mockados)
if __name__ == '__main__':
    mock_tokens = [
        Token('INICIO_PROGRAMA', 'Eu juro vo sair cagando', 1, 1),
        Token('PRINTAR', 'Que foi cabeleira?', 2, 3),
        Token('LPAREN', '(', 2, 20),
        Token('STRING_LITERAL', '"Teste"', 2, 21),
        Token('RPAREN', ')', 2, 28),
        Token('SEMICOLON', ';', 2, 29),
        Token('FIM_PROGRAMA', 'Ta branco tiro na cabeça', 3, 1),
        Token('EOF', '', 3, 26)
    ]
    parser = Parser(mock_tokens)
    try:
        ast = parser.parse()
        print("AST Gerada (simplificada):")
        print(f"Programa com {len(ast.statements)} statements.")
        for stmt in ast.statements:
            if isinstance(stmt, PrintNode):
                print(f"  - PrintNode com expressão: {stmt.expression_to_print}")
    except SyntaxError as e:
        print(f"Erro de Parsing: {e}")