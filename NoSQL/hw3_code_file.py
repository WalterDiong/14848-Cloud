import boto3
import csv

# Setting up connection to aws
s3 = boto3.resource('s3', aws_access_key_id = '', aws_secret_access_key = '')
# s3.create_bucket(Bucket='walterdjs-bucket-1', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

# Setting up ACL configuration for bucket
bucket = s3.Bucket("walterdjs-bucket-1")
bucket.Acl().put(ACL='public-read')

# Upload data as a blob to s3 bucket
# s3.Object('walterdjs-bucket-1', 'test.png').put(Body=open('test.png', 'rb'))

# Create DynamoDB table to store metadata and references to s3 Objects
dynamo_db = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id = '', aws_secret_access_key = '')

# If creating for the first time
# table = dynamo_db.create_table(
#     TableName = 'Data_table',
#     KeySchema = [
#         {'AttributeName' : 'PartitionKey',
#          'KeyType' : 'HASH'},
#         {'AttributeName' : 'RowKey',
#          'KeyType' : 'RANGE'}
#     ],
#     AttributeDefinitions = [
#         {'AttributeName' : 'PartitionKey',
#          'AttributeType' : 'S'},
#         {'AttributeName' : 'RowKey',
#          'AttributeType' : 'S'}
#     ],
#     ProvisionedThroughput = {
#         'ReadCapacityUnits' : 5,
#         'WriteCapacityUnits': 5
#     }
# )

# Wait for table to get created
# table.meta.client.get_waiter('table_exists').wait(TableName='Data_table')

# If the table has already been created
table = dynamo_db.Table("Data_table")
# urlbase = "https://s3-us-west-2.amazonaws.com/walterdjs-bucket-1/"
# with open('experiments.csv', 'r') as csv_file:
#     csvf = csv.reader(csv_file, delimiter=',', quotechar = '|')
#     next(csvf)
#     for item in csvf:
#         unique_data = open(item[4], 'rb')
#         s3.Object("walterdjs-bucket-1", item[4]).put(Body=unique_data)
#         md = s3.Object("walterdjs-bucket-1", item[4]).Acl().put(ACL='public-read')

#         url = urlbase + item[4]
#         metadata = {'PartitionKey': item[4], 'RowKey': item[0], 'Temperature' : item[1],
#                   'Conductivity' : item[2],  "Concentration" : item[3], "url":url}

#         try:
#             table.put_item(Item=metadata)
#         except:
#             print("Error")

response = table.get_item(
    Key = {'PartitionKey': "exp1.csv",
            'RowKey': "1"
    }
)

print(response['Item'])
print(response)
