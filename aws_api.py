import boto3

_ec2 = boto3.client('ec2',region_name='us-east-1')
response = _ec2.describe_instances()

instance_list=[]
for item in response['Reservations']:
    #print("********************************************************************************")
    instance_list.append(item['Instances'][0]['InstanceId'])
#print(instance_list)
try:
    _ec2.start_instances(instanceIds=instance_list)
except Exception as e:
    print(f"Error: {e}")