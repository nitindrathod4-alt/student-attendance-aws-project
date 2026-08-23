# 🎓 Student Attendance & Result Management System

### AWS Cloud Deployment • MongoDB Atlas • REST API • High Availability

[![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)](https://aws.amazon.com/)
[![MongoDB Atlas](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb)](https://www.mongodb.com/atlas)
[![EC2](https://img.shields.io/badge/AWS-EC2-blue?logo=amazon-aws)](https://aws.amazon.com/ec2/)
[![Route 53](https://img.shields.io/badge/AWS-Route%2053-blue?logo=amazon-aws)](https://aws.amazon.com/route53/)
[![ALB](https://img.shields.io/badge/AWS-Application%20Load%20Balancer-blue?logo=amazon-aws)](https://aws.amazon.com/elasticloadbalancing/)
[![S3](https://img.shields.io/badge/AWS-S3-blue?logo=amazon-aws)](https://aws.amazon.com/s3/)
[![CloudWatch](https://img.shields.io/badge/AWS-CloudWatch-blue?logo=amazon-aws)](https://aws.amazon.com/cloudwatch/)

> A production-style cloud deployment project demonstrating how a student attendance and result management application can be hosted securely and reliably on AWS, with MongoDB Atlas used as the managed database layer.

---

## 📌 Project Overview

The **Student Attendance & Result Management System** provides a centralized platform for managing student records, attendance and academic results.

The infrastructure is designed around AWS cloud services:

```text
Route 53
    ↓
Application Load Balancer
    ↓
EC2 Backend/API
    ↓
MongoDB Atlas
```

Static frontend assets are hosted through **Amazon S3**, while **VPC, IAM, Security Groups and CloudWatch** provide networking, security and monitoring.

### 🎯 Project Goals

- Deploy a real-world application on AWS
- Build a secure and scalable cloud architecture
- Separate frontend, backend and database layers
- Implement managed DNS and load balancing
- Use MongoDB Atlas instead of self-managed database infrastructure
- Demonstrate AWS networking, security and monitoring
- Create a resume-ready DevOps/Cloud project

---

# 🏗️ Architecture

```text
                         🌐 INTERNET
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
                    | Static Frontend  |
                    +------------------+
                             |
                         API Requests
                             |
                             v
                    +------------------+
                    |       ALB        |
                    | Application LB   |
                    +--------+---------+
                             |
                  +----------+----------+
                  |                     |
                  v                     v
          +-------------+       +-------------+
          |   EC2 AZ-1  |       |   EC2 AZ-2  |
          | Backend/API |       | Backend/API |
          +------+------+       +------+------+
                  |                     |
                  +----------+----------+
                             |
                             v
                    +------------------+
                    |  MongoDB Atlas   |
                    |    Database      |
                    +------------------+

       VPC → Network Isolation
       IAM → Access Control
       CloudWatch → Monitoring & Logs
```

## 🔄 Request Flow

```text
User
 ↓
Route 53
 ↓
Application Load Balancer
 ↓
Healthy EC2 Backend
 ↓
REST API
 ↓
MongoDB Atlas
 ↓
Response
 ↓
User
```

---

# ☁️ AWS Services

| Service | Role |
|---|---|
| **Amazon VPC** | Secure cloud networking |
| **Amazon EC2** | Backend/API compute |
| **Application Load Balancer** | Traffic distribution & health checks |
| **Amazon Route 53** | DNS and custom domain |
| **Amazon S3** | Static frontend hosting |
| **AWS IAM** | Identity and access management |
| **Security Groups** | Network-level security |
| **AWS CloudWatch** | Metrics, logs and monitoring |
| **AWS Certificate Manager** | HTTPS/SSL certificates |
| **AWS Systems Manager** | Secure EC2 administration |
| **AWS Secrets Manager / Parameter Store** | Secure application secrets |
| **MongoDB Atlas** | Managed database |

> **Database note:** MongoDB Atlas is the database layer; the infrastructure and application deployment remain AWS-focused.

---

# ✨ Key Features

### 👨‍🎓 Student Management
- Student registration
- Student profile management
- Student search
- Student records

### 📋 Attendance
- Attendance recording
- Attendance history
- Attendance percentage calculation
- Student-wise attendance tracking

### 📝 Results
- Result management
- Academic result history
- Student result lookup

### 🔐 Authentication
- Login
- Role-based access
- Admin functionality

### ☁️ Cloud & DevOps
- AWS cloud deployment
- Multi-AZ EC2 architecture
- Application Load Balancer
- Route 53 custom domain
- S3 frontend hosting
- MongoDB Atlas integration
- CloudWatch monitoring
- HTTPS with ACM
- Secure IAM permissions
- Security Groups
- Deployment documentation

---

# 📁 Project Structure

```text
Student_Attendance_AWS_Project/
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

---

# 🚀 Deployment

A complete click-by-click deployment guide is available here:

**[`aws/deployment-guide.md`](Student_Attendance_AWS_Project/aws/deployment-guide.md)**

The guide covers:

```text
1. AWS Region
2. VPC
3. Availability Zones
4. Public/Private Subnets
5. Internet Gateway
6. IAM Role
7. Security Groups
8. EC2 Instance 1
9. EC2 Instance 2
10. MongoDB Atlas
11. Backend deployment
12. Target Group
13. Application Load Balancer
14. S3 frontend
15. Route 53
16. ACM / HTTPS
17. CloudWatch
18. Testing
19. Troubleshooting
20. Cleanup
```

---

# 🖥️ Recommended Infrastructure

For the production-style demonstration:

```text
VPC                 → 1
Availability Zones  → 2
Public Subnets      → 2
Private Subnets     → 2
EC2 Instances       → 2
Application ALB     → 1
Target Group        → 1
S3 Bucket           → 1
Route 53            → 1 Hosted Zone
ACM Certificate     → 1
MongoDB Atlas       → 1 Cluster
CloudWatch          → Monitoring
```

### Why 2 EC2 instances?

Two backend instances provide:

- High availability
- Load balancing
- Health-check based routing
- Better fault tolerance
- Multi-AZ demonstration

For a low-cost learning environment, the architecture can initially be tested with **one EC2 instance**.

---

# 🍃 MongoDB Atlas

MongoDB Atlas provides the managed database layer.

### Database

```text
Database:
studentdb

Collections:
├── students
├── attendance
├── results
└── users
```

### Environment Variables

```bash
export MONGODB_URI="<MONGODB_ATLAS_CONNECTION_STRING>"
export DB_NAME="studentdb"
```

⚠️ **Never commit database credentials, connection strings or `.env` files to GitHub.**

---

# 🔐 Security

Security practices implemented/recommended:

- IAM least-privilege access
- Restricted EC2 Security Groups
- ALB as public backend entry point
- HTTPS using ACM
- MongoDB Atlas network restrictions
- Secure secret storage
- No credentials in source code
- SSH restricted to My IP when required
- CloudWatch monitoring
- CloudTrail recommended for audit visibility

### Never commit

```text
.env
MONGODB_URI
MONGODB_PASSWORD
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
*.pem
```

---

# 📊 Monitoring

### EC2

```text
CPU Utilization
Network In
Network Out
Status Checks
```

### ALB

```text
Request Count
Target Health
HTTP 4XX
HTTP 5XX
Target Response Time
```

### Application

```text
Backend Logs
API Errors
Database Connectivity
```

---

# 🧪 Testing

### Local backend

```bash
curl http://localhost/
```

### API

```bash
curl http://localhost/api/students
```

### ALB

```bash
curl http://<ALB_DNS_NAME>/
```

### Route 53

```bash
nslookup attendance.yourdomain.com
```

### HTTPS

```bash
curl -I https://attendance.yourdomain.com/
```

### MongoDB

Verify application/database connectivity through the backend without exposing credentials.

---

# 🛠️ Useful AWS CLI Commands

```bash
aws sts get-caller-identity

aws ec2 describe-instances --output table

aws ec2 describe-vpcs --output table

aws ec2 describe-subnets --output table

aws elbv2 describe-load-balancers --output table

aws elbv2 describe-target-groups --output table

aws elbv2 describe-target-health \
  --target-group-arn <TARGET_GROUP_ARN>

aws s3 ls

aws route53 list-hosted-zones --output table
```

---

# 🧹 Cost & Cleanup

AWS resources can generate charges depending on the account, region and configuration.

After testing, remove resources that are no longer required:

```text
1. ALB
2. Target Group
3. EC2 Instances
4. NAT Gateway
5. Unused Elastic IPs
6. S3 objects/bucket
7. Route 53 hosted zone if unused
8. VPC resources
9. MongoDB Atlas cluster if unused
```

Always review the AWS Billing dashboard after cleanup.

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- AWS Cloud
- AWS VPC
- Subnets
- EC2
- Application Load Balancer
- Route 53
- S3
- IAM
- Security Groups
- CloudWatch
- ACM
- AWS CLI
- REST APIs
- MongoDB Atlas
- Database connectivity
- DNS
- HTTPS
- High availability
- Multi-AZ architecture
- Cloud security
- Production-style deployment

---

# 💼 Resume Description

### Student Attendance & Result Management System — AWS + MongoDB Atlas

> Designed and deployed a cloud-based student attendance and result management application using AWS VPC, EC2, Application Load Balancer, Route 53, S3, IAM, Security Groups, CloudWatch and ACM, with MongoDB Atlas as the managed database. Implemented REST APIs, multi-AZ backend deployment, secure DNS/HTTPS configuration, database integration and cloud monitoring.

### Skills Demonstrated

```text
AWS | EC2 | VPC | ALB | Route 53 | S3 |
IAM | Security Groups | CloudWatch | ACM |
AWS CLI | REST API | MongoDB Atlas | Linux |
Cloud Deployment | Networking | Cloud Security
```

---

# 🎯 Interview Highlights

### Why AWS?

AWS provides the infrastructure for:

```text
Compute       → EC2
Networking    → VPC
Load Balancer → ALB
DNS           → Route 53
Storage       → S3
Security      → IAM + Security Groups
Monitoring    → CloudWatch
HTTPS         → ACM
```

### Why MongoDB Atlas?

MongoDB Atlas provides:

- Managed database infrastructure
- Automated database operations
- Secure connectivity
- Scalable deployment options
- Reduced database administration overhead

---

# 👨‍💻 Author

**Nitin Rathod**

AWS • DevOps • Cloud Computing

---

## ⭐ Project Status

**AWS Cloud Architecture:** ✅  
**MongoDB Atlas Integration:** ✅  
**Route 53 Architecture:** ✅  
**ALB Architecture:** ✅  
**Multi-AZ EC2 Design:** ✅  
**Security & Monitoring Design:** ✅  
**Deployment Guide:** ✅

---

> ⭐ Built as a hands-on AWS & DevOps portfolio project.
