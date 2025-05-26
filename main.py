import os
import subprocess
from fsl_lexer import tokenize
from fsl_parser import Parser
from fsl_transpiler import Transpiler

def compile_c_code(c_filepath, executable_filepath):
    """Compila o código C usando GCC."""
    compile_command = ['gcc', c_filepath, '-o', executable_filepath, '-lm'] 
    try:
        print(f"\n--- Compilando Código C ---")
        print(f"Comando: {' '.join(compile_command)}")
        process = subprocess.run(compile_command, capture_output=True, text=True, check=True)
        if process.stderr:
            print(f"Saída do Compilador (Warnings):\n{process.stderr}")
        print(f"Código C compilado com sucesso para: {executable_filepath}")
        return True
    except FileNotFoundError:
        print("Erro: Compilador GCC não encontrado. Verifique se está instalado e no PATH do sistema.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Erro durante a compilação do C (Comando: {' '.join(e.cmd)}):\n{e.stderr}")
        return False
    except Exception as e:
        print(f"Erro inesperado durante a compilação do C: {e}")
        return False

def run_executable(executable_filepath):
    """Executa o programa compilado e captura sua saída."""
    try:
        print(f"\n--- Executando Programa FSL (via C) ---")
        print(f"Executando: {executable_filepath}")
        process = subprocess.run([executable_filepath], capture_output=True, text=True, check=False, encoding='utf-8', errors='replace')
        print("--- Saída do Programa ---")
        if process.stdout:
            print(process.stdout, end='')
        if process.stderr:
            print(f"--- Erros na Execução (stderr) ---\n{process.stderr}", end='')
        print("-------------------------")
        if process.returncode != 0:
            print(f"O programa terminou com código de erro: {process.returncode}")
        return True
    except FileNotFoundError:
        print(f"Erro: Executável '{executable_filepath}' não encontrado. A compilação pode ter falhado.")
        return False
    except Exception as e:
        print(f"Erro ao executar o programa: {e}")
        return False

def main():
    fsl_file_path = input("Digite o caminho para o arquivo .fsl (ou deixe em branco para 'exemplos/ola_felipe.fsl'): ")
    if not fsl_file_path:
        fsl_file_path = "exemplos/ola_felipe.fsl" # Arquivo padrão

    if not os.path.exists(fsl_file_path):
        print(f"Erro: Arquivo FSL '{fsl_file_path}' não encontrado.")
        return

    base_name = os.path.splitext(os.path.basename(fsl_file_path))[0]
    c_file_path = f"{base_name}_temp.c"
    executable_name = f"{base_name}_exec"
    executable_path = os.path.join(os.path.dirname(fsl_file_path) or '.', executable_name)
    if os.name == 'nt': 
        executable_path_os_specific = executable_path + ".exe"
    else:
        executable_path_os_specific = executable_path


    try:
        with open(fsl_file_path, 'r', encoding='utf-8') as f:
            fsl_code = f.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo FSL: {e}")
        return

    print("--- Código FSL Original ---")
    print(fsl_code)
    print("-------------------------\n")

    # 1. Análise Léxica
    try:
        tokens = tokenize(fsl_code)
        print("--- Tokens Gerados ---")
        print(f"{len(tokens)} tokens gerados.")
        print("----------------------\n")
    except Exception as e:
        print(f"Erro no Lexer: {e}")
        return

    # 2. Análise Sintática
    parser = Parser(tokens)
    try:
        ast = parser.parse()
        print("--- AST Gerada (Representação) ---")
        print(f"Nó Raiz: {type(ast).__name__}, com {len(ast.statements if hasattr(ast, 'statements') else [])} nós filhos.")
        print("----------------------------------\n")
    except SyntaxError as e:
        print(f"Erro de Sintaxe FSL: {e}")
        return
    except Exception as e:
        print(f"Erro inesperado no Parser: {e}")
        import traceback
        traceback.print_exc()
        return

    # 3. Geração de Código C (Transpilação)
    transpiler = Transpiler()
    try:
        c_code = transpiler.transpile(ast)
        print("--- Código C Gerado (Transpilado) ---")
        print(f"Código C gerado com {len(c_code.splitlines())} linhas.")
        print("-----------------------------------\n")

        with open(c_file_path, 'w', encoding='utf-8') as f:
            f.write(c_code)
        print(f"Código C salvo temporariamente em: {c_file_path}")

    except Exception as e:
        print(f"Erro na Transpilação: {e}")
        import traceback
        traceback.print_exc()
        return

    # 4. Compilação do Código C Gerado
    if not compile_c_code(c_file_path, executable_path_os_specific):
        if os.path.exists(c_file_path):
            os.remove(c_file_path)
        return

    # 5. Execução do Programa Compilado
    run_executable(executable_path_os_specific)

    # 6. Limpeza
    print("\n--- Limpeza ---")
    try:
        if os.path.exists(c_file_path):
            os.remove(c_file_path)
            print(f"Arquivo C temporário '{c_file_path}' removido.")
        if os.path.exists(executable_path_os_specific):
            os.remove(executable_path_os_specific)
            print(f"Executável '{executable_path_os_specific}' removido.")
    except Exception as e:
        print(f"Erro durante a limpeza: {e}")

if __name__ == "__main__":
    main()