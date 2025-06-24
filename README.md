# MonitorEC2InstanceStateChanges
Assignment 3: Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS
Objective: Automatically monitor changes in EC2 instance states and send notifications whenever an instance is started or stopped.

Task: Set up a Lambda function that listens to EC2 state change events and sends SNS notifications detailing the state changes.

Instructions:

1. SNS Setup:

   - Navigate to the SNS dashboard and create a new topic.

   - Subscribe to this topic with your email.

2. Lambda IAM Role:

   - Create a role with permissions to read EC2 instance states and send SNS notifications.

3. Lambda Function:

   - Create a function and assign the above IAM role.

   - Use Boto3 to:

     1. Extract details from the event regarding the EC2 state change.

     2. Send an SNS notification with details about which EC2 instance changed state and the new state (e.g., started, stopped).

4. EC2 Event Bridge (formerly CloudWatch Events):

   - Set up an Event Bridge rule to trigger your Lambda function whenever an EC2 instance state changes.

5. Testing:

   - Start or stop one of your EC2 instances.

   - Confirm you receive an SNS notification about the state change.
