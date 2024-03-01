import json
import os

import requests

from common.constants.environment_variables import ENVIRONMENT_VARIABLES

from requests.auth import HTTPBasicAuth


def handle_history(event, context):
    # Logic for /servicenow/history
    query_params = event.get('queryStringParameters', {})
    url = f"{ENVIRONMENT_VARIABLES['API_URL']}/table/sysapproval_approver"
    query_params = event.get('queryStringParameters', {})
    params = {
        'sysparm_limit': 10,
        'sysparm_display_value': True,
        'sysparm_query': ""
    }

    if query_params:
        sysparm_limit = query_params.get('sysparm_limit')
        sysparm_display_value = query_params.get('sysparm_display_value')
        sysparm_query = query_params.get('sysparm_query')

        if sysparm_limit:
            params['sysparm_limit'] = sysparm_limit
        if sysparm_display_value:
            params['sysparm_display_value'] = sysparm_display_value
        if sysparm_query:
            params['sysparm_query'] = sysparm_query

    try:
        response = requests.get(
            url,
            params=params,
            auth=HTTPBasicAuth(ENVIRONMENT_VARIABLES['USERNAME'], ENVIRONMENT_VARIABLES['PASSWORD'])
        )
        response.raise_for_status()

        data = response.json()
        print(data)

        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
