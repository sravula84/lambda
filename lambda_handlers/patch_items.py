import json

import requests
from requests.auth import HTTPBasicAuth

from common.constants.environment_variables import ENVIRONMENT_VARIABLES


def handle_patch_item(event, context):
    # Logic for handling PATCH on /servicenow/item/<item_id>
    if 'path' not in event or 'body' not in event:
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
    patch_data = event['body']

    try:
        response = requests.patch(
            url,
            auth=HTTPBasicAuth(ENVIRONMENT_VARIABLES['USERNAME'], ENVIRONMENT_VARIABLES['PASSWORD']),
            headers={'Content-Type': 'application/json'},
            data=patch_data
        )
        response.raise_for_status()  # Raise an exception for bad responses (4xx, 5xx)

        patched_data = response.json()
        # Process the patched data as needed
        print(patched_data)

        return {
            'statusCode': 200,
            'body': json.dumps(patched_data)
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
