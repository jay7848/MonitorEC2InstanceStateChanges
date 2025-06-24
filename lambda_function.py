import boto3


def lambda_handler(event, context):
    sns_topic_arn = 'arn:aws:sns:us-west-2:975050024946:ec2-state-change-topic'  # Replace with your SNS Topic ARN
    target_instance_id = 'i-064081573ba66668b'  # Replace with your actual EC2 Instance ID


    detail = event.get("detail", {})
    instance_id = detail.get("instance-id", "Unknown")
    state = detail.get("state", "Unknown")


    # ✅ Monitor only the specified instance
    if instance_id != target_instance_id:
        print(f"Ignored instance {instance_id}, only monitoring {target_instance_id}")
        return {"status": "ignored"}


    message = f"✅ Monitored EC2 Instance {instance_id} has changed state to: {state}"


    sns = boto3.client("sns")
    sns.publish(
        TopicArn=sns_topic_arn,
        Subject="Monitored EC2 Instance State Change",
        Message=message
    )


    print("Notification sent:", message)
    return {"status": "done"}
