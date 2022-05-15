import requests

class hsd:

    API_KEY = ""
    ADDRESS = ""
    PORT = ""

    def __init__(self, api_key, address, port):
        global API_KEY
        global ADDRESS
        global PORT

        API_KEY = api_key
        ADDRESS = address
        PORT = port

### BEGIN: GET methods
    def get(endpoint):
        url = 'http://x:' + API_KEY + '@' + ADDRESS + ':' + PORT + '/' + endpoint
        getResponse = requests.get(url)
        response = getResponse.json() if getResponse and getResponse.status_code == 200 else None
        return response # Returned as json
    ### END METHOD ################################### get(endpoint)

    def getInfo(self):
        endpoint = "/"
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getInfo(self)

    def getMemPool(self):
        endpoint = "/mempool"
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPool(self)

    def getMemPoolInvalid(self):
        endpoint = "/mempool/invalid"
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPoolInvalid(self)

    def getMemPoolInvalidHash(self, hash):
        endpoint = "/mempool/invalid/" + hash
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getMemPoolInvalidHash(self, hash)

    def getBlockHashOrHeight(self, blockHashOrHeight):
        endpoint = "/block/" + blockHashOrHeight
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getBlockHashOrHeight(self, blockHashOrHeight)

    def getHeaderHashOrHeight(self, headerHashOrHeight):
        endpoint = "/header/" + headerHashOrHeight
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getHeaderHashOrHeight(self headerHashOrHeight)

    def getCoinAddress(self, address):
        endpoint = "/coin/address/" + address
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getCoinAddress(self, address)

    def getCoinHashOrIndex(self, hasOrIndex):
        endpoint = "/coin/" + hash + "/" + hasOrIndex
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getCoinByHashOrIndex(self, hasOrIndex)

    def getFeeEstimate(self, blocks):
        endpoint = "/fee?blocks=" + blocks
        response = self.get(endpoint)
        return response
    ### END METHOD ################################### getFeeEstimate(self, blocks)



### BEGIN: POST methods
    def post(endpoint, post_message):

        url = 'http://x:' + API_KEY + '@' + ADDRESS + ':' + PORT + '/' + endpoint

        postRequest = requests.post(url, post_message)

        response = postRequest.json() if postRequest and postRequest.status_code == 200 else None

        return response # Returned as json
    ### END METHOD ################################### post(endpoint, post_message)

    def postBroadcast(self, tx):
        endpoint = "/broadcast/"
        post_message = "{'tx': '" + tx + "'}"
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### postBroadcast(self, tx)

    def postBroadcastClaim(self, claim):
        endpoint = "/claim/"
        post_message = "{'claim': '" + claim + "'}"
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### postBroadcastClaim(self, claim)

    def postReset(self, height):
        endpoint = "/reset"
        post_message = "{ 'height': " + height + "}"
        response = self.post(endpoint, post_message)
        return response
    ### END METHOD ################################### postReset(self, height)


""" 
for element in json_data:
    if element == "chain":
        entry = json_data[element]
        for value in entry:
            if value == "height":
                print(entry[value]) """