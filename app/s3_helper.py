import aiofiles
import boto3
import time
from app.config import *

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)



# this functions for uploade data to s3
async def upload_to_s3(filename: str, data: dict):
    async with aiofiles.open(f"/tmp/{filename}", "w") as f:
        await f.write(str(data))

    s3 = session.client('s3',region_name='ca-central-1')
    print(s3)
    s3.upload_file(f"/tmp/{filename}", S3_BUCKET, filename)
    print(s3.upload_file(f"/tmp/{filename}", S3_BUCKET, filename))

# check data from cache 
async def check_cache(city: str):
    s3 = session.client('s3',region_name='ca-central-1')
    cache_expiry = 5 * 60  # 5 minutes
    objects = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=city)

    if 'Contents' in objects:
        latest_file = max(objects['Contents'], key=lambda obj: obj['LastModified'])
        last_modified = latest_file['LastModified'].timestamp()
        current_time = time.time()

        if current_time - last_modified < cache_expiry:
            file_key = latest_file['Key']
            s3.download_file(S3_BUCKET, file_key, f"/tmp/{file_key}")
            async with aiofiles.open(f"/tmp/{file_key}", "r") as f:
                return await f.read()

    return None
