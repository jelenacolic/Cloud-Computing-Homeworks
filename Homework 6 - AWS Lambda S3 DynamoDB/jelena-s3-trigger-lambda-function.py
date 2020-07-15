import json
import boto3


BUCKET_NAME = 'master-jelena-1031-2019'


def lambda_handler(event, context):
    
    event_type = event['Records'][0]['eventName']
    file_path = event['Records'][0]['s3']['object']['key']
    dynamo = boto3.client('dynamodb')
    s3 = boto3.client('s3')
    
    if "Created" in event_type:
        
        try:
            file = s3.get_object(Bucket=BUCKET_NAME, Key=file_path)
                
            file_content = file['Body'].read()
            
            num_rows = str(len(file_content.splitlines()))
            num_words = str(len(file_content.split()))
            num_chars = str(len(file_content))
            
            dynamo.put_item(
                TableName = 'master-jelena-1031-2019-files',
                Item = {
                    'fileName': {'S': file_path},
                    'numRows': {'N': num_rows},
                    'numWords': {'N': num_words},
                    'numChars': {'N': num_chars}
                }
            )
        except Exception as e:
            raise IOError(e)
    elif "Removed" in event_type:
        try:
            dynamo.delete_item(
                TableName = 'master-jelena-1031-2019-files',
                Key= {
                    'fileName': {'S': file_path}
                }
            )
        except Exception as e:
            raise IOError(e)