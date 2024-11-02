import boto3

ec2 = boto3.client('ec2', region_name="us-east-1")
#_iam = boto3.client('iam')
# _s3 = boto3.client('s3')
dev_filter = [{'Name': 'tag:env', 'Values': ['dev']}]
response = ec2.describe_instances(Filters=dev_filter)
instance_list = []
for instance in response['Reservations']:
    instance_id = instance['Instances'][0]['InstanceId']
    instance_list.append(instance_id)
    
    print(instance_list)
