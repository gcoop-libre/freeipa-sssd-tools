# `ipa-api-syn`

## How does it work?

The synchronization endpoint does not synchronize cache, it queue the
given `sAMAccount` to be processed later, it only return the queue
operation status (if was able or not to add the account to the queue),
after waiting a few seconds (that will depend on the size of the queue
and the time held by the cache synchronization script `ipa-sss-syn`) the
process results will be available for querying. One of the following
four outcomes, may appear as result:

- `sAMAccount` not found, this happens when the queried `sAMAccount`
  never was sent as parameter of the synchronization endpoint or it was
  the first time this `sAMAccount` was used and was not dequeued and
  processed yet.

- Last `n` query results for a `sAMAccount` are older than expected,
  this happens when the query is made before `ipa-sss-syn` was called
  for the given `sAMAccount`.

- Query returned successfully the last `sAMAccount` but there was an
  error during cache synchronization (the _EndPoint_ return message
  includes all the error codes and output messages returned by
  `ipa-sss-syn`.

- Query returned successfully with the success messages from
  `ipa-sss-syn` process.

\pagebreak

## Exposed _EndPoints_

### Account's cache synchronization _EndPoint_

Request: `http://{ipa_hostname}:8888/syn/{sAMAccount}`

Example Response:

```json
{
    "hash": "c490e266779319b2bbb9f4e10e1c6d79",
    "retval": "OK",
    "sAMAccount": "admin",
    "time": 1645789938.802653
}
```

### Query last synchronization result _EndPoint_

Request: `http://{ipa_hostname}:8888/qry/{sAMAccount}`

Example Response:

```json
{
    "items": "1",
    "result": [
        {
            "account": "admin",
            "dequeue_time": "2022-02-25 08:52:18",
            "finish_time": "2022-02-25 08:52:20",
            "hash": "c490e266779319b2bbb9f4e10e1c6d79",
            "item": "1",
            "result": "",
            "timestamp": "2022-02-25 08:52:18"
        }
    ],
    "retval": "OK"
}
```

\pagebreak

### Query last `n` synchronization results _EndPoint_

Request: `http://{ipa_hostname}:8888/qry/{sAMAccount}/n`

Example Response:

```json
{
    "items": "2",
    "result": [
        {
            "account": "admin",
            "dequeue_time": "2022-02-25 08:52:18",
            "finish_time": "2022-02-25 08:52:20",
            "hash": "c490e266779319b2bbb9f4e10e1c6d79",
            "item": "1",
            "result": "",
            "timestamp": "2022-02-25 08:52:18"
        },
        {
            "account": "admin",
            "dequeue_time": "2022-02-25 08:52:11",
            "finish_time": "2022-02-25 08:52:13",
            "hash": "1d0309af7c805756225edc7982218dd6",
            "item": "2",
            "result": "",
            "timestamp": "2022-02-25 08:52:10"
        }
    ],
    "retval": "OK"
}
```
