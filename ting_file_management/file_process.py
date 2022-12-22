from .file_management import txt_importer
import sys


def process(path_file, instance):
    text_lines = txt_importer(path_file)
    if text_lines not in instance.queue:
        instance.enqueue(text_lines)
    processed_data = dict(
        nome_do_arquivo=path_file,
        qtd_linhas=len(text_lines),
        linhas_do_arquivo=text_lines,
    )
    print(processed_data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
