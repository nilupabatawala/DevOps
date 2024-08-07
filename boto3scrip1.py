import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List buckets
response = s3.list_buckets()

# Print the owner ID
owner_id = response['Owner']['ID']
print(owner_id)