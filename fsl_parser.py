# fsl_parser.py (VERSÃO FINALMENTE CORRIGIDA)
from fsl_lexer import Token

# --- ETAPA 1: DEFINIÇÃO DOS NÓS DA AST (Estruturas de Dados) ---
# Esta parte está correta e não muda.
class ASTNode: pass
class ProgramNode(ASTNode):
    def __init__(self, statements): self.statements = statements
class PrintNode(ASTNode):
    def __init__(self, expression): self.expression = expression
class VariableDeclarationNode(ASTNode):
    def __init__(self, var_type, var_name, expression=None):
        self.var_type = var_type; self.var_name = var_name; self.expression = expression
class AssignmentNode(ASTNode):
    def __init__(self, var_name, expression):
        self.var_name = var_name; self.expression = expression
class ExpressionNode(ASTNode):
    def __init__(self, tokens): self.tokens = tokens
class IfNode(ASTNode):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition; self.if_block = if_block; self.else_block = else_block
class WhileNode(ASTNode):
    def __init__(self, condition, body_block):
        self.condition = condition; self.body_block = body_block
class ForNode(ASTNode):
    def __init__(self, initialization, condition, increment, body_block):
        self.initialization = initialization; self.condition = condition; self.increment = increment; self.body_block = body_block
class ParamNode(ASTNode):
    def __init__(self, param_type, param_name):
        self.param_type = param_type; self.param_name = param_name
class FunctionDeclarationNode(ASTNode):
    def __init__(self, return_type, func_name, params, body_block):
        self.return_type = return_type; self.func_name = func_name; self.params = params; self.body_block = body_block
class FunctionCallNode(ASTNode):
    def __init__(self, func_name, args):
        self.func_name = func_name; self.args = args
class ReturnNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression


# --- ETAPA 2: O PARSER MODIFICADO ---

# Em fsl_parser.py, substitua sua classe Parser inteira por esta:

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None
        self.return_types = ['TIPO_INT', 'TIPO_FLOAT', 'TIPO_CHAR', 'TIPO_DOUBLE', 'TIPO_VOID']

    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def expect(self, token_type, error_message):
        if self.current_token and self.current_token.type == token_type:
            # Este método agora não retorna nada, apenas valida e avança.
            self.advance()
        else:
            line = self.current_token.line if self.current_token else 'desconhecida'
            col = self.current_token.column if self.current_token else 'desconhecido'
            current_type = self.current_token.type if self.current_token else 'Nenhum (EOF talvez?)'
            raise SyntaxError(f"Erro Sintático na Linha {line}, Col {col}: {error_message}. "
                              f"Esperava '{token_type}', mas encontrou '{current_type}'.")

    def parse_expression(self, end_tokens):
        expression_tokens = []
        paren_level = 0
        while self.current_token:
            if self.current_token.type in end_tokens and paren_level == 0: break
            if self.current_token.type == 'LPAREN': paren_level += 1
            elif self.current_token.type == 'RPAREN': paren_level -= 1
            expression_tokens.append(self.current_token)
            self.advance()
        return ExpressionNode(expression_tokens)
    
    def parse_function_call(self):
        self.advance() # Consome 'FUNC_CALL_PREFIX'
        func_name_token = self.current_token
        self.expect('IDENTIFIER', "Esperava nome da função após 'Da o cu'.")
        self.expect('LPAREN', "Esperava '(' após nome da função na chamada.")
        args = []
        if self.current_token.type != 'RPAREN':
            while True:
                args.append(self.parse_expression(end_tokens=['COMMA', 'RPAREN']))
                if self.current_token.type == 'RPAREN': break
                self.expect('COMMA', "Esperava ',' para separar argumentos.")
        self.expect('RPAREN', "Esperava ')' para fechar argumentos da chamada.")
        return FunctionCallNode(func_name_token.value, args)

    def parse_if_statement(self):
        self.advance()
        self.expect('LPAREN', "Esperava '(' após 'Debaixo da ponte?'.")
        condition = self.parse_expression(end_tokens=['RPAREN'])
        self.expect('RPAREN', "Esperava ')' após a condição do IF.")
        if_block = []
        while self.current_token and self.current_token.type not in ['ELSE', 'FIM_BLOCO_GENERICO']:
            if_block.append(self.parse_statement())
        else_block = None
        if self.current_token and self.current_token.type == 'ELSE':
            self.advance()
            else_block = []
            while self.current_token and self.current_token.type != 'FIM_BLOCO_GENERICO':
                else_block.append(self.parse_statement())
        self.expect('FIM_BLOCO_GENERICO', "Esperava 'Seu cu' para finalizar o bloco IF/ELSE.")
        return IfNode(condition, if_block, else_block)

    def parse_while_statement(self):
        self.advance()
        self.expect('LPAREN', "Esperava '(' após '5Km?'.")
        condition = self.parse_expression(end_tokens=['RPAREN'])
        self.expect('RPAREN', "Esperava ')' após a condição do WHILE.")
        body_block = []
        while self.current_token and self.current_token.type != 'FIM_BLOCO_GENERICO':
            body_block.append(self.parse_statement())
        self.expect('FIM_BLOCO_GENERICO', "Esperava 'Seu cu' para finalizar o loop '5Km?'.")
        return WhileNode(condition, body_block)

    def parse_for_statement(self):
        self.advance()
        self.expect('LPAREN', "Esperava '(' após 'Rave, RAVE?!'.")
        initialization = self.parse_expression(end_tokens=['SEMICOLON'])
        self.expect('SEMICOLON', "Esperava ';' após a inicialização do FOR.")
        condition = self.parse_expression(end_tokens=['SEMICOLON'])
        self.expect('SEMICOLON', "Esperava ';' após a condição do FOR.")
        increment = self.parse_expression(end_tokens=['RPAREN'])
        self.expect('RPAREN', "Esperava ')' para fechar os parâmetros do FOR.")
        body_block = []
        while self.current_token and self.current_token.type != 'FIM_BLOCO_GENERICO':
            body_block.append(self.parse_statement())
        self.expect('FIM_BLOCO_GENERICO', "Esperava 'Seu cu' para finalizar o loop 'Rave, RAVE?!'.")
        return ForNode(initialization, condition, increment, body_block)

    def parse_function_declaration(self):
        self.advance()
        if self.current_token.type not in self.return_types:
            raise SyntaxError(f"Tipo de retorno de função inválido: '{self.current_token.value}'")
        return_type_token = self.current_token
        self.advance()
        func_name_token = self.current_token
        self.expect('IDENTIFIER', "Esperava nome da função após o tipo de retorno.")
        self.expect('LPAREN', "Esperava '(' para iniciar a lista de parâmetros.")
        params = []
        if self.current_token.type != 'RPAREN':
            while True:
                if self.current_token.type not in self.return_types:
                    raise SyntaxError(f"Tipo de parâmetro inválido: '{self.current_token.value}'")
                param_type_token = self.current_token
                self.advance()
                param_name_token = self.current_token
                self.expect('IDENTIFIER', "Esperava nome do parâmetro após o tipo.")
                params.append(ParamNode(param_type_token, param_name_token))
                if self.current_token.type == 'RPAREN': break
                self.expect('COMMA', "Esperava ',' para separar parâmetros.")
        self.expect('RPAREN', "Esperava ')' para fechar a lista de parâmetros.")
        body_block = []
        while self.current_token and self.current_token.type != 'FIM_BLOCO_GENERICO':
            body_block.append(self.parse_statement())
        self.expect('FIM_BLOCO_GENERICO', "Esperava 'Seu cu' para finalizar o corpo da função.")
        return FunctionDeclarationNode(return_type_token, func_name_token, params, body_block)

    def parse_statement(self):
        if not self.current_token or not self.current_token.type: return None
        token_type = self.current_token.type

        if token_type == 'FUNC_DECL': return self.parse_function_declaration()
        if token_type == 'IF': return self.parse_if_statement()
        if token_type == 'WHILE': return self.parse_while_statement()
        if token_type == 'FOR': return self.parse_for_statement()

        if token_type == 'FUNC_CALL_PREFIX':
            call_node = self.parse_function_call()
            self.expect('SEMICOLON', "Esperava ';' após chamada de função.")
            return call_node
        
        if token_type == 'RETURN':
            self.advance()
            expression = self.parse_expression(end_tokens=['SEMICOLON'])
            self.expect('SEMICOLON', "Esperava ';' após a expressão de retorno ('Achei').")
            return ReturnNode(expression)

        if token_type == 'PRINTAR':
            self.advance()
            self.expect('LPAREN', "Esperava '(' após 'Que foi cabeleira?'.")
            expression = self.parse_expression(end_tokens=['RPAREN'])
            self.expect('RPAREN', "Esperava ')' no final do 'Que foi cabeleira?'.")
            self.expect('SEMICOLON', "Esperava ';' no final da instrução.")
            return PrintNode(expression)

        if token_type in self.return_types:
            var_type_token = self.current_token
            self.advance()
            var_name_token = self.current_token
            self.expect('IDENTIFIER', f"Esperava nome da variável após tipo '{var_type_token.value}'.")
            expression = None
            if self.current_token and self.current_token.type == 'ASSIGN':
                self.advance()
                if self.current_token.type == 'FUNC_CALL_PREFIX':
                    expression = self.parse_function_call()
                else:
                    expression = self.parse_expression(end_tokens=['SEMICOLON'])
            self.expect('SEMICOLON', "Esperava ';' no final da declaração.")
            return VariableDeclarationNode(var_type_token, var_name_token, expression)

        if token_type == 'IDENTIFIER':
            var_name_token = self.current_token
            self.advance()
            self.expect('ASSIGN', f"Esperava '=' após o nome da variável '{var_name_token.value}'.")
            if self.current_token.type == 'FUNC_CALL_PREFIX':
                expression = self.parse_function_call()
            else:
                expression = self.parse_expression(end_tokens=['SEMICOLON'])
            self.expect('SEMICOLON', "Esperava ';' no final da atribuição.")
            return AssignmentNode(var_name_token, expression)
        
        return None

    def parse(self):
        """Ponto de entrada do parser."""
        statements = []
        while self.current_token and self.current_token.type == 'FUNC_DECL':
            statements.append(self.parse_statement())
        
        self.expect('INICIO_PROGRAMA', "O código deve começar com 'Eu juro vo sair cagando' após as declarações de função.")
        
        main_body = []
        while self.current_token and self.current_token.type != 'FIM_PROGRAMA':
            statement = self.parse_statement()
            if statement:
                main_body.append(statement)
            else:
                # Se parse_statement retorna None e não estamos no fim, é um erro.
                raise SyntaxError(f"Instrução inválida ou inesperada dentro do programa principal: '{self.current_token.value}'")
        
        self.expect('FIM_PROGRAMA', "O código deve terminar com 'Ta branco tiro na cabeça'")
        
        main_func = FunctionDeclarationNode(
            Token('TIPO_INT', '14', 0, 0), 
            Token('IDENTIFIER', 'main', 0, 0),
            [], # Sem parâmetros
            main_body
        )
        statements.append(main_func)
        
        if self.current_token and self.current_token.type == 'EOF':
            self.advance()
        return ProgramNode(statements)