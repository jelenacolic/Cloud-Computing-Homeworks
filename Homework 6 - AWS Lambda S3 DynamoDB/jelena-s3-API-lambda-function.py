import json
import base64
import boto3

BUCKET_NAME = 'master-jelena-1031-2019'

def lambda_handler(event, context):
    
    method = event['requestContext']['http']['method']
    s3 = boto3.client('s3')
    
    if method == "POST":
    
        file_content = base64.b64decode(json.loads(event['body'])['content'])
        file_path = json.loads(event['body'])['fileName']
        
        try:
            s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
            
            
        except Exception as e:
            raise IOError(e)
        
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'fileName':file_path
            }),
            'content-type': 'application/json'
        }
        
        return response
    elif method == "GET":
        file_path = json.loads(event['body'])['fileName']
        
        try:
            file = s3.get_object(Bucket=BUCKET_NAME, Key=file_path)
            
            data = file['Body'].read()
            
            contentDispositionHeader = 'attachment; filename={}'.format(file_path)
        except Exception as e:
            raise IOError(e)
        return {
            'content-disposition': contentDispositionHeader,
            'statusCode': 200,
            'body': data
        }
    elif method == "DELETE":
        
        file_path = json.loads(event['body'])['fileName']
        
        try:
            s3.delete_object(Bucket=BUCKET_NAME, Key=file_path)
            
            
        except Exception as e:
            raise IOError(e)
        return {
            'statusCode': 200,
            'body': json.dumps({'deleted':True}),
            'content-type': 'application/json'
        }
    elif method == "PUT":
        old_file_path = json.loads(event['body'])['originalFileName']
        new_file_path = json.loads(event['body'])['newFileName']
        
        copy_source = {'Bucket': BUCKET_NAME, 'Key': old_file_path}
        
        try:
            
            s3.copy_object(Bucket=BUCKET_NAME, CopySource=copy_source, Key=new_file_path)
            s3.delete_object(Bucket=BUCKET_NAME, Key=old_file_path)
            
            
        except Exception as e:
            raise IOError(e)
        return {
            'statusCode': 200,
            'body': json.dumps({'newFileName':new_file_path}),
            'content-type': 'application/json'
        }