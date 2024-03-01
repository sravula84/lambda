import json
import os

import requests

from common.constants.environment_variables import ENVIRONMENT_VARIABLES

from requests.auth import HTTPBasicAuth


def handle_history(event, context):
    # Logic for /servicenow/history
    url = f"{ENVIRONMENT_VARIABLES['API_URL']}/sysapproval_approver?sysparm_limit=10"


    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(ENVIRONMENT_VARIABLES['USERNAME'], ENVIRONMENT_VARIABLES['PASSWORD'])
        )
        response.raise_for_status()  # Raise an exception for bad responses (4xx, 5xx)

        data = response.json()
        # Process the data as needed
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
