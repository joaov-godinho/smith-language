# Felipe Smith Language (FSL) 🤪

**Transformando o meme Felipe Smith em código executável! "COÉ PC???"**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Compiler](https://img.shields.io/badge/Type-Transpiler-orange)](https://github.com/joaov-godinho/smith-language)
[![Status](https://img.shields.io/badge/Status-Functional-success)](https://github.com/joaov-godinho/smith-language)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🚀 Por Trás do Código

Inspirado no meme **Felipe Smith** e no já memético [birl-language](https://birl-language.github.io/), este projeto nasceu como uma forma divertida e educativa de explorar os conceitos da disciplina de **Compiladores**.

O objetivo? Pegar as frases de efeito, os momentos de angústia e as pérolas de sabedoria de Felipe Smith e transformá-los em uma linguagem de programação imperativa. Sim, "ensinamos" o computador a entender **"Eu juro vo sair cagando"** como o início de tudo!

### 🎯 Aspectos Técnicos Relevantes

- **Paradigma Funcional:** Pipeline puro de transformações (Source → Tokens → AST → C Code)
- **Transpilador Completo:** Implementação full-stack de compilador
- **Integração com GCC:** Orquestração automática de compilação e execução
- **Zero Dependências Externas:** Apenas Python padrão + expressões regulares

---

## 🗣️ O que é a Felipe Smith Language (FSL)?

A FSL é uma **linguagem de programação imperativa**, onde as palavras-chave, tipos de dados e estruturas de controle da linguagem C foram substituídas por frases que viralizaram no meme Felipe Smith.

### 📝 Sintaxe da FSL

#### Estrutura Básica

```fsl
Eu juro vo sair cagando
    // Seu código aqui
Ta branco tiro na cabeça
```

#### Tipos de Dados

| FSL | C Equivalente | Exemplo |
|-----|---------------|---------|
| `14` | `int` | `14 idade;` |
| `16` | `float` | `16 altura;` |
| `Smith` | `char` | `Smith inicial;` |
| `Red Bull?` | `double` | `Red Bull? pi;` |
| `Katrina` | `void` | `Katrina` (função sem retorno) |

#### Comandos Principais

```fsl
// Saída (printf)
Que foi cabeleira? ("Olá, mundo!");

// Entrada (scanf)
Vixi vixi? ("%d", &idade);

// Condicional IF
Debaixo da ponte? (idade >= 18)
    Que foi cabeleira? ("Maior de idade");
Seu cu

// Condicional IF/ELSE
Debaixo da ponte? (nota >= 7)
    Que foi cabeleira? ("Aprovado");
Faz isso comigo não velho
    Que foi cabeleira? ("Reprovado");
Seu cu

// Loop WHILE
5Km? (contador < 10)
    contador = contador + 1;
Seu cu

// Loop FOR
Rave, RAVE?! (14 i = 0; i < 10; i = i + 1)
    Que foi cabeleira? ("Iteration");
Seu cu

// Função
Guarapari - Buzios calcularSoma (14 a, 14 b)
    Da o cu (a + b);
Seu cu

// Chamada de função
14 resultado;
Minha arte calcularSoma(5, 3);
```

---

## 🛠️ Como Essa Mágica Acontece? (Visão Técnica)

Por baixo de toda a zueira, existe um **processo de compilação** bem definido seguindo o paradigma funcional:

### Pipeline de Compilação

```
┌──────────────────┐
│  Código FSL      │  "Eu juro vo sair cagando..."
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Lexer (Puro)    │  Transforma em Tokens
│  fsl_lexer.py    │  "EU_JURO_VO_SAIR_CAGANDO" → T_MAIN_START
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Parser (Puro)   │  Valida sintaxe e constrói AST
│  fsl_parser.py   │  Sequência de tokens → Árvore Sintática
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Transpiler (Puro)│  Gera código C equivalente
│fsl_transpiler.py │  AST → Código C válido
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  GCC (Externo)   │  Compila C → Executável
│  subprocess      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Execução       │  ./programa
└──────────────────┘
```

### Análise de Cada Fase

#### 1. **Análise Léxica** (`fsl_lexer.py`)
Quebra o código fonte em **tokens** usando expressões regulares:

```python
# Função pura: String → List[Token]
def tokenize(source_code: str) -> List[Token]:
    patterns = {
        r'Eu juro vo sair cagando': 'T_MAIN_START',
        r'Debaixo da ponte\?': 'T_IF',
        r'14': 'T_INT',
        # ...
    }
    return [Token(type, value) for match in matches]
```

#### 2. **Análise Sintática** (`fsl_parser.py`)
Valida a sequência de tokens e constrói uma **AST**:

```python
# Função pura: List[Token] → AST
def parse(tokens: List[Token]) -> AST:
    ast = ASTNode('program')
    # Valida estrutura gramatical
    # Constrói árvore sintática abstrata
    return ast
```

#### 3. **Transpilação** (`fsl_transpiler.py`)
Percorre a AST e gera **código C**:

```python
# Função pura: AST → String (código C)
def transpile(ast: AST) -> str:
    c_code = ""
    for node in ast.traverse():
        c_code += translate_node(node)  # Puro
    return c_code
```

#### 4. **Compilação e Execução** (`main.py`)
**Único ponto com efeitos colaterais:**

```python
# Efeito colateral: I/O, execução externa
def compile_and_run(c_code: str):
    with open('output.c', 'w') as f:  # I/O
        f.write(c_code)
    
    subprocess.run(['gcc', 'output.c', '-o', 'programa'])  # Externo
    subprocess.run(['./programa'])  # Execução
```

---

## 🎯 Exemplo Completo

### Código FSL

```fsl
Eu juro vo sair cagando
    14 idade;
    
    Que foi cabeleira? ("Digite sua idade: ");
    Vixi vixi? ("%d", &idade);
    
    Debaixo da ponte? (idade >= 18)
        Que foi cabeleira? ("Você é maior de idade!
");
    Faz isso comigo não velho
        Que foi cabeleira? ("Você é menor de idade!
");
    Seu cu
Ta branco tiro na cabeça
```

### Código C Gerado

```c
#include <stdio.h>

int main() {
    int idade;
    
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    
    if (idade >= 18) {
        printf("Você é maior de idade!\n");
    } else {
        printf("Você é menor de idade!\n");
    }
    
    return 0;
}
```

---

## 💻 Tecnologias Utilizadas

| Componente | Tecnologia | Função |
|------------|-----------|--------|
| **Linguagem Principal** | Python 3.8+ | Implementação do transpilador |
| **Lexer** | Módulo `re` (regex) | Tokenização |
| **Parser** | Python puro | Análise sintática |
| **Transpiler** | Python puro | Geração de código C |
| **Compilador C** | GCC | Compilação do código gerado |
| **Orquestração** | `subprocess` | Invocação de GCC e execução |

### Paradigma Funcional Aplicado

✅ **Separação de Efeitos:** I/O isolado em `main.py`  
✅ **Funções Puras:** Lexer, Parser e Transpiler são determinísticos  
✅ **Composição:** Pipeline de transformações encadeadas  
✅ **Imutabilidade:** Tokens e AST são estruturas imutáveis  

---

## 🚀 Como Executar

### 1. Pré-requisitos

- **Python 3.8+** instalado
- **GCC** (GNU Compiler Collection) instalado e no PATH

**Instalação do GCC:**
- **Linux:** `sudo apt-get install gcc` (Debian/Ubuntu)
- **macOS:** `xcode-select --install`
- **Windows:** [MinGW](http://www.mingw.org/) ou [MSYS2](https://www.msys2.org/)

### 2. Clone o Repositório

```bash
git clone https://github.com/joaov-godinho/smith-language.git
cd smith-language
```

### 3. Execute o Transpilador

```bash
python main.py
```

O script solicitará o caminho para um arquivo `.fsl`. Você pode:
- Digitar o caminho do seu próprio arquivo
- Pressionar **Enter** para usar o exemplo padrão em `exemplos/`

### 4. Aprecie a Mágica! 🎉

```
$ python main.py
Digite o caminho do arquivo FSL (ou Enter para exemplo): 

[INFO] Lendo arquivo: exemplos/ola_felipe.fsl
[INFO] Tokenização... ✓
[INFO] Análise sintática... ✓
[INFO] Transpilação para C... ✓
[INFO] Compilando com GCC... ✓
[INFO] Executando programa...

--- OUTPUT ---
COÉ PC??? O programa tá rodando!
Maior de idade detectado!
--------------
```

---

## 📁 Estrutura do Projeto

```
smith-language/
├── fsl_lexer.py          # Analisador léxico (String → Tokens)
├── fsl_parser.py         # Analisador sintático (Tokens → AST)
├── fsl_transpiler.py     # Gerador de código (AST → C)
├── main.py               # Orquestrador principal
├── exemplos/
│   ├── ola_felipe.fsl    # Exemplo básico
│   ├── loops.fsl         # Demonstração de loops
│   └── funcoes.fsl       # Demonstração de funções
├── README.md
└── requirements.txt      # (vazio - sem dependências externas)
```

---

## 🎯 Status Atual do Projeto

### ✅ Implementado

- ✅ Analisador Léxico completo
- ✅ Analisador Sintático funcional
- ✅ Transpilador para C
- ✅ Suporte a tipos básicos (int, float, char, double, void)
- ✅ Estruturas condicionais (IF, IF/ELSE)
- ✅ Loops (WHILE, FOR)
- ✅ Funções (declaração e chamada)
- ✅ I/O (printf, scanf equivalentes)
- ✅ Expressões aritméticas e lógicas
- ✅ Orquestração completa (FSL → Executável)

### 🔮 Roadmap Futuro

- [ ] Mensagens de erro mais descritivas (com linha/coluna)
- [ ] Suporte a arrays
- [ ] Suporte a structs
- [ ] Otimizações no código C gerado
- [ ] REPL interativo
- [ ] Extensão VSCode com syntax highlighting
- [ ] Documentação completa da gramática (BNF)

---

## 🧪 Testes

Rode os exemplos incluídos:

```bash
# Exemplo básico
python main.py exemplos/ola_felipe.fsl

# Loops
python main.py exemplos/loops.fsl

# Funções
python main.py exemplos/funcoes.fsl
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/NovoComando`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo comando FSL'`)
4. Push para a branch (`git push origin feature/NovoComando`)
5. Abra um Pull Request

### Ideias de Contribuição

- 📝 Adicionar novos comandos baseados em frases do Felipe Smith
- 🐛 Corrigir bugs no parser
- 📚 Melhorar documentação
- 🎨 Criar syntax highlighting para editores
- 🧪 Adicionar testes automatizados

---

## 🏆 Equipe da "Rave"

- **João Vitor Borges Godinho** ([@joaov-godinho](https://github.com/joaov-godinho))
- **Julianna Orso** ([@Ju-Orso](https://github.com/Ju-Orso))

---

## 📚 Referências

- Aho, A. V., et al. (2006). *Compilers: Principles, Techniques, and Tools* (Dragon Book)
- [Crafting Interpreters](https://craftinginterpreters.com/) - Robert Nystrom
- [BIRL Language](https://birl-language.github.io/) - Inspiração

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✉️ Contato

**João Vitor Godinho**  
📧 joaovitor.godinho@outlook.com  
🔗 [LinkedIn](https://www.linkedin.com/in/joão-vb-godinho/)  
💻 [GitHub](https://github.com/joaov-godinho)

---

<div align="center">

**⭐ Se este projeto te fez rir E aprender sobre compiladores, dê uma estrela!**

*"COÉ PC??? Programa compilado com sucesso!"* 🤪

</div>
