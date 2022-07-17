from sqlite3 import connect

def run_query(query, parametros=()):
    try:
        with connect('DB/db.db') as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parametros)
            conn.commit()
        return resultado
    except Exception as e:

        print(e)