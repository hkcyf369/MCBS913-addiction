#!/usr/bin/python

import sys
import sqlite3


def create_table(c, table_name):
    cmd = "create or replace table fasta (INFO,text\
        SEQ text,\
        START int,\
        END int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")


def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + \
        "(INFO, SEQ, START, END) VALUES (?,?,?,?);"
    c.execute(cmd, data)


if __name__ == '__main__':
    file_name = sys.argv[i]
    c = 0
    with open(file_name, "r") as pos_file:
        for line in pos_file:
            fields = line.split(" ")
            Query = None
            if '>'in fields[0]:
                if Query != None:
                    print("reference: ", Reference)
                    print("query: ", Query)
                Reference = fields[0]
            else:
                Query = Query + line.replace('/n','')
                