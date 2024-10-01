from spyne import Application, rpc, ServiceBase, Integer, Unicode, ComplexModel
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Integer
from spyne.model.complex import ComplexModel

class NumberToWordsInput(ComplexModel):
    __namespace__ = "http://example.com/numberconversion"
    number = Integer

class NumberToWordsOutput(ComplexModel):
    __namespace__ = "http://example.com/numberconversion"
    result = Unicode

class NumberConversionService(ServiceBase):
    @rpc(NumberToWordsInput, _returns=NumberToWordsOutput, _out_message_name="NumberToWordsResponse")
    def NumberToWordsRequest(self, request):
        number = request.number
        # Here you would implement the logic to convert number to words
        # For simplicity, returning a placeholder string
        return NumberToWordsOutput(result=f"Number in words for {number}")

# Create the application
application = Application(
    [NumberConversionService],
    tns='http://example.com/numberconversion',
    name='NumberConversionService',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

if __name__ == '__main__':

    # Wrap the application in a WSGI application
    wsgi_app = WsgiApplication(application)

    # Start a simple server
    server = make_server('localhost', 8001, wsgi_app)
    print("Server is running on http://localhost:8001/?wsdl...")
    server.serve_forever()
