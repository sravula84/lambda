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

    url = ""
    query_params = event.get('queryStringParameters', {})
    # Logic for /servicenow/item/<item_id>
    if query_params:
        item_id = query_params.get('item_id')
        if item_id:
            url = f"{ENVIRONMENT_VARIABLES['API_URL']}/task/{item_id}"
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid request'})
            }


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
