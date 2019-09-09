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