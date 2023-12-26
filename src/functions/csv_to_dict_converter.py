import pandas as pd


def convert_csv_to_dict(csv_file: pd.DataFrame):
    result_dictionary = dict()
    for i, row in csv_file.iterrows():
        if row['Должность'] in result_dictionary:
            if row['Возраст'] >= 0:
                result_dictionary[row['Должность']].append(row['Возраст'])
        else:
            result_dictionary[row['Должность']] = []
            if row['Возраст'] >= 0:
                result_dictionary[row['Должность']].append(row['Возраст'])
    for i in result_dictionary:
        result_dictionary[i] = sum(result_dictionary[i]) / len(result_dictionary[i]) if result_dictionary[i] else None
    return result_dictionary


if __name__ == '__main__':
    df = pd.read_csv("../testfiles/employees.csv")
    result = convert_csv_to_dict(df)
    print(result)
