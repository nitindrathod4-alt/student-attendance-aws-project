# 🎓 Student Attendance & Result Management System

### AWS Cloud Deployment • MongoDB Atlas • REST API • High Availability

<p align="center">
  <img src="https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws" />
  <img src="https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb" />
  <img src="https://img.shields.io/badge/AWS-EC2-blue?logo=amazon-aws" />
  <img src="https://img.shields.io/badge/AWS-Route%2053-blue?logo=amazon-aws" />
  <img src="https://img.shields.io/badge/AWS-ALB-blue?logo=amazon-aws" />
  <img src="https://img.shields.io/badge/AWS-S3-blue?logo=amazon-aws" />
  <img src="https://img.shields.io/badge/AWS-CloudWatch-blue?logo=amazon-aws" />
</p>

> 🚀 A production-style cloud deployment project demonstrating a student attendance and result management application hosted on AWS, with MongoDB Atlas as the managed database layer.

## 📊 Project Dashboard

| Component | Status |
|---|---|
| ☁️ AWS Infrastructure | 🟢 Active |
| 🌐 Route 53 | 🟢 Configured |
| ⚖️ Application Load Balancer | 🟢 Configured |
| 🖥️ EC2 Backend | 🟢 Deployed |
| 🍃 MongoDB Atlas | 🟢 Connected |
| 📦 S3 Frontend | 🟢 Deployed |
| 🔐 Security | 🟢 Configured |
| 📊 CloudWatch | 🟢 Monitoring |
| 📚 Deployment Guide | 🟢 Available |

## 🧭 Quick Navigation

- [📌 Overview](#-project-overview)
- [🏗️ Architecture](#️-architecture)
- [☁️ AWS Services](#️-aws-services)
- [✨ Features](#-key-features)
- [🚀 Deployment](#-deployment)
- [🍃 MongoDB Atlas](#-mongodb-atlas)
- [🔐 Security](#-security)
- [📊 Monitoring](#-monitoring)
- [🧪 Testing](#-testing)
- [💼 Resume](#-resume-description)

---

## 📌 Project Overview

The **Student Attendance & Result Management System** provides a centralized platform for managing student records, attendance and academic results.

```text
Route 53 → ALB → EC2 Backend/API → MongoDB Atlas
                    ↑
              CloudWatch Monitoring

S3 → Static Frontend
```

### 🎯 Project Goals

- Deploy a real-world application on AWS
- Build a secure and scalable cloud architecture
- Separate frontend, backend and database layers
- Implement managed DNS and load balancing
- Use MongoDB Atlas as the managed database layer
- Demonstrate AWS networking, security and monitoring
- Build a strong DevOps/Cloud portfolio project

---

# 🏗️ Architecture

<details open>
<summary><strong>🏗️ View AWS Architecture</strong></summary>

```text
                         🌐 INTERNET
                              |
                              v
                    +------------------+
                    |    Route 53      |
                    |  Custom Domain   |
                    +--------+---------+
                             |
                  +----------+----------+
                  |                     |
                  v                     v
          +-------------+       +------------------+
          |     S3      |       |       ALB        |
          |   Frontend  |       | Application Load |
          +-------------+       |    Balancer      |
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
       ACM → HTTPS
       CloudWatch → Monitoring & Logs
```

</details>

---

# 🔄 Request Flow

<details open>
<summary><strong>🔄 Click to view end-to-end request flow</strong></summary>

```text
👤 User
  ↓
🌐 Route 53
  ↓
🔒 HTTPS / ACM
  ↓
⚖️ Application Load Balancer
  ↓
🏥 Healthy EC2 Backend
  ↓
🔌 REST API
  ↓
🍃 MongoDB Atlas
  ↓
📦 JSON Response
  ↓
👤 User
```

### Frontend Flow

```text
User Browser
     ↓
Amazon S3
     ↓
Frontend Application
     ↓
Route 53 / API Domain
     ↓
Application Load Balancer
```

</details>

---

# ☁️ AWS Services

| Service | Role |
|---|---|
| Amazon VPC | Secure cloud networking |
| Amazon EC2 | Backend/API compute |
| Application Load Balancer | Traffic distribution & health checks |
| Amazon Route 53 | DNS and custom domain |
| Amazon S3 | Static frontend hosting |
| AWS IAM | Identity and access management |
| Security Groups | Network-level security |
| AWS CloudWatch | Metrics, logs and monitoring |
| AWS Certificate Manager | HTTPS/SSL certificates |
| AWS Systems Manager | Secure EC2 administration |
| AWS Secrets Manager / Parameter Store | Secure application secrets |
| MongoDB Atlas | Managed database |

> **Architecture note:** MongoDB Atlas is used only as the database layer. The compute, networking, DNS, storage, security and monitoring architecture is AWS-based.

<details>
<summary>➕ Recommended advanced AWS extensions</summary>

```text
AWS WAF                 → Web application protection
Auto Scaling            → Automatic EC2 scaling
ECR                     → Docker image registry
CodeBuild/CodePipeline  → CI/CD automation
SNS                     → Monitoring notifications
CloudTrail              → AWS activity auditing
```

</details>

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

---

# 📁 Project Structure

```text
Student_Attendance_AWS_Project/
│
├── frontend/
├── backend/
├── database/
├── aws/
│   └── deployment-guide.md
├── docs/
└── README.md
```

---

# 🚀 Deployment

### 📖 Complete Deployment Guide

👉 **[Open the AWS Click-by-Click Deployment Guide](Student_Attendance_AWS_Project/aws/deployment-guide.md)**

The guide covers VPC, subnets, IAM, Security Groups, EC2, MongoDB Atlas, ALB, S3, Route 53, ACM/HTTPS, CloudWatch, testing, troubleshooting and cleanup.

# 🖥️ Recommended Infrastructure

<details open>
<summary><strong>🖥️ Click to view infrastructure resources</strong></summary>

| Resource | Recommended | Purpose |
|---|---:|---|
| VPC | 1 | Network isolation |
| Availability Zones | 2 | High availability |
| Public Subnets | 2 | ALB / public components |
| Private Subnets | 2 | Recommended application isolation |
| EC2 Instances | 2 | Backend/API high availability |
| Application ALB | 1 | Load balancing |
| Target Group | 1 | EC2 health & routing |
| S3 Bucket | 1 | Static frontend |
| Route 53 Hosted Zone | 1 | Custom DNS |
| ACM Certificate | 1 | HTTPS |
| MongoDB Atlas Cluster | 1 | Managed database |
| CloudWatch | 1 service | Monitoring & logs |

### Why 2 EC2 instances?

```text
                    Application Load Balancer
                           /          \
                          /            \
                    EC2 AZ-1        EC2 AZ-2
                       🟢               🟢
                         \             /
                          \           /
                         MongoDB Atlas
```

Benefits:

- 🔄 Load distribution
- ❤️ Health checks
- 🛡️ Better fault tolerance
- 🌍 Multi-AZ architecture
- 📈 Easier future scaling

### 💰 Low-cost learning mode

For initial testing, you can start with **1 EC2 instance** and later move to the 2-EC2 Multi-AZ design.

> ⚠️ ALB, NAT Gateway, public IPv4 addresses and other AWS resources may incur charges. Check current AWS pricing before deployment.

</details>

---

# 🍃 MongoDB Atlas

```text
Database: studentdb

Collections:
├── students
├── attendance
├── results
└── users
```

Example environment variables:

```bash
export MONGODB_URI="<MONGODB_ATLAS_CONNECTION_STRING>"
export DB_NAME="studentdb"
```

⚠️ Never commit database credentials, connection strings or `.env` files.

---

# 🔐 Security

- IAM least-privilege access
- Restricted EC2 Security Groups
- ALB as the public backend entry point
- HTTPS using ACM
- MongoDB Atlas network restrictions
- Secure secret storage
- No credentials in source code
- SSH restricted to My IP when required
- CloudWatch monitoring
- CloudTrail recommended for audit visibility

```text
.env
MONGODB_URI
MONGODB_PASSWORD
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
*.pem
```

**These files/secrets must never be committed to GitHub.**

---

# 📊 Monitoring

| Layer | What to monitor |
|---|---|
| EC2 | CPU, network, status checks |
| ALB | Requests, 4XX, 5XX, target health, response time |
| Application | Backend logs, API errors, database connectivity |

---

# 🧪 Testing

```bash
aws sts get-caller-identity
curl http://localhost/
curl http://localhost/api/students
curl http://<ALB_DNS_NAME>/
nslookup attendance.yourdomain.com
curl -I https://attendance.yourdomain.com/
```

---

# 🛠️ Useful AWS CLI

```bash
aws ec2 describe-instances --output table
aws ec2 describe-vpcs --output table
aws ec2 describe-subnets --output table
aws elbv2 describe-load-balancers --output table
aws elbv2 describe-target-groups --output table
aws elbv2 describe-target-health --target-group-arn <TARGET_GROUP_ARN>
aws s3 ls
aws route53 list-hosted-zones --output table
```

---

# 🧹 Cost & Cleanup

When the project is no longer required, remove unused resources such as ALB, EC2 instances, NAT Gateway, unused Elastic IPs, S3 resources, Route 53 hosted zones and the MongoDB Atlas cluster.

> 💰 Always check AWS Billing before and after deployment.

---

# 📚 Learning Outcomes

```text
AWS Cloud | VPC | EC2 | ALB | Route 53 | S3 |
IAM | Security Groups | CloudWatch | ACM |
AWS CLI | REST APIs | MongoDB Atlas | Linux |
DNS | High Availability | Multi-AZ | Cloud Security
```

---

# 💼 Resume Description

### Student Attendance & Result Management System — AWS + MongoDB Atlas

> Designed and deployed a cloud-based student attendance and result management application using AWS VPC, EC2, Application Load Balancer, Route 53, S3, IAM, Security Groups, CloudWatch and ACM, with MongoDB Atlas as the managed database. Implemented REST APIs, multi-AZ backend deployment, secure DNS/HTTPS configuration, database integration and cloud monitoring.

### Skills

`AWS` `EC2` `VPC` `ALB` `Route 53` `S3` `IAM` `CloudWatch` `ACM` `AWS CLI` `REST API` `MongoDB Atlas` `Linux` `Cloud Security`

---

# 🎯 Interview Highlights

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

---

# 👨‍💻 Author

**Nitin Rathod**  
AWS • DevOps • Cloud Computing

---

## ⭐ Project Status

| Area | Status |
|---|---|
| AWS Cloud Architecture | ✅ |
| MongoDB Atlas Integration | ✅ |
| Route 53 Architecture | ✅ |
| ALB Architecture | ✅ |
| Multi-AZ EC2 Design | ✅ |
| Security & Monitoring Design | ✅ |
| Deployment Guide | ✅ |

> ⭐ Built as a hands-on AWS & DevOps portfolio project.
