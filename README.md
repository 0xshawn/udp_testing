# UDP Testing

Run Server side.

```
python3 server.py --port 1234
```

Then run Client side to check connectivity

```
python3 client.py --ip 127.0.0.1 --port 1234

OUTPUT:

Check udp on 127.0.0.1:1234
b'PONG' 0.000200s
b'PONG' 0.000606s
b'PONG' 0.000244s
b'PONG' 0.000207s
b'PONG' 0.000247s
b'PONG' 0.000464s
```
