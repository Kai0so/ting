import sys


def txt_importer(path_file):
    if path_file.endswith(".txt") is not True:
        print("Formato inválido", file=sys.stderr)
    text_list = list()
    try:
        with open(path_file) as file:
            for line in file:
                text_list.append(line.strip())
    except Exception:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    return text_list
