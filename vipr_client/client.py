#!/usr/bin/env python

import argparse
import collections
import datetime
import requests
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--family', default="influenza", help="Virus family, (default: 'influenza')")
    parser.add_argument('--from-year', help="Starting from year, (default: 2 years ago)")
    parser.add_argument('--host', default="human", help="Host organism, (default: 'human')")
    parser.add_argument('--continent', default="North America", help="Continent, (default: 'North America')")

    args = parser.parse_args()
    
    api_root = "https://www.fludb.org/brc/api"
    query_params = collections.OrderedDict()
    query_params['datatype'] = "genome"
    query_params['completegenome'] = "y"
    query_params['family'] = args.family
    query_params['host'] = args.host
    query_params['continent'] = args.continent

    if not args.from_year:
        current_year = datetime.datetime.now().year
        query_params['fromyear'] = str(current_year - 2)
    else:
        query_params['fromyear'] = args.from_year

    query_params['output'] = 'json'

    #request_url = api_root + '/sequence' + '&'.join([param + '=' + query_params[param] for param in query_params])
    request_url = api_root + '/sequence'
    print(request_url)
    response = requests.get(request_url, params=query_params)
    if response.status_code == 200:
        response_data = response.json()
        print(json.dumps(response_data, indent=2))

if __name__ == '__main__':
    main()
