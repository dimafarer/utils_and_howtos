# promps

## Architecture Prompts

1. "A real-time chat application for 50,000 users with message history and file sharing"
   • Tests: WebSocket handling, high concurrency, storage needs

2. "An e-commerce platform with inventory management, payment processing, and order tracking"
   • Tests: Complex business logic, multiple integrations, security requirements

3. "A video streaming service like Netflix with user profiles and content recommendations"
   • Tests: Media storage, CDN usage, ML services, high bandwidth

4. "A mobile app backend for ride-sharing with GPS tracking and real-time matching"
   • Tests: Location services, real-time processing, mobile optimization

5. "A data analytics dashboard processing IoT sensor data from 10,000 devices"
   • Tests: IoT integration, big data processing, visualization needs

## Demo Error Messages

1. "AccessDenied: User is not authorized to perform: s3:GetObject on resource: arn:aws:s3:::my-bucket/file.txt"
   • Tests: IAM permissions, S3 bucket policies

2. "InvalidParameterValue: The subnet ID 'subnet-12345' does not exist"
   • Tests: VPC configuration, resource validation

3. "ThrottlingException: Rate exceeded for operation: PutItem"
   • Tests: DynamoDB throttling, capacity planning

4. "ValidationException: 1 validation error detected: Value at 'functionName' failed to satisfy constraint: Member must satisfy regular expression 
pattern: [a-zA-Z0-9-_]+"
   • Tests: Lambda naming conventions, input validation

5. "InsufficientCapacityException: We currently do not have sufficient m5.large capacity in the Availability Zone you requested"
   • Tests: EC2 capacity issues, instance type selection   