import time

import pymysql
import datetime


class dbUtil():
    def __init__(self):
        conn, cursor = self.get_conn()
        self.conn = conn
        self.cursor = cursor

    def get_time(self):
        time_str = time.strftime("%Y{}%m{}%d{} %X")
        return time_str.format("year", "month", "day")

    def get_conn(self):
        # establish a connection
        conn = pymysql.connect(host="127.0.0.1", user="root", password="liding2008", db="data", charset="utf8")
        # cCreate cursor A
        cursor = conn.cursor()
        return conn, cursor

    def close_commit(self):
        self.conn.commit()
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def close(self):
        self.conn.commit()
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def query(self, sql, *args):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        return res

    def query_noargs(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res


# Get the next n days
def get_day(n=1):
    second_date = (datetime.datetime.now() + datetime.timedelta(days=n)).strftime("%Y-%m-%d")
    return second_date
