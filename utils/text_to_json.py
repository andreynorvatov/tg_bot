import json

cenz_list = []
cenz_source_path = 'utils/cenz_source.txt'
cenz_json_path = 'utils/cenz.json'

try:
    with open(cenz_source_path, encoding='utf-8') as source_file:
        for word in source_file:
            cenz_list.append(word.lower().split('\n')[0])


    with open(cenz_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(cenz_list, json_file)

    print('done')

except FileNotFoundError:
    print(f'Отсутствует файл {cenz_source_path}')