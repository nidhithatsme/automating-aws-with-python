# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

new_bucket = s3.create_bucket(Bucket='s3-boto3', CreateBucketConfiguration = {'LaunchConstraint' : 'ap-southeast-2'})
for bucket in s3.buckets.all():
    print(bucket)

ec2 = session.resource('ec2')
for instance in ec2.instances.all():
    print(instance)

for instance in ec2.instances.all():
    print(instance.state)
    
