import re

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, '{self.value}', Ln {self.line}, Col {self.column})"

# Definição dos tipos de tokens que sua linguagem terá
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
    ('FOR', r'Rave, RAVE\?'),
    ('CONTINUE', r'Pega um incenso pra mim pelo amor de deus'),
    ('BREAK', r'Sai daê doido'),
    ('FUNC_DECL', r'Minha arte'),
    ('FUNC_CALL_PREFIX', r'Da o cu'),

    # Tipos de Dados
    ('TIPO_CHAR', r'Smith'),
    ('TIPO_INT', r'14'),
    ('TIPO_FLOAT', r'16'),
    ('TIPO_DOUBLE', r'Red Bull\?'),
    ('TIPO_VOID', r'Katrina'),

    # Literais
    ('NUMBER_LITERAL', r'\b\d+(\.\d*)?\b|\b\.\d+\b'), 
    ('STRING_LITERAL', r'"(?:\\.|[^"\\])*"'), 

    # Identificadores (nomes de variáveis, funções)
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),

    # Operadores e Delimitadores
    ('ASSIGN', r'='),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('SEMICOLON', r';'),
    ('COMMA', r','),
    ('OP_MAIOR', r'>'),
    ('OP_MENOR', r'<'),
    ('OP_IGUAL', r'=='),
    ('OP_MAIOR_IGUAL', r'>='),
    ('OP_MENOR_IGUAL', r'<='),
    ('OP_DIFERENTE', r'!='),
    ('OP_SOMA', r'\+'),
    ('OP_SUB', r'-'),
    ('OP_MUL', r'\*'),
    ('OP_DIV', r'/'),
    ('OP_AND', r'&&'), 
    ('OP_OR', r'\|\|'),

    # Ignorar espaços em branco e comentários (simples por enquanto)
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('COMMENT', r'//.*'),
    ('MISMATCH', r'.'), 
]

def tokenize(code):
    tokens = []
    line_num = 1
    line_start_pos = 0
    pos = 0
    while pos < len(code):
        match = None
        # Verifica nova linha para contagem e posição da coluna
        if code[pos] == '\n':
            tokens.append(Token('NEWLINE', '\n', line_num, pos - line_start_pos + 1))
            line_num += 1
            line_start_pos = pos + 1
            pos += 1
            continue

        # Ignora espaços e tabs
        if re.match(r'[ \t]+', code[pos]):
            pos +=1
            continue

        # Ignora comentários
        comment_match = re.match(r'//.*', code[pos:])
        if comment_match:
            comment_text = comment_match.group(0)
            newline_in_comment = comment_text.find('\n')
            if newline_in_comment != -1:
                pos += newline_in_comment
            else:
                pos += len(comment_text)
            continue


        for token_type, regex_pattern in TOKEN_REGEX_RULES:
            regex = re.compile(regex_pattern)
            m = regex.match(code, pos)
            if m:
                value = m.group(0)
                if token_type not in ['SKIP', 'COMMENT', 'NEWLINE']: 
                    tokens.append(Token(token_type, value, line_num, pos - line_start_pos + 1))
                match = True
                pos = m.end(0)
                break
        if not match:
            m_mismatch = re.match(r'.', code[pos])
            if m_mismatch:
                 tokens.append(Token('MISMATCH', m_mismatch.group(0), line_num, pos - line_start_pos + 1))
                 pos = m_mismatch.end(0)
            else:
                raise RuntimeError(f"Caractere inesperado na linha {line_num} coluna {pos - line_start_pos + 1}: {code[pos]}")


    tokens.append(Token('EOF', '', line_num, pos - line_start_pos + 1))
    return [t for t in tokens if t.type not in ['SKIP', 'COMMENT', 'NEWLINE']]

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