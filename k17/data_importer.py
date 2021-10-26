#Team02 - Renggeng Zheng Ivan Lam Lia Nelson
#SoftDev
#K17 -- The full stack -- making a wiki
#2021-10-25
#Time Spent: 40 People Minutes

from db_builder import Db_builder
from os.path import exists

db_name = "pages.db"

if exists(db_name):
	pass
else:
	dbb = Db_builder(db_name)
	dbb.create_table("subjects", {"subject":"TEXT PRIMARY KEY", "tag1":"TEXT", "tag2":"TEXT", "tag3":"TEXT"})
	dbb.fill_table("subjects", "subjects.csv")
	del dbb
