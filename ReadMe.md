# Working with WSDL Files with Python

The following project is a reference for creating and consuming WSDL files in Python.

WSDL (Web Service Description Language) is an XML based definition language used for describing the functionality of a 
SOAP based web service. For more information, visit [SoapUI WSDL Documentation](https://www.soapui.org/docs/soap-and-wsdl/working-with-wsdls/)

In this project, **spyne** library has been used to create a WSDL file and **zeep** library has been used to consume the service.

To run this project, clone the project and execute the following command in the root folder:
```
docker compose up --build -d
```

To view the WSDL file, open the link [http://localhost:8001/?wsdl](http://localhost:8001/?wsdl) in your browser.

Alter services.py file to explore operations defined in the WSDL file.

