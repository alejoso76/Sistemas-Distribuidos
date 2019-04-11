from xmlrpc.server import SimpleXMLRPCServer
usuarios=[]
funciones=False
class	login:
	def registro(self, x, y):
		for i in usuarios:
			if i[0]==x:
				return ("Usuario ya existente. Intente con otro usuario.")
		usuarios.append([x, y.encode('utf-8')])
		return("Registro exitoso.")

	def validacion(self, x, y):
		n=False
		for i in usuarios:
			if i[0]==x:
				n=True
				if i[1].decode('utf-8')==y:
					funciones=True
					return("Hola "+str(i[0])+", bienvenido a tu SERV-ER.")
		if not n:
			return ("Usuario no existente")
		return("Contrasena incorrecta")

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
	def salir(self):
		return("BYE")

server = SimpleXMLRPCServer(("192.168.8.180", 8001))
if funciones:
	server.register_instance(funciones_remota(), "func")
else:
	server.register_instance(login(), "login")
print ("Hi, I'm SERV-ER running on port 8001.")
server.serve_forever()
