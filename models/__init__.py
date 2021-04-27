from .base_model import BaseModel
from .notebook import Notebook
from .note import Note


def create_tables():
    db = BaseModel._meta.database
    if not db.get_tables():
        db.create_tables([Notebook, Note])
    if not Notebook.select().count():
        Notebook.create(name='默认便签集', description='系统创建的默认便签集')
