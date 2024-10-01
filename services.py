import zeep

# Load the WSDL file
wsdl = 'http://localhost:8001/?wsdl'
client = zeep.Client(wsdl=wsdl)


# List all operations defined in the WSDL
print("Available operations:")
for service in client.wsdl.services.values():
    for port in service.ports.values():
        operations = port.binding._operations.values()
        for operation in operations:
            print(f"Operation Name: {operation.name}")

            # Display the input message parameters
            print("Input Parameters:")
            input_message = operation.input
            # for part in input_message.signature():
            print(f" - {input_message.signature()}")

            # Display the output message parameters
            print("Output Parameters:")
            output_message = operation.output
            # for part in output_message.signature():
            print(f" - {output_message.signature()}")