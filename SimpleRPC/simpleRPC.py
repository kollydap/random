from xmlrpc.server import SimpleXMLRPCServer


class KeyValueServer:
    _rpc_methods = ["get", "set", "delete", "exists", "keys"]

    def __init__(self, address) -> None:
        self.data = {}
        # _we create a simple server
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for method in self._rpc_methods:
            self._serv.register_function(getattr(self, method))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


kvserv = KeyValueServer(("", 15000))
kvserv.serve_forever()
