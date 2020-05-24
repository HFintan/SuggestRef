import pymysql

conn = None

def connect():
    global conn
    conn = pymysql.connect(host="localhost",user="root",password="d4t4mysql",db="SUGGEST_REF",cursorclass=pymysql.cursors.DictCursor)

def by_msc(code):
        if (not conn):
            connect();
        query="SELECT * FROM MSC_CODES WHERE msc = %s" % ("'"+code+"'", )

        with conn:
            cursor = conn.cursor()
            cursor.execute(query)
            x = cursor.fetchall()
            return x

def by_partial_msc(partial_code):
        if (not conn):
            connect();
        query="SELECT * FROM MSC_CODES WHERE msc LIKE %s" % ("'"+partial_code+"%'", )
        print(query)

        with conn:
            cursor = conn.cursor()
            cursor.execute(query)
            x = cursor.fetchall()
            return x

