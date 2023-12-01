from sqlalchemy.orm import Session
from datetime import datetime, timezone
from typing import List

from crud.base import CRUDBase
from models.text import Text
from schemas.text import ReadText, CreateUpdateText


class CRUDText(CRUDBase[Text, ReadText, CreateUpdateText]):
    pass

text_crud = CRUDText(Text)



