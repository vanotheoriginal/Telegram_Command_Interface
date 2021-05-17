import sqlite3
from os import getcwd


def __sqlite(query: str, iter_=0):
    db_path = f'{getcwd()}/quotes.db'
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    if iter_ == 1:
        result = ''
        counter = 1
        for value in cur.execute(query):
            result = result + f'{counter}. ' + value[1] + '\n'
            counter = counter + 1
        return result
    if iter_ == 2:
        result = ''
        for value in cur.execute(query):
            result = result + f'{value[0]}. ' + value[1] + '\n'
        return result
    else:
        cur.execute(query)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result


def __sqlite_init():
    db = sqlite3.connect('quotes.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS quotes(id INTEGER PRIMARY KEY, quote TEXT)""")
    db.commit()


def __sqlite_insert(value: str):
    __sqlite(f"INSERT INTO quotes (quote) VALUES (\"{value}\")")


def __sqlite_select_all(iter_=1):
    res = __sqlite("SELECT * FROM quotes", iter_)
    return res


def __sqlite_select_last():
    res = __sqlite('SELECT * FROM quotes ORDER BY id DESC LIMIT 1')
    return f'{res[0][0]}. {res[0][1]}'


def __sqlite_clear():
    __sqlite("DELETE FROM quotes")


def __sqlite_update(new_quote: str, quote_id: int):
    __sqlite(f"UPDATE quotes SET quote = '{new_quote}' WHERE id = {quote_id};")


def __sqlite_delete_quote(quote_id: int):
    __sqlite(f"DELETE FROM quotes WHERE id = {quote_id}")


if __name__ == '__main__':
    # __sqlite_init()
    # __sqlite_clear()
    # __sqlite_delete_quote(4)
    #
    #
    # print(__sqlite_select_all(2))
    # print('Last:',__sqlite_select_last())
    pass