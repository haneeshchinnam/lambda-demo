import json

def lambda_handler(event, context):
    # TODO implement
    print("implement")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Updated from Github!')
    }
