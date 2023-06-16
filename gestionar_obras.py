import pandas as pd
from peewee import SqliteDatabase, Model


db = SqliteDatabase("obras_urbanas.db")

class GestionarObra:
    @classmethod
    def leer_data_set(cls, dataset_path):
        df = pd.read_csv(dataset_path)
        return df

    @classmethod
    def conectar_db(cls):
        db = SqliteDatabase("obras_urbanas.db")
        return db

    @classmethod
    def mapear_orm(cls):
        db.create_tables([Obra])
        return db