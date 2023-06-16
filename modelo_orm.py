from peewee import *

sqlite_db = SqliteDatabase(
    './RUEDA_BUJAN/obras_urbanas.db', pragmas={'journal_mode': 'wal'})
try:
    sqlite_db.connect()
except OperationalError as e:
    print("Error al conectar con la BD.", e)
    exit()


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class Entorno(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "entorno"


class Etapa(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "etapa"


class Tipo(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "tipo_obra"


class AreaResponsable(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "area_responsable"


class Comuna(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "comuna"


class Barrio(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "barrio"


class LicitacionAnio(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "licitacion_anio"


class ContratacionTipo(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "contratacion_tipo"


class CuitContratista(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "cuit_contratista"


class Compromiso(BaseModel):
    nombre = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = "compromiso"


class ObrasUrbanas(BaseModel):
    entorno = ForeignKeyField(Entorno, backref="entorno")
    nombre = CharField()
    etapa = ForeignKeyField(Etapa, backref="etapa")
    tipo = ForeignKeyField(Tipo, backref="tipo")
    area_responsable = CharField()
    descripcion = TextField()
    monto_contrato = CharField()
    comuna = ForeignKeyField(Comuna, backref="comuna")
    barrio = ForeignKeyField(Barrio, backref="barrio")
    direccion = TextField()
    lat = CharField()
    lng = CharField()

    class Meta:
        db_table = "obras_urbanas.db"


# Creamos las tablas correspondientes a las clases del modelo
sqlite_db.create_tables([Entorno, Etapa, Tipo, AreaResponsable, Comuna, Barrio,
                        LicitacionAnio, ContratacionTipo, CuitContratista, Compromiso, ObrasUrbanas])
