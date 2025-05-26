# Felipe Smith Language (FSL) 🤪

**Transformando o meme Felipe Smith em código executável! "COÉ PC???"**

## 🚀 Por Trás do Código

Inspirado no meme Felipe Smith e no já memético [birl-language](https://birl-language.github.io/), este projeto nasceu como uma forma divertida e (educativa) de explorar os conceitos da disciplina de Compiladores.

O objetivo? Pegar as frases de efeito, os momentos de angústia e as pérolas de sabedoria de Felipe Smith e transformá-los em uma linguagem de programação funcional. Sim, "ensinamos" o computador a entender  "Eu juro vo sair cagando" como o início de tudo!

## 🗣️ O que é a Felipe Smith Language (FSL)?

A FSL é uma linguagem de programação imperativa, onde as palavras-chave, tipos de dados, e estruturas de controle da linguagem C foram substituídas por frases que viralizaram no meme Felipe Smith.

**Alguns exemplos da sintaxe da FSL:**

* **Início do programa:** `Eu juro vo sair cagando`
* **Fim do programa (com sucesso):** `Ta branco tiro na cabeça`
* **Declarar um inteiro:** `14 minhaIdade;`
* **Exibir algo na tela:** `Que foi cabeleira? ("Minha mensagem aqui!");`
* **Estrutura condicional (IF/ELSE):**
    ```fsl
    Debaixo da ponte? (condicao)
        // Código se verdadeiro
    Faz isso comigo não velho // Equivale ao ELSE
        // Código se falso
    Seu cu // Fim do bloco IF ou ELSE
    ```
* **Outros "comandos" incluem:**
    * Tipos: `14` (int), `16` (float), `Smith` (char), `Red Bull?` (double), `Katrina` (void)
    * Loops (WIP): `5Km?` (while), `Rave, RAVE?!` (for)
    * E muito mais pérolas sendo implementadas!

## 🛠️ Como Essa Mágica Acontece? (Visão Técnica)

Por baixo de toda a zueira, existe um processo de compilação (ou melhor, transpilação) bem definido:

1.  **Linguagem de Implementação:** O "compilador" da FSL é inteiramente escrito em **Python 3**.
2.  **Análise Léxica:** O código fonte escrito em FSL é lido e quebrado em uma sequência de "tokens". Cada token representa uma frase de meme ou um operador conhecido (ex: `Debaixo da ponte?` vira um token `T_IF`).
3.  **Análise Sintática:** Os tokens são analisados para verificar se a sequência forma uma estrutura gramaticalmente válida na FSL. O resultado dessa análise é, conceitualmente, uma Árvore Sintática Abstrata (AST) que representa a lógica do programa.
4.  **Transpilação para C:** A AST é percorrida e cada nó (representando uma instrução ou expressão FSL) é traduzido para seu equivalente em código **Linguagem C**. É aqui que "Guarapari - Buzios é minha arte" vira lógica de verdade!
5.  **Compilação e Execução do Código C:**
    * O código C gerado é salvo em um arquivo `.c`.
    * Um compilador C padrão (como o **GCC**) é invocado automaticamente pelo script Python para compilar esse arquivo `.c` em um programa executável.
    * Finalmente, o script Python executa esse programa compilado, e a saída do seu código FSL é exibida no console.

Basicamente, a FSL não é executada diretamente, mas sim traduzida para C, que então é compilado e executado – tudo de forma transparente para o usuário (depois de configurado, claro!).

## 💻 Tecnologias e Ferramentas Utilizadas

* **Python 3.x:** Linguagem principal para o desenvolvimento do tradutor FSL.
    * Módulos Python notáveis: `re` (expressões regulares para o lexer), `subprocess` (para invocar o GCC e executar o código compilado), `os`.
* **Linguagem C:** A linguagem alvo da nossa transpilação. O código FSL se transforma em código C funcional.
* **GCC (GNU Compiler Collection):** Ou qualquer outro compilador C compatível, necessário para compilar o código C gerado e permitir a execução dos programas FSL.

## 🎯 Status Atual do Projeto (Exemplo - Atualize conforme o progresso!)

* ✅ Analisador Léxico capaz de reconhecer os principais "memes-comandos".
* ✅ Analisador Sintático para estruturas básicas como:
    * Início e Fim de programa.
    * Declaração de tipos de dados básicos (`14`, `16`, `Smith`, `Red Bull?`, `Katrina`).
    * Comando de escrita na tela (`Que foi cabeleira?`).
    * Estruturas condicionais `IF` e `IF/ELSE` (`Debaixo da ponte?`, `Faz isso comigo não velho`, `Seu cu`).
* ✅ Transpilador funcional para as estruturas acima, gerando código C equivalente.
* ✅ Orquestração completa: O script `main.py` lê um arquivo `.fsl`, traduz, compila o C com GCC e executa o resultado.
* 🚧 Em desenvolvimento: Loops `WHILE` (`5Km?`) e `FOR` (`Rave, RAVE?!`), declaração e chamada de funções (`Minha arte`).

## 🚀 Como Rodar essa "Obra de Arte"

1.  **Pré-requisitos Indispensáveis (Favor não ignorar, "pelo amor de deus"):**
    * **Python 3.x** instalado no seu sistema.
    * Um **Compilador C (como o GCC)** instalado e configurado corretamente no PATH do seu sistema operacional. (Sem isso, o passo de compilar o C gerado vai falhar com "Compilador GCC não encontrado").
2.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/joaov-godinho/smith-language.git
    cd smith-language
    ```
3.  **Execute o Script Principal:**
    No terminal, dentro da pasta do projeto, rode:
    ```bash
    python main.py
    ```
4.  O script solicitará o caminho para um arquivo `.fsl`. Você pode:
    * Digitar o caminho para seu próprio arquivo FSL.
    * Apenas pressionar Enter para usar o arquivo de exemplo padrão (geralmente `exemplos/ola_felipe.fsl`).
5.  Aprecie (ou depure) a mágica acontecendo!

## 🔮 Próximos Passos e Ideias para o "PC Gusmão" Implementar

* Implementar completamente os laços de repetição `WHILE` (`5Km?`) e `FOR` (`Rave, RAVE?!`).
* Suporte completo à declaração e chamada de funções (`Minha arte`, `Da o cu NOME_FUNCAO()`).
* Melhorar o sistema de tratamento de erros, com mensagens quem sabe... mais meméticas?
* Expandir o suporte a expressões aritméticas e lógicas complexas.
* Criar uma documentação mais detalhada para a sintaxe da FSL (se é que isso é possível para algo tão caótico 😂).
* Testes, muitos testes! "Quebro meu braço, tá branco véi!" se não testar.

## 🏆 Equipe da "Rave" (Autores)

* João Vitor Borges Godinho (joaov-godinho)
* Julianna Orso ()

---
