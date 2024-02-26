import os
import json
import requests
from requests.auth import HTTPBasicAuth

def lambda_handler(event, context):
    path = event['path']
    http_method = event['httpMethod']

    if path == '/servicenow/history':
        return handle_history()
    elif path.startswith('/servicenow/item/') and http_method == 'GET':
        # Extract item_id from the path
        item_id = path.split('/')[-1]
        return handle_item(item_id)
    elif path == '/servicenow/items' and http_method == 'GET':
        return handle_items()
    elif path.startswith('/servicenow/item/') and http_method == 'PATCH':
        # Extract item_id from the path
        item_id = path.split('/')[-1]
        return handle_patch_item(item_id, event['body'])
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Not Found'}),
        }

def handle_history():
    # Logic for /servicenow/history
    url = "https://cornerstoneondemanddev.service-now.com/api/now/table/sysapproval_approver?sysparm_limit=10"

    username = os.environ.get("API_USERNAME")
    password = os.environ.get("API_PASSWORD")

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(username, password)
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

def handle_item(item_id):
    # Logic for /servicenow/item/<item_id>
    url = f"https://cornerstoneondemanddev.service-now.com/api/now/table/x_rnod_csod_serv_0_service_ops_request/{item_id}"

    username = os.environ.get("API_USERNAME")
    password = os.environ.get("API_PASSWORD")

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(username, password)
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

def handle_items():
    # Logic for /servicenow/items
    url = "https://cornerstoneondemanddev.service-now.com/api/now/table/sysapproval_approver?sysparm_limit=10&sysparm_display_value=true"

    username = os.environ.get("API_USERNAME")
    password = os.environ.get("API_PASSWORD")

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(username, password)
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

def handle_patch_item(item_id, patch_data):
    # Logic for handling PATCH on /servicenow/item/<item_id>
    url = f"https://cornerstoneondemanddev.service-now.com/api/now/table/sysapproval_approver/{item_id}"

    username = os.environ.get("API_USERNAME")
    password = os.environ.get("API_PASSWORD")

    try:
        response = requests.patch(
            url,
            auth=HTTPBasicAuth(username, password),
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

