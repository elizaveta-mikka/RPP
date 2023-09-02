from peewee import *

db = SqliteDatabase('database_labs.db')


class BaseModel(Model):

    class Meta:
        database = db

class Posts(BaseModel):
    class Meta:
        db_table = 'Посты и комментарии к ним'

    n_post = IntegerField()
    n_comm = IntegerField()

class Comments(BaseModel):
    class Meta:
        db_table = 'Описание комментариев'

    id_chng = ForeignKeyField(Posts)
    date = DateField()
    time = TimeField()
    text = CharField(max_length=1000)
    likes = IntegerField()

if __name__ == '__main__':
    db.create_tables([Posts])
    db.create_tables([Comments])


