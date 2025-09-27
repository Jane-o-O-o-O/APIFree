def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def save_results(results, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(results)