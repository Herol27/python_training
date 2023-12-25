import pandas as pd


def convert_csv_to_dict(csv_file):
    res = {}
    for i, row in csv_file.iterrows():
        if row['Должность'] in res:
            (res[row['Должность']].append(row['Возраст']))
        else:
            res[row['Должность']] = []
            res[row['Должность']].append(row['Возраст'])
    for i in res:
        res[i] = sum(res[i]) / len(res[i])
    return res


if __name__ == '__main__':
    result = convert_csv_to_dict(pd.read_csv("employees.csv"))
    print(result)
