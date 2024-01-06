from zeep import Client

# Replace this URL with the actual URL of your WSDL file
wsdl_url = 'http://localhost:8000/?wsdl'

# Create a Zeep client using the WSDL URL
client = Client(wsdl_url)

# Call the 'add' service
result = client.service.add(5, 3)
print(f"Result of add service: {result}")

# Call the 'subtract' service
result = client.service.subtract(10, 4)
print(f"Result of subtract service: {result}")

# Get a reference to the HelloWorldService
hello_service = client.bind('HelloWorldService')

# Call the 'say_hello' method
name = 'GCARNAB'
times = 1
result = hello_service.say_hello(name, times)

# Print the result
for greeting in result:
    print(greeting)