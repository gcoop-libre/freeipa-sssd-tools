from flask_restful import Resource, Api
from flask import jsonify, request, current_app
import sqlite3
import time
import hashlib
import logging
import random
import datetime

class Query(Resource):
    def get(self, userid, recordnum = 1):
        sqlqry = "SELECT * FROM accounts WHERE account=? ORDER BY timestamp DESC"
        current_app.config.from_pyfile('config/settings.py')
        logging.basicConfig(filename=current_app.config["LOGFILE"], 
                            filemode='w',
                            format='%(asctime)s - %(levelname)s - usr=%(name)s %(message)s',
                            level=logging.INFO,
                            datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("op=qry acct="+userid+" status=recived")
        with sqlite3.connect(current_app.config["DBPROCS"]) as con:
            cur = con.cursor()
            cur.execute(sqlqry,(userid,))
            rec = cur.fetchmany(recordnum)
            return_list = []
            count = 0
            for row in rec:
                count += 1
                return_list.append({
                    'item':str(count),
                    'hash':row[0],
                    'timestamp':datetime.datetime.fromtimestamp(row[1]).strftime('%Y-%m-%d %H:%M:%S'),
                    'account':row[2],
                    'dequeue_time':datetime.datetime.fromtimestamp(row[3]).strftime('%Y-%m-%d %H:%M:%S'),
                    'finish_time':datetime.datetime.fromtimestamp(row[4]).strftime('%Y-%m-%d %H:%M:%S'),
                    'result':row[5],
                    })

            if len(return_list) > 0:
                logging.info("op=qry acct="+userid+" records="+str(recordnum)+" status=success")
                ''' return_list = "["+return_list+"]" '''
                return jsonify({'retval':"OK",
                                'items':str(count),
                                'result':return_list
                                })

            else:
                logging.warning("op=qry acct="+userid+" status=account not found")
                return jsonify({'retval':"Error",
                                'result':"Account not found"
                                })
