import re

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, '{self.value}', Ln {self.line}, Col {self.column})"

# Definição dos tipos de tokens que a linguagem terá
TOKEN_REGEX_RULES = [
    # Palavras-chave e Estruturas Principais
    ('INICIO_PROGRAMA', r'Eu juro vo sair cagando'),
    ('FIM_PROGRAMA', r'Ta branco tiro na cabeça'),
    ('PRINTAR', r'Que foi cabeleira\?'),
    ('LER_INPUT', r'Eu tenho quantos anos gente\?'),
    ('IF', r'Debaixo da ponte\?'),
    ('ELSE', r'Faz isso comigo não velho'),
    ('FIM_BLOCO_GENERICO', r'Seu cu'),
    ('WHILE', r'5Km\?'),
    ('FOR', r'Rave, RAVE\?!'),
    ('CONTINUE', r'Pega um incenso pra mim pelo amor de deus'),
    ('BREAK', r'Sai daê doido'),
    ('FUNC_DECL', r'Minha arte'),
    ('FUNC_CALL_PREFIX', r'Da o cu'),
    ('RETURN', r'Achei'),

    # Tipos de Dados
    ('TIPO_CHAR', r'Smith'),
    ('TIPO_INT', r'14'),
    ('TIPO_FLOAT', r'16'),
    ('TIPO_DOUBLE', r'Red Bull\?'),
    ('TIPO_VOID', r'Katrina'),

    # Literais
    ('NUMBER_LITERAL', r'\b\d+(\.\d*)?\b|\b\.\d+\b'), 
    ('STRING_LITERAL', r'"(?:\\.|[^"\\])*"'), 

    # Identificadores
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),

    ('COMMENT', r'//.*'),

    # Operadores e Delimitadores
    ('OP_IGUAL', r'=='),
    ('OP_DIFERENTE', r'!='),
    ('OP_MAIOR_IGUAL', r'>='),
    ('OP_MENOR_IGUAL', r'<='),
    ('OP_AND', r'&&'),
    ('OP_OR', r'\|\|'),
    ('ASSIGN', r'='),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('SEMICOLON', r';'),
    ('COMMA', r','),
    ('OP_MAIOR', r'>'),
    ('OP_MENOR', r'<'),
    ('OP_SOMA', r'\+'),
    ('OP_SUB', r'-'),
    ('OP_MUL', r'\*'),
    ('OP_DIV', r'/'),
    ('OP_MOD', r'%'),

    # Ignorar espaços em branco e comentários
    ('NEWLINE', r'\n'),
    ('SKIP', r'\s+'),
    ('MISMATCH', r'.'), 
]

def tokenize(code):
    tokens = []
    line_num = 1
    line_start_pos = 0
    pos = 0
    while pos < len(code):
        # Pula todos os caracteres de whitespace, exceto a nova linha
        if code[pos] in ' \t\r\u00A0': # Espaço, Tab, Retorno de Carro, Espaço Não-Separável
            pos += 1
            continue
        
        # Trata a nova linha para incrementar o contador de linha
        if code[pos] == '\n':
            line_num += 1
            line_start_pos = pos + 1
            pos += 1
            continue

        match = None
        for token_type, regex_pattern in TOKEN_REGEX_RULES:
            if token_type in ['SKIP', 'NEWLINE']:
                continue

            regex = re.compile(regex_pattern)
            m = regex.match(code, pos)
            if m:
                value = m.group(0)
                
                # Trata comentários
                if token_type == 'COMMENT':
                    pos = m.end(0)
                    match = True
                    break # Ignora o resto e vai para a próxima posição do código
                
                # Adiciona o token encontrado
                tokens.append(Token(token_type, value, line_num, pos - line_start_pos + 1))
                pos = m.end(0)
                match = True
                break

        # Se, após pular os espaços, ainda não encontrar match, é um erro.
        if not match:
            mismatch_char = code[pos]
            tokens.append(Token('MISMATCH', mismatch_char, line_num, pos - line_start_pos + 1))
            pos += 1


    tokens.append(Token('EOF', '', line_num, pos - line_start_pos + 1))
    return tokens

# Exemplo de uso (para testar o lexer isoladamente)
if __name__ == '__main__':
    sample_code = """
Eu juro vo sair cagando
    // Isso é um comentário
    14 idade = 16;
    Que foi cabeleira? ("Tem %d anos!", idade);
    Debaixo da ponte? (idade > 14)
        Que foi cabeleira? ("Maior que 14!");
    Seu cu // fim do if
Ta branco tiro na cabeça
    """
    generated_tokens = tokenize(sample_code)
    for token in generated_tokens:
        print(token)