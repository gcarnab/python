from suds.client import Client

# Define the URL to the WSDL file of the SOAP service
wsdl_url = 'http://localhost:8000/?wsdl'

# Create a Suds client using the WSDL URL
client = Client(wsdl_url, cache=None)

# Get a reference to the HelloWorldService
hello_service = client.service

# Call the 'say_hello' method
name = 'John'
times = 3
#result = hello_service.say_hello(name, times)
# Print the result
#for greeting in result:
#    print(greeting)

print(client.service.say_hello("GCARNAB", times))


