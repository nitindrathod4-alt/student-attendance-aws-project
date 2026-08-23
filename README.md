# 🎓 Student Attendance & Result Management System — AWS + MongoDB Atlas

> A student-focused cloud application demonstrating a 3-tier AWS architecture with Route 53, Application Load Balancer, EC2, S3 and MongoDB Atlas.

## 📌 Project Overview

The **Student Attendance & Result Management System** is a web application for managing student information, attendance and academic results.

It demonstrates how a student application can be deployed using core AWS services with **MongoDB Atlas** as the managed database:

**S3 → Route 53 → Application Load Balancer → EC2 → MongoDB Atlas**

## 🏗️ AWS Architecture

```text
                         👨‍🎓 STUDENT
                              |
                              v
                    +------------------+
                    |    Route 53      |
                    |  Custom Domain   |
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
                    |  MongoDB Atlas   |
                    |    Database      |
                    +------------------+
```

## ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Static frontend hosting |
| Amazon Route 53 | Custom domain and DNS routing |
| Application Load Balancer | Backend traffic distribution |
| Amazon EC2 | Backend/API server |
| Amazon VPC | Network isolation |
| IAM | Access management |
| Security Groups | Network security |
| CloudWatch | Monitoring |
| MongoDB Atlas | Managed application database |

## ✨ Features

- 👨‍🎓 Student registration and management
- 📋 Attendance tracking
- 📊 Attendance percentage calculation
- 📝 Result management
- 🔎 Student search
- 🔐 Login and authentication
- 👤 Admin dashboard
- 📜 Attendance and result history
- 📱 Responsive web interface
- 🌐 Custom domain with Route 53
- ⚖️ Application Load Balancer
- 🖥️ AWS EC2 backend
- 🍃 MongoDB Atlas database
- 📊 CloudWatch monitoring
- 🔒 IAM and Security Groups
- 🔗 REST API integration

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
HTTP 80  → 0.0.0.0/0
HTTPS 443 → 0.0.0.0/0
```

### EC2

```text
HTTP 80 → ALB Security Group
SSH 22  → My IP
```

### MongoDB Atlas

Restrict database network access to the required application/EC2 egress IPs or trusted network configuration. Do not expose the database publicly without appropriate controls.

## 3. MongoDB Atlas

Example configuration:

```text
Cluster: student-attendance
Database: studentdb
Collections:
  ├── students
  ├── attendance
  ├── results
  └── users
```

Set the database connection securely:

```bash
export MONGODB_URI="<MONGODB_ATLAS_CONNECTION_STRING>"
export DB_NAME="studentdb"
```

Never commit the MongoDB connection string, username or password to GitHub.

## 4. EC2 Backend

Install packages:

```bash
sudo dnf update -y
sudo dnf install -y python3-pip
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
export MONGODB_URI="<MONGODB_ATLAS_CONNECTION_STRING>"
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

## 6. Route 53

Create a hosted zone for your domain and point an Alias A record to the Application Load Balancer.

Example:

```text
Domain: attendance.example.com
Record: A / Alias
Target: Application Load Balancer
```

For production, configure HTTPS using an ACM certificate and an HTTPS listener on the ALB.

## 7. S3 Frontend

Upload static frontend files:

```bash
aws s3 cp frontend/index.html s3://<BUCKET_NAME>/
aws s3 cp frontend/css/style.css s3://<BUCKET_NAME>/css/style.css
aws s3 cp frontend/js/app.js s3://<BUCKET_NAME>/js/app.js
```

Update the frontend API endpoint to the Route 53 application domain:

```javascript
const API_URL = "https://attendance.example.com/api/students";
```

# 🔄 Application Data Flow

```text
Student Browser
      |
      v
Route 53
      |
      v
Application Load Balancer
      |
      v
EC2 Backend / REST API
      |
      v
MongoDB Atlas
      |
      v
JSON Response
      |
      v
Student Browser
```

Static frontend assets are hosted using Amazon S3.

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
```

# 🛠️ Useful AWS CLI Commands

```bash
aws sts get-caller-identity
aws ec2 describe-instances --output table
aws elbv2 describe-load-balancers --output table
aws s3 ls
aws route53 list-hosted-zones --output table
```

# 🔒 Security

Do not commit sensitive information:

```text
.env
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
MONGODB_URI
MONGODB_PASSWORD
*.pem
```

Use IAM least privilege, restricted security groups, protected MongoDB Atlas access and HTTPS for production.

# 🧹 AWS Cleanup

After testing, delete unused resources to avoid charges:

```text
1. S3 resources
2. Load Balancer
3. Target Group
4. EC2 Instances
5. Route 53 records / hosted zone if no longer required
6. NAT Gateway (if created)
7. VPC resources
```

Also review MongoDB Atlas resources and AWS Billing after cleanup.

# 🎯 Learning Outcomes

- AWS VPC networking
- Public/private subnets
- EC2
- Application Load Balancer
- Route 53 DNS
- S3
- IAM
- Security Groups
- CloudWatch
- AWS CLI
- MongoDB Atlas
- REST API
- Database connectivity
- Cloud deployment
- 3-tier cloud architecture

# 💼 Resume Description

**Student Attendance & Result Management System — AWS & MongoDB Atlas**

> Designed and deployed a cloud-based student attendance and result management application using AWS services including VPC, EC2, Application Load Balancer, Route 53, S3, IAM and CloudWatch, with MongoDB Atlas as the managed database. Implemented REST APIs for student attendance and result management and configured secure cloud networking and monitoring.

## 👨‍💻 Developer

**Nitin Rathod**

AWS & DevOps Learner

---

⭐ **Built with AWS Cloud + MongoDB Atlas**
