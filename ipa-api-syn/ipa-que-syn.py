#!/usr/bin/env python

import sys
import os
import sqlite3
import time
import subprocess
import logging
import yaml
from yaml import load, dump, Loader, Dumper

get_acct_qry = "SELECT * FROM accounts ORDER BY timestamp ASC LIMIT 1"
del_acct_qry = "DELETE FROM accounts WHERE hash=?"
ins_acct_qry = "INSERT INTO accounts(hash,timestamp,account,action,dequeue_time,finish_time,return) VALUES(?,?,?,?,?,?,?)"
upd_acct_qry = "UPDATE accounts SET finish_time=?, return=? WHERE hash=?"

if len(sys.argv) < 2:
    print("Configuration file required.")
    print("example: ipa-que-syn.py /path/to/configuration/file")
    os._exit(1)

conffile = sys.argv[1]
with open(conffile, "r") as f:
    cfg = yaml.load(f, Loader=Loader)

db_input = cfg["db_input"]
db_processed = cfg["db_processed"]
script = cfg["script"]
escpriv = cfg["escpriv"]
consumer_log = cfg["consumer_logfile"]

logging.basicConfig(
    filename=consumer_log,
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.info("op=quesyn status=started")

while True:
    row_hash = ""
    row_time = ""
    row_acct = ""
    row_actn = ""
    with sqlite3.connect(db_input) as con_input:
        cur = con_input.cursor()
        cur.execute(get_acct_qry)
        rec = cur.fetchone()
        if rec:
            row_hash = rec[0]
            row_time = rec[1]
            row_acct = rec[2]
            row_actn = rec[3]
            script_prefix = ""

    if row_hash != "":
        logging.info("op=quesyn acct=" + row_acct + " status=processing")
        with sqlite3.connect(db_processed) as con_proc:
            con_proc.execute(
                ins_acct_qry, (row_hash, row_time, row_acct, row_actn, time.time(), 0, "")
            )
            con_proc.commit()

        logging.info("op=quesyn acct=" + row_acct + " row_actn=" + row_actn + " status=account_inserted")

        if row_actn == 'resyn':
            script_prefix = 'IPA_SSS_SYN_LAST=0 '

        if escpriv:
            script_prefix = "sudo " + script_prefix

        script_command = script_prefix + " " + script + " " + row_acct
        process = subprocess.Popen(
            script_command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()
        rc = process.returncode
        result = "stdout=" + stdout + " stderr=" + stderr
        logging.info("script_command=" + script_command)
        logging.info(
            "op=quesyn acct="
            + row_acct
            + " row_actn="
            + row_actn
            + " "
            + script_prefix
            + " status=run_script  exit_code="
            + str(rc)
            + " "
            + result
        )
        with sqlite3.connect(db_processed) as con_proc:
            con_proc.execute(upd_acct_qry, (time.time(), result, row_hash))
            con_proc.commit()

        logging.info("op=quesyn acct=" + row_acct + " status=exectime_updated")
        deleted = False
        while not deleted:
            with sqlite3.connect(db_input) as con_input:
                con_input.execute(del_acct_qry, (row_hash,))
                con_input.commit()
                deleted = True
                logging.info("op=quesyn acct=" + row_acct + " status=del_inputdb")
            if not deleted:
                time.sleep(2)
        logging.info("op=quesyn acct=" + row_acct + " status=finished")
    time.sleep(1)
