# Importing necessary libraries
import pandas as pd
import pytest


# Loading a raw dataset
@pytest.fixture
def df():
   df = pd.read_csv("data/raw/mushroom_dataset.csv")
   return df

# Checking the number of columns in the dataset
def test_columns_num(df):
   col_num = df.shape[1]
   assert col_num == 9, "Ошибка: Количество столбцов в датасете не соответствует ожидаемому"


# Checking column names in the dataset
def test_columns_names(df):
   col_names = ['cap-diameter', 'cap-shape', 'gill-attachment', 'gill-color',
                'stem-height', 'stem-width', 'stem-color', 'season', 'class']
   assert df.columns.to_list() == col_names, "Ошибка: Названия столбцов в датасете не соответствуют ожидаемому"


# Checking data types
def test_dataset_dtypes(df):
    assert df['cap-diameter'].dtype == 'int64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['cap-shape'].dtype  == 'int64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['gill-attachment'].dtype  == 'int64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['gill-color'].dtype  == 'int64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['stem-height'].dtype  == 'float64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['stem-width'].dtype  == 'int64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['stem-color'].dtype  == 'int64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['season'].dtype  == 'float64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"
    assert df['class'].dtype  == 'int64', "Ошибка: Типы данных в датасете не соответствует ожидаемому"


# Checking for missing values
def test_missing_values(df):
    assert df['cap-diameter'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['cap-shape'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['gill-attachment'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['gill-color'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['stem-height'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['stem-width'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['stem-color'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['season'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    assert df['class'].isnull().sum() == 0, "Ошибка: Датасет содержит пропущенные значения"
    

# Checking values in range
def test_range_val(df):
   assert df['gill-color'].between(0,11).any(), "Ошибка: Датасет содержит неверные значения цвета"
   assert df['stem-color'].between(0,11).any(), "Ошибка: Датасет содержит неверные значения цвета"
