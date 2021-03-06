#!/usr/bin/python

import sys
import sqlite3

def create_table_fasta(c, table_name):
    cmd = "create table fasta(F_Header text,\
        Seq text,\
        primary key(F_Header));"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def create_table_pos(c, table_name):
    cmd = "create table " + table_name + "(S_Header text,\
        R_start_POS int,\
        F_start_POS int,\
        primary key(S_Header));"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def create_table_sam(c, table_name):
    cmd = "create table " + table_name + "(QNAME text,\
        NUM int,\
        FLAG int,\
        REFNAME text,\
        POS int,\
        MAPQ int,\
        CIGAR text,\
        RNEXT text,\
        PNEXT int,\
        TLEN int,\
        SEQ text,\
        QUAL text,\
        TAG text,\
        FILE text,\
        primary key(QNAME, NUM));"
    c.execute(cmd)
    print("table created successfully, now inserting datas")


if __name__ == '__main__':
    file_name = "Silva.fasta"
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    create_table_fasta(c, "fasta")
    create_table_sam(c, 'sam')
    create_table_pos(c, 'startPOS')
    conn.commit()
    conn.close()