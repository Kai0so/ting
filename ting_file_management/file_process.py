from .file_management import txt_importer
import sys


def process(path_file, instance):
    text_lines = txt_importer(path_file)
    file_exists = False
    for queue in instance.queue:
        queue_path = queue["nome_do_arquivo"]
        if path_file == queue_path:
            file_exists = True
            break
    if file_exists is False:
        processed_data = dict(
            nome_do_arquivo=path_file,
            qtd_linhas=len(text_lines),
            linhas_do_arquivo=text_lines,
        )
        instance.enqueue(processed_data)
        print(processed_data, file=sys.stdout)


def remove(instance):
    queue_size = instance.__len__()
    if queue_size == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        dequeue = instance.dequeue()
        path_file = dequeue["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    last_position = instance.__len__() - 1
    if position < 0 or position > last_position:
        print("Posição inválida", file=sys.stderr)
    else:
        selected_queue = instance.search(position)
        print(selected_queue, file=sys.stdout)
