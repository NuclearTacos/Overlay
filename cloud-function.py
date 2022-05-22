import requests
import functions_framework
import os

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    
    # For more information about CORS and CORS preflight requests, see
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request
    # for more information.

    # Set CORS headers for preflight requests
    #  or request.method == 'GET'
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': 'Authorization',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    # Methods line is new in this segment
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Credentials': 'true'
    }
    
    
    outCount = 0
    
    request_json = request.get_json(force=True)

    if request_json and 'exCount' in request_json:
        outCount = request_json['exCount']
    """
    if request.args and 'exCount' in request.args:
        outCount = request.args.get('exCount')
    elif request_json and 'exCount' in request_json:
        outCount = request_json['exCount']
    """   
    url = requests.get("https://storage.googleapis.com/tf-overlays-db/basic-card.json")
    # text = url.text
    # print(type(text))

    return (url.text, 200, headers)
    # return (os.environ.get('testCardData', 'null' ), 200, headers)
    # return (str(outCount), 200, headers)