import fastapi
import pandas as pd
import uvicorn
from fastapi import FastAPI, File, UploadFile, Response
from pydantic import BaseModel

from functions.csv_to_dict_converter import convert_csv_to_dict
from functions.different_registers_finder import find_in_different_registers


class WordList(BaseModel):
    words: list


app = FastAPI(title="My API")


@app.post("/average_age_by_position")
def calculate_average_age_by_position(response: Response, csv_file: UploadFile = File(...)):
    if csv_file.content_type != 'text/csv':
        response.status_code = fastapi.status.HTTP_400_BAD_REQUEST
        return "Неверный формат файла"
    df = pd.read_csv(csv_file.file)

    csv_file.file.close()

    expected_columns = ['Имя', 'Возраст', 'Должность']
    if list(df.columns) != expected_columns:
        response.status_code = fastapi.status.HTTP_400_BAD_REQUEST
        return "Невалидный файл"
    return convert_csv_to_dict(df)


@app.post("/find_in_different_registers")
def delete_duplicates_in_different_registers(word_list: WordList):
    return find_in_different_registers(word_list.words)


if __name__ == '__main__':
    uvicorn.run("my_api:app", host="localhost", port=8080, reload=True)
