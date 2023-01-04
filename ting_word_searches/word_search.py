def exists_word(word, instance):
    search_info = []
    occurrences = []
    for queue in instance.queue:
        file_lines = queue["linhas_do_arquivo"]
        file_name = queue["nome_do_arquivo"]
        for line in file_lines:
            if word.lower() in line.lower():
                occurrences.append({"linha": file_lines.index(line) + 1})
        occurrence_result = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": occurrences
        }
        search_info.append(occurrence_result)
    if len(occurrences) < 1:
        return []
    return search_info


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
