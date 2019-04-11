from xmlrpc.server import SimpleXMLRPCServer

class	funciones_remota:
	def suma(self, x, y):
		return x+y
	def resta(self, x, y):
		return x-y
	def multi(self, x, y):
		return x*y
	def div(self, x, y):
		return x/y
	def pot(self, x, y):
		return x**y
	
	
server = SimpleXMLRPCServer(("192.168.8.180", 8001))
server.register_instance(funciones_remota(), "funciones")
print ("Hola amigos, soy el servidor y estoy corriendo por el puerto 8001")
server.serve_forever()
