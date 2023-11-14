import json
import boto3
import os

# Denne koden kan også kjøres som en selvstendig applikasjon (Uten SAM) bare gjøre følgende
# (dersom man har python på maskinen sin altså...)
#
# Instruksjoner for å kjøre ... (Kan sikkert lage container senere ..)
#
# pip3 install -r requirements.txt
# python3 app.py
#
# Hilsen Kjell

s3_client = boto3.client('s3', region_name='eu-west-1')
rekognition_client = boto3.client('rekognition', region_name='eu-west-1')

# Oppgave 1A
BUCKET_NAME = "kjellsimagebucker"

def lambda_handler(event, context):

    # List all objects in the S3 bucket
    paginator = s3_client.get_paginator('list_objects_v2')
    rekognition_results = []  # Store the results

    for page in paginator.paginate(Bucket=BUCKET_NAME):
        for obj in page.get('Contents', []):
            # Perform PPE detection using Rekognition
            rekognition_response = rekognition_client.detect_protective_equipment(
                Image={
                    'S3Object': {
                        'Bucket': BUCKET_NAME,
                        'Name': obj['Key']
                    }
                },
                SummarizationAttributes={
                    'MinConfidence': 80,  # Confidence level threshold
                    'RequiredEquipmentTypes': ['FACE_COVER']
                }
            )
            rekognition_results.append(rekognition_response)

    return {
        "statusCode": 200,
        "body":  json.dumps(rekognition_results),
    }

print(lambda_handler(None, None))