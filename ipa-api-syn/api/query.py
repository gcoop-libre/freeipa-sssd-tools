from flask_restful import Resource, Api
from flask import jsonify, request, current_app
import sqlite3
import time
import hashlib
import logging
import random

class Query(Resource):
    def get(self, userid):
        sqlqry = "SELECT * FROM accounts WHERE account=? ORDER BY timestamp"
        current_app.config.from_pyfile('config/settings.py')
        logging.basicConfig(filename=current_app.config["LOGFILE"], 
                            filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO,
                            datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("op=qry acct="+userid+" status=recived")
        with sqlite3.connect(current_app.config["DBPROCS"]) as con:
            cur = con.cursor()
            cur.execute(sqlqry,userid)
            rec = cur.fetchone()
            if rec:
                logging.info("op=qry acct="+userid+" status=success")
                return jsonify({'retval':"OK",
                                'hash':rec[0],
                                'timestamp':rec[1],
                                'account':rec[2],
                                'dequeue_time':rec[3],
                                'finish_time':rec[4],
                                'result':rec[5]
                                })
            else:
                logging.warning("op=qry acct="+userid+" status=account not found")
                return jsonify({'retval':"Error",
                                'hash':"-",
                                'timestamp':"-",
                                'account':"-",
                                'dequeue_time':"-",
                                'finish_time':"-",
                                'result':"Account not found"
                                })
