import csv

def read_csv():
    with open('data/especialidades.csv', 'r', encoding='latin-1') as file:
        list_dicts = []
        reader = list(csv.reader(file, delimiter=';'))
        for row in reader:
            dict = {'especializacao': row[0].strip(), 'regioes': []}
            for i,column in enumerate(row):
                if column:
                    if i != 0 and i != 18:
                        dict['regioes'].append(reader[3][i].strip())
            print(dict)

    return
