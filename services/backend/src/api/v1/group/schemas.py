from pydantic import BaseModel


class BaseGroup(BaseModel):
	full_title: str
	short_title: str
	faculty_id: int


class GroupPublic(BaseGroup):
	id: int
	faculty_full_title: str


class GroupCreate(BaseGroup):
	...


class GroupUpdate(BaseGroup):
	...
