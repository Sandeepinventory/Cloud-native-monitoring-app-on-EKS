import boto3
region_name = 'us-west-2'

ecr_client = boto3.client('ecr', region_name=region_name)

repository_name = "my_repository"
response= ecr_client.create_repository(repositoryName=repository_name)

repository_uri=response['repository']['repositoryUri']
print(repository_uri)
