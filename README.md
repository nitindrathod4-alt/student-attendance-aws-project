# 🎓 Student Attendance & Result Management System — AWS

> A student-focused cloud application demonstrating a 3-tier AWS architecture.

## 📌 Project Overview

The **Student Attendance & Result Management System** is a simple web application for managing student attendance and academic results.

It demonstrates how a student application can be deployed using core AWS services:

**S3 → CloudFront → Application Load Balancer → EC2 → RDS MySQL**

## 🏗️ AWS Architecture

```text
                         👨‍🎓 STUDENT
                              |
                              v
                    +------------------+
                    |   CloudFront     |
                    |      CDN         |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |       S3         |
                    |    Frontend      |
                    +--------+---------+
                             |
                         API Request
                             |
                             v
                    +------------------+
                    |       ALB        |
                    | Application LB   |
                    +--------+---------+
                             |
                 +-----------+-----------+
                 |                       |
                 v                       v
          +-------------+         +-------------+
          |   EC2 AZ-1  |         |   EC2 AZ-2  |
          | Backend/API |         | Backend/API |
          +------+------+         +------+------+
                 |                       |
                 +-----------+-----------+
                             |
                             v
                    +------------------+
                    |    RDS MySQL     |
                    |    Database      |
                    +------------------+
```

## ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Static frontend hosting |
| Amazon CloudFront | CDN and frontend delivery |
| Application Load Balancer | Backend traffic distribution |
| Amazon EC2 | Backend/API server |
| Amazon RDS MySQL | Student database |
| Amazon VPC | Network isolation |
| IAM | Access management |
| Security Groups | Network security |
| CloudWatch | Monitoring |

## ✨ Features

- Student information
- Attendance tracking
- Result management
- Student roll number
- Attendance percentage
- Pass/Result status
- REST API
- MySQL database
- AWS cloud deployment

## 📁 Project Structure

```text
student-attendance-aws-project/
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── database/
│   └── schema.sql
│
├── aws/
│   └── deployment-guide.md
│
├── docs/
│   └── architecture.md
│
└── README.md
```

# 🚀 Deployment Overview

## 1. VPC

Recommended network:

```text
VPC: 10.0.0.0/16
Availability Zones: 2
Public Subnets: 2
Private Subnets: 2
```

## 2. Security Groups

### ALB

```text
HTTP 80 → 0.0.0.0/0
```

### EC2

```text
HTTP 80 → ALB Security Group
SSH 22  → My IP
```

### RDS

```text
MySQL 3306 → EC2 Security Group
```

> RDS port 3306 should not be publicly exposed.

## 3. RDS MySQL

Example configuration:

```text
DB Identifier: student-db
Username: admin
Database: studentdb
Public Access: No
```

Database schema:

```sql
CREATE DATABASE IF NOT EXISTS studentdb;

USE studentdb;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(30) NOT NULL UNIQUE,
    attendance DECIMAL(5,2),
    result VARCHAR(30)
);
```

Sample data:

```sql
INSERT INTO students
(name, roll_no, attendance, result)
VALUES
('Rahul Patil', 'STU001', 88.50, 'Pass'),
('Amit Shinde', 'STU002', 76.00, 'Pass'),
('Sneha More', 'STU003', 92.00, 'Pass'),
('Pooja Jadhav', 'STU004', 64.50, 'Pass');
```

## 4. EC2 Backend

Install packages:

```bash
sudo dnf update -y
sudo dnf install -y python3-pip mysql
python3 --version
pip3 --version
```

Install backend dependencies:

```bash
cd backend
pip3 install -r requirements.txt
```

Set database variables:

```bash
export DB_HOST="<RDS_ENDPOINT>"
export DB_USER="admin"
export DB_PASSWORD="<DB_PASSWORD>"
export DB_NAME="studentdb"
```

Run:

```bash
sudo python3 app.py
```

Test:

```bash
curl http://localhost/
curl http://localhost/api/students
```

## 5. Application Load Balancer

Create an internet-facing ALB with:

```text
Listener: HTTP : 80
Target Group: student-backend
Protocol: HTTP
Port: 80
Health Check: /
```

Test:

```bash
curl http://<ALB_DNS>/
curl http://<ALB_DNS>/api/students
```

## 6. S3 Frontend

Upload:

```bash
aws s3 cp frontend/index.html s3://<BUCKET_NAME>/
aws s3 cp frontend/css/style.css s3://<BUCKET_NAME>/css/style.css
aws s3 cp frontend/js/app.js s3://<BUCKET_NAME>/js/app.js
```

For a production-style setup, keep the bucket private and use CloudFront Origin Access Control.

## 7. CloudFront

Recommended:

```text
Origin: S3
Origin Access: OAC
Default Root Object: index.html
Viewer Protocol: Redirect HTTP → HTTPS
```

Update `frontend/js/app.js`:

```javascript
const API_URL = "http://<ALB_DNS>/api/students";
```

For production, use HTTPS for the API as well.

# 🔄 Application Data Flow

```text
Student Browser
      |
      v
CloudFront
      |
      v
S3 Frontend
      |
      | API Request
      v
Application Load Balancer
      |
      v
EC2 Backend
      |
      v
RDS MySQL
      |
      v
JSON Response
      |
      v
Student Browser
```

# 🧪 Testing

Backend:

```bash
curl http://<ALB_DNS>/
```

Student API:

```bash
curl http://<ALB_DNS>/api/students
```

Expected response:

```json
[
  {
    "name": "Rahul Patil",
    "roll_no": "STU001",
    "attendance": 88.5,
    "result": "Pass"
  }
]
```

# 📊 CloudWatch Monitoring

Monitor:

```text
EC2
 ├── CPU Utilization
 ├── Network
 └── Status Checks

ALB
 ├── Request Count
 ├── Target Health
 └── HTTP Errors

RDS
 ├── CPU Utilization
 ├── Database Connections
 └── Storage
```

# 🛠️ Useful AWS CLI Commands

```bash
aws sts get-caller-identity

aws ec2 describe-instances --output table

aws rds describe-db-instances --output table

aws elbv2 describe-load-balancers --output table

aws s3 ls

aws cloudfront list-distributions --output table
```

# 🔒 Security

Do not commit sensitive information:

```text
.env
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
DB_PASSWORD
*.pem
```

Use IAM least privilege, private RDS access, restricted security groups and HTTPS for production.

# 🧹 AWS Cleanup

After testing, delete unused resources to avoid charges:

```text
1. CloudFront
2. S3 Bucket
3. Load Balancer
4. Target Group
5. EC2 Instances
6. RDS Database
7. NAT Gateway (if created)
8. VPC resources
```

Always check AWS Billing after cleanup.

# 🎯 Learning Outcomes

- AWS VPC networking
- Public/private subnets
- EC2
- Application Load Balancer
- RDS MySQL
- S3
- CloudFront
- IAM
- Security Groups
- AWS CLI
- CloudWatch
- REST API
- Database connectivity
- 3-tier cloud architecture

# 💼 Resume Description

**Student Attendance & Result Management System — AWS**

> Designed and deployed a 3-tier student management application on AWS using Amazon S3, CloudFront, Application Load Balancer, EC2, RDS MySQL, VPC, IAM and Security Groups. Implemented a backend REST API for retrieving student attendance and result data from RDS and configured cloud networking and monitoring.

## 👨‍💻 Developer

**Nitin Rathod**

AWS & DevOps Learner

---

⭐ **Built with AWS Cloud**
