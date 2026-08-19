# Student Attendance & Result Management System — AWS

Student-focused AWS project using S3, CloudFront, ALB, EC2, RDS, VPC, IAM, Security Groups and CloudWatch.

Architecture:
Student Browser -> CloudFront -> S3 Frontend
                         |
                         v
                    ALB -> EC2 Backend -> RDS MySQL

Features:
- Student registration/login foundation
- Attendance
- Results
- Student dashboard
- Database-backed API

Replace placeholders such as <RDS_ENDPOINT>, <DB_PASSWORD>, <ALB_DNS> and <BUCKET_NAME> before deployment.

This is a student/demo project. For production use HTTPS, Secrets Manager, least-privilege IAM and private backend/database subnets.
