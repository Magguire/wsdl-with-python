import zeep

wsdl = 'http://localhost:8001/?wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service)