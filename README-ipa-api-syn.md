# ipa-api-syn
## Exposed endpoints

- Account's cache Syncronization EndPoint: ```http://{ipalab_hostname}:8888/syn/{sAMAccount}```
- Query last syncronization result EndPoint for a given sAMAccount: ```http://{ipalab_hostname}:8888/qry/{sAMAccount}```
- Query last ```n``` syncronization results EndPoint for a given sAMAccount: ```http://{ipalab_hostname}:8888/qry/{sAMAccount}/n```

## How does it work?

The syncronization endpoint does not syncronize cache, it queue the given
sAMAccount to be processed later, it only return the queue operation status (if
was able or not to add the account to the queue), after waiting a few seconds 
(that will depende on the size of the queue and the time held by the cache
syncronization script ```ipa-sss-syn```) the process results will be available for
quering. One of the folowing four outcomes, may appear as result: 

- sAMAccount not found, this happends when the queried sAMAccount never was
  sent as parameter of the syncronization endpoint or it was the first time
  this sAMAccount was used and was not dequeued and processed yet.
- Last ```n``` query results for a sAMAccount are older than expected, this
  happends when the query is made before ```ipa-sss-syn``` was called for the given
  sAMAccount.
- Query returned succesfully the last sAMAccount but there was an error during
  cache syncronization (the enpoint return message includes all the error codes
  and output messages returned by ```ipa-sss-syn```.
- Query returned successfully with the success messages form ```ipa-sss-syn```
  process.
