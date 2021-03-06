import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Connection


def get_data(conn: Connection, id: int = None):
    if id is None:
        sql_query = "SELECT * FROM poems"
    else:
        sql_query = f"SELECT * FROM poems WHERE id = {id}"

    df = pd.read_sql(sql_query, con=conn)
    return df


def search_data(conn: Connection, query: str = None):
    if query is None or len(query) == 0:
        sql_query = "SELECT * FROM poems"
    else:
        lst_query = query.split(" ")
        sql_query = f"SELECT * FROM poems WHERE"
        i = 0
        for item in lst_query:
            if i > 0:
                sql_query += f" AND"
            sql_query += f" Poem LIKE '%{item}%'"
            i += 1

    df = pd.read_sql(sql_query, con=conn)
    return df


@st.cache(hash_funcs={Connection: id})
def get_connection(path: str):
    """Put the connection in cache to reuse if path does not change between Streamlit reruns.
    NB : https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
    """
    return sqlite3.connect(path, check_same_thread=False)
