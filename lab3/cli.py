import sys
import requests

def add_query(request):
    argsLen = len(sys.argv)
    request += "?"
    for i in range(3, argsLen):
        request += sys.argv[i]
        if i != argsLen-1:
            request += "&"
    return request

request = "http://localhost:8003/" + sys.argv[2]

response = ""
method = sys.argv[1].lower()
fileType = sys.argv[2]
if method == "get":
    request = add_query(request)
    response = requests.get(request)
elif method == "post":
    body = ""
    if fileType == "directory":
        body = {'father': sys.argv[3], 'name': sys.argv[4], 'max_elems': sys.argv[5]}
    elif fileType == "binaryfile":
        body = {'father': sys.argv[3], 'name': sys.argv[4], 'info': sys.argv[5]}
    elif fileType == "bufferfile":
        body = {'father': sys.argv[3], 'name': sys.argv[4], 'max_size': sys.argv[5]}
    elif fileType == "logtextfile":
        body = {'father': sys.argv[3], 'name': sys.argv[4]}
    response = requests.post(request, json = body)
elif method == "patch":
    request = add_query(request)
    response = requests.patch(request)
elif method == "delete":
    request = add_query(request)
    response = requests.delete(request)
elif method == "put":
    body = {'path': sys.argv[3], 'info': sys.argv[4]}
    response == requests.put(request, json = body)

print("Status code:", response.status_code)
print("Response:", response.content)