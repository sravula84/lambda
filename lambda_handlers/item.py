import json

import requests
from requests.auth import HTTPBasicAuth

from common.constants.environment_variables import ENVIRONMENT_VARIABLES


def handle_item(event, context):
    if 'path' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid request'})
        }
    item_id = event['path'].split('/')[-1]

    # Logic for /servicenow/item/<item_id>
    url = f"{ENVIRONMENT_VARIABLES['API_URL']}/x_rnod_csod_serv_0_service_ops_request/{item_id}"


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
