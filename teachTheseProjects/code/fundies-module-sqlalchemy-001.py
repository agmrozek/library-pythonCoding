from sqlalchemy import create_engine, text

engine = create_engine('sqlite://///home/amrozek/Documents/gitrepos/library-pythonCoding/teachTheseProjects/code/data/books.db', echo=True, future=True)
conn = engine.connect()

result01 = conn.execute(text("select * from author"))
print(result01.all())
