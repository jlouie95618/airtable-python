

class Airtable(object):
    """docstring for Airtable"""
    DEFAULT_CONFIG = {
        'endpointUrl': 'https://api.airtable.com',
        'apiVersion': '0.1.0',
        'apiKey': None,
        'allowUnauthorizedSsl': False,
        'noRetryIfRateLimited': False,
    }
    def __init__(self, opts = {}):
        self.opts = opts
        if 'apiKey' in opts: 
            self.apiKey = opts['apiKey']
        if 'endpointUrl' in opts:
            self.endpointUrl = opts['endpointUrl']
        if 'apiVersion' in opts: 
            self.apiVersion = opts['apiVersion']
        if 'apiVersionMajor' in opts:
            self.apiVersionMajor = opts['apiVersionMajor']
        if 'allowUnauthorizedSsl' in opts:
            self.allowUnauthorizedSsl = opts['allowUnauthorizedSsl']
        if 'noRetryIfRateLimited' in opts:
            self.noRetryIfRateLimited = opts['noRetryIfRateLimited']

    def configure(self, opts):
        self.apiKey = opts['apiKey']
        self.endpointUrl = opts['endpointUrl']
        self.apiVersion = opts['apiVersion']
        self.apiVersionMajor = opts['apiVersionMajor']
        self.allowUnauthorizedSsl = opts['allowUnauthorizedSsl']
        self.noRetryIfRateLimited = opts['noRetryIfRateLimited']

    def base(self, baseId):
        assert self.apiKey != None
        


airtable = Airtable({'apiKey': 'keyrpG4FPpEqZ0ubg'});
        