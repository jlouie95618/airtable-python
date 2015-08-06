"""
The Record class is the container/wrapper for information
    that pertains to a particular record in the Airtable
    web application. This class will hold the following
    pieces of information: 
        - a table object, which permits mutability of the record
        - the record id
        - the raw JSON object (which should be parsed by requests)
        - and methods to allow for the alteration of a record
        (namely patch and put updates)
    Important Methods:
        - init: assign the above info
        - getId: returns the record ID
        - get: returns a particular field value (passed the fieldName)
        - set: sets a particular field value to be the passed in value
        - save: ??? I guess it just issues a put request to update
            the object stored on the server
        - 
"""


class Record(object):
    """docstring for Record"""
    def __init__(self, arg):
        self.arg = arg
        