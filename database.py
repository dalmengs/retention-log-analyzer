import sqlite3
import os
from dotenv import load_dotenv
from test import make_test_data

load_dotenv()

class Database:
    _conn = sqlite3.connect(os.environ.get("DB_DIRECTORY"))

    def __init__(self, test_environment: bool):
        self._create_table()
        if test_environment:
            self._make_sample_data()
    
    def insert_authentication_log(self, session_id, user_id, serial_number, token, is_auth_succeed, msg, created_at):
        cursor = self._conn.cursor()
        cursor.execute('insert into auth_log (session_id, user_id, serial_number, token, is_auth_succeed, msg, created_at) values (?, ?, ?, ?, ?, ?, ?)',(
            session_id,
            user_id,
            serial_number,
            token,
            is_auth_succeed,
            msg,
            created_at
        ))
        self._conn.commit()
    
    def insert_one_turn_log(self, request_id, session_id, user_id, created_at, user_chat, naly_chat):
        cursor = self._conn.cursor()
        cursor.execute('insert into one_turn_log (request_id, session_id, user_id, created_at, user_chat, naly_chat) values (?, ?, ?, ?, ?, ?)',(
            request_id,
            session_id,
            user_id,
            created_at,
            user_chat,
            naly_chat
        ))
        self._conn.commit()
    
    def insert_performance_log(self, request_id, session_id, user_id, component_id, data, execution_time):
        cursor = self._conn.cursor()
        cursor.execute('insert into performance_log (request_id, session_id, user_id, component_id, data, execution_time) values (?, ?, ?, ?, ?, ?)',(
            request_id,
            session_id,
            user_id,
            component_id,
            data,
            execution_time
        ))
        self._conn.commit()
    
    def insert_summary_log(self, session_id, summary, summary_type, user_id, created_at):
        cursor = self._conn.cursor()
        cursor.execute('insert into summary_log (session_id, summary, summary_type, user_id, created_at) values (?, ?, ?, ?, ?)',(
            session_id,
            summary,
            summary_type,
            user_id,
            created_at
        ))
        self._conn.commit()

    def _make_sample_data(self):
        cursor = self._conn.cursor()
        test_data = make_test_data()
        for data in test_data["auth"]:
            cursor.execute('insert into auth_log (session_id, user_id, serial_number, token, is_auth_succeed, msg, created_at) values (?, ?, ?, ?, ?, ?, ?)',(
                data["session_id"],
                data["user_id"],
                data["serial_number"],
                data["token"],
                data["is_auth_succeed"],
                data["msg"],
                data["created_at"],
            ))
        for data in test_data["one_turn"]:
            cursor.execute('insert into one_turn_log (request_id, session_id, user_id, created_at, user_chat, naly_chat) values (?, ?, ?, ?, ?, ?)',(
                data["request_id"],
                data["session_id"],
                data["user_id"],
                data["created_at"],
                data["user_chat"],
                data["naly_chat"],
            ))
        for data in test_data["performance"]:
            cursor.execute('insert into performance_log (request_id, session_id, user_id, component_id, data, execution_time) values (?, ?, ?, ?, ?, ?)',(
                data["request_id"],
                data["session_id"],
                data["user_id"],
                data["component_id"],
                data["data"],
                data["execution_time"],
            ))
        for data in test_data["summary"]:
            cursor.execute('insert into summary_log (session_id, summary, summary_type, user_id, created_at) values (?, ?, ?, ?, ?)',(
                data["session_id"],
                data["summary"],
                data["summary_type"],
                data["user_id"],
                data["created_at"],
            ))
        self._conn.commit()

    def _create_table(self):
        cursor = self._conn.cursor()
        cursor.execute("""
            create table if not exists auth_log(
                session_id      text not null,
                user_id         text,
                serial_number   text not null,
                token           text not null,
                is_auth_succeed bool not null,
                msg             text,
                created_at      text not null
            )
        """)
        cursor.execute("""
            create table if not exists one_turn_log(
                request_id      text primary key,
                session_id      text not null,
                user_id         text not null,
                created_at      text not null,
                user_chat       text not null,
                naly_chat       text not null
            )
        """)
        cursor.execute("""
            create table if not exists performance_log(
                request_id      text not null,
                session_id      text not null,
                user_id         text not null,
                component_id    int not null,
                data            text,
                execution_time  int not null,
                foreign key (request_id) references one_turn_log (request_id)
            )
        """)
        cursor.execute("""
            create table if not exists summary_log(
                session_id      text not null,
                summary         text not null,
                summary_type    int not null,
                user_id         text not null,
                created_at      text not null
            )
        """)
        self._conn.commit()
