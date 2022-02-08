from flask_restful import Resource, Api
from flask import jsonify, request, current_app
import sqlite3
import time
import hashlib
import logging
import random

class Sync(Resource):
    def get(self, userid):
        ''' userid is sAMAccount '''
        sqlqry = "INSERT INTO accounts VALUES (?,?,?)"
        current_app.config.from_pyfile('config/settings.py')
        logging.basicConfig(filename=current_app.config["LOGFILE"],
                            filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO,
                            datefmt='%Y-%m-%d %H:%M:%S')
        con = sqlite3.connect(current_app.config["DBINPUT"])
        cur = con.cursor()
        run = True
        retval = "Error"
        cnt = 1
        logging.info("op=sync acct="+userid+" status=synching")
        while run:
            random.seed(time.time())
            time.sleep(random.randint(1,1000)/1000)
            str2hash = str(time.time()) + userid + str(random.randint(0,1000))
            row = (hashlib.md5(str2hash.encode()).hexdigest(), time.time(), userid)
            try:
                with con:
                    cur.execute(sqlqry, row)
                    con.commit()
                    run = False
                    logging.info("op=sync acct="+userid+" status=queued")
            except sqlite3.OperationalError:
                logging.warning("op=sync acct="+ userid+" status=SQLite3 Operational Error")
                time.sleep(1)
        con.close()
        if not run:
            retval = "OK"
        return jsonify({'retval':retval,
                        'hash':row[0],
                        'time':row[1],
                        'sAMAccount':row[2]
                        })
