from sqlite3 import connect

db = connect('user_records.db')
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='user_query'"
if not db.execute(tb_exists).fetchone():
    db.execute('create table user_query (id INTEGER PRIMARY KEY AUTOINCREMENT, question text, answer text, helpful text, extra1 text, extra2 text, extra3 text, extra4 text, extra5 text, extra6 text, extra7 text)')
#db.execute('insert into user_query (id, question, answer, helpful) values  (2, "test2 question", "test2 answer", "yes")')
#db.commit()
#db.execute('insert into user_query (id, question) values  (%s, "%s")' % (id,sentence))
#db.commit()
#db.execute('insert into user_query (id, question) values (1, "new")')
db.commit()
