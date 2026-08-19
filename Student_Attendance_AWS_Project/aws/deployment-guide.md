# AWS Deployment Guide

## VPC
Create VPC student-vpc, CIDR 10.0.0.0/16, 2 AZs, 2 public subnets and 2 private subnets.

## Security Groups
ALB: HTTP 80 from Internet.
EC2: HTTP 80 from ALB SG; SSH 22 from My IP.
RDS: MySQL 3306 only from EC2 SG.

## RDS
Create MySQL DB:
- Identifier: student-db
- Username: admin
- Database: studentdb
- Public access: No
- RDS security group

Run database/schema.sql from a host that can reach RDS.

## EC2 Backend
Amazon Linux example:

```bash
sudo dnf update -y
sudo dnf install -y python3-pip mysql
mkdir -p ~/student-backend
cd ~/student-backend
pip3 install -r requirements.txt

export DB_HOST="<RDS_ENDPOINT>"
export DB_USER="admin"
export DB_PASSWORD="<DB_PASSWORD>"
export DB_NAME="studentdb"

sudo python3 app.py
```

Test:
```bash
curl http://localhost/
curl http://localhost/api/students
```

## ALB
Create internet-facing Application Load Balancer in public subnets.
Create target group for HTTP port 80.
Health check path: /.
Register backend EC2 instances.

Test:
```bash
curl http://<ALB_DNS>/
curl http://<ALB_DNS>/api/students
```

## S3
Create a unique bucket and upload:
```bash
aws s3 cp frontend/index.html s3://<BUCKET_NAME>/
aws s3 cp frontend/css/style.css s3://<BUCKET_NAME>/css/style.css
aws s3 cp frontend/js/app.js s3://<BUCKET_NAME>/js/app.js
```

Use CloudFront with S3 Origin Access Control for a production-style private bucket.

## CloudWatch
Monitor EC2 CPU, ALB request count/target health and RDS CPU/connections.

## AWS CLI
```bash
aws sts get-caller-identity
aws ec2 describe-instances --output table
aws rds describe-db-instances --output table
aws elbv2 describe-load-balancers --output table
aws s3 ls
aws cloudfront list-distributions --output table
```

## Cleanup
Delete CloudFront, empty/delete S3, ALB, target group, EC2, RDS, NAT Gateway if used, then VPC dependencies. Check AWS Billing.
