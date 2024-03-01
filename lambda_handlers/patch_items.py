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
    item_id = event['path'].split('/')[-1]
    patch_data = event['body']
    url = f"{ENVIRONMENT_VARIABLES['API_URL']}/sysapproval_approver/{item_id}"

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
