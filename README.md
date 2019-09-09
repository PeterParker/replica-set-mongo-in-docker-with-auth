### Test 1, WORKING - Replica Set without Auth

```bash
docker-compose run --rm test-no-auth
```

Runs without error.

### Test 2, NOT WORKING - Replica Set with Auth

```bash
docker-compose run --rm test-auth
```

Produces:

```bash
Traceback (most recent call last):
  File "/test-auth.py", line 12, in <module>
    client.admin.command('ismaster')
  File "/usr/local/lib/python3.7/site-packages/pymongo/database.py", line 730, in command
    read_preference, session) as (sock_info, slave_ok):
  File "/usr/local/lib/python3.7/contextlib.py", line 112, in __enter__
    return next(self.gen)
  File "/usr/local/lib/python3.7/site-packages/pymongo/mongo_client.py", line 1299, in _socket_for_reads
    server = self._select_server(read_preference, session)
  File "/usr/local/lib/python3.7/site-packages/pymongo/mongo_client.py", line 1254, in _select_server
    server = topology.select_server(server_selector)
  File "/usr/local/lib/python3.7/site-packages/pymongo/topology.py", line 231, in select_server
    address))
  File "/usr/local/lib/python3.7/site-packages/pymongo/topology.py", line 189, in select_servers
    selector, server_timeout, address)
  File "/usr/local/lib/python3.7/site-packages/pymongo/topology.py", line 205, in _select_servers_loop
    self._error_message(selector))
pymongo.errors.ServerSelectionTimeoutError: No replica set members match selector "Primary()"
```

The docker logs for the database include the following

```
/usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init-replica-set.sh
MongoDB shell version v4.2.0
connecting to: mongodb://127.0.0.1:27017/admin?compressors=disabled&gssapiServiceName=mongodb
2019-09-09T20:27:45.203+0000 I  NETWORK  [listener] connection accepted from 127.0.0.1:38246 #3 (1 connection now open)
2019-09-09T20:27:45.204+0000 I  NETWORK  [conn3] received client metadata from 127.0.0.1:38246 conn3: { application: { name: "MongoDB Shell" }, driver: { name: "MongoDB Internal Client", version: "4.2.0" }, os: { type: "Linux", name: "Ubuntu", architecture: "x86_64", version: "18.04" } }
Implicit session: session { "id" : UUID("4a92dfec-6b15-4d6c-80c6-f12e8f272137") }
MongoDB server version: 4.2.0
{
	"ok" : 0,
	"errmsg" : "This node was not started with the replSet option",
	"code" : 76,
	"codeName" : "NoReplicationEnabled"
}
bye
```