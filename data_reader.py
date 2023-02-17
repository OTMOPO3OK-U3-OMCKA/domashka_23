def r_file(file):
    try:
        with open(f'data\{file}', 'r', encoding="utf-8") as f:
            ff = f.read().rstrip("\n")
            return ff.split("\n")
    except FileNotFoundError:
        return []
