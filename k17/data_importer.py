import db_builder
from os.path import exists

db_name = "pages.db"

if exists(db_name):
	pass
else:
	dbb = Db_builder(db_name)
	dbb.create_table("subjects", {"subject":"TEXT PRIMARY KEY", "tag1":"TEXT", "tag2":"TEXT", "tag3":"TEXT"})
	dbb.fill_table("subjects", "subjects.csv")
	del dbb
