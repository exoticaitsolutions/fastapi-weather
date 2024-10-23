import boto3


S3_BUCKET = ""

AWS_ACCESS_KEY =""
AWS_SECRET_KEY =""
AWS_REGION = ""


session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)


dynamodb = session.resource('dynamodb',region_name=AWS_REGION)
table = dynamodb.Table('WeatherLogs')

async def log_to_dynamodb(city: str, timestamp: int, s3_url: str):
    table.put_item(Item={
        'city': city,
        'timestamp': timestamp,
        's3_url': s3_url
    })
