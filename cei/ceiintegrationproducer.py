import boto3
import uuid

from cei.amazon_secrets import AmazonSecrets


class CeiIntegrationProducer:
    # Create SQS client
    secrets = AmazonSecrets()
    # Get the service resource
    sqs = boto3.resource(
        'sqs',
        aws_access_key_id=secrets.accessKey,
        aws_secret_access_key=secrets.secretKey,
        region_name='sa-east-1'
    )

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='update-portfolio.fifo')

    def sendMessage(message):

        # Send message to SQS queue
        response = CeiIntegrationProducer.queue.send_message(
            MessageGroupId='transactions',
            MessageBody=message,
            MessageDeduplicationId=uuid.uuid4().__str__()
        )

        print(response['MessageId'])
