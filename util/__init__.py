def get_file_lines_stripped(file_path):
    lines = []
    with open(file_path, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines


def get_common_elements(*collections):
    if len(collections) == 0:
        return []
    common = set(collections[0])
    for collection in collections[1:]:
        common.intersection_update(set(collection))
    return list(common)


def text_file_args(func):
    def wrapper(*args, **kwargs):
        file_lines = []
        for file_path in args:
            file_lines.append(get_file_lines_stripped(file_path))
        func(*file_lines, **kwargs)
    return wrapper
