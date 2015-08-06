import requests

def performRequest():
    header = { 'Authorization': 'Bearer keyrpG4FPpEqZ0ubg'}
    r = requests.get('https://api.airtable.com/v0/app9uvKeuVL1pOfCD/Cuisines/recgruzSZ0BvRB63q', headers = header)
    print r
    print r.text

performRequest()