# 🚀 Student Attendance & Result Management System — AWS Deployment Guide

This guide deploys the project using **AWS + MongoDB Atlas** with Route 53, Application Load Balancer, EC2, S3, IAM, VPC, Security Groups and CloudWatch.

## 🏗️ Final Architecture

```text
User → Route 53 → HTTPS/ACM → Application Load Balancer
                                  ↓
                         ┌────────┴────────┐
                         ↓                 ↓
                       EC2-1             EC2-2
                         └────────┬────────┘
                                  ↓
                           MongoDB Atlas

Static frontend → Amazon S3
Monitoring → CloudWatch
Security → IAM + Security Groups
```

---

# 1. Recommended AWS Resources

For the full architecture create:

```text
VPC                 1
Availability Zones  2
Public Subnets      2
Private Subnets     2 (recommended)
Internet Gateway    1
NAT Gateway         1 (optional; may cost money)
EC2 Instances       2
Application ALB     1
Target Group        1
S3 Bucket           1
Route 53 Hosted Zone 1
ACM Certificate     1
IAM EC2 Role        1
Security Groups     2
MongoDB Atlas       1 cluster
CloudWatch          automatic
```

### Low-cost learning setup

You can initially use **1 EC2** to test the application. For the final ALB/high-availability architecture, use **2 EC2 instances in 2 Availability Zones**.

> ALB, NAT Gateway, EC2, public IPv4 and other resources can incur charges. Check current AWS pricing and delete resources after testing.

---

# 2. Select AWS Region

AWS Console → Region selector → choose one region, for example:

```text
Asia Pacific (Mumbai)
ap-south-1
```

Keep VPC, EC2, ALB and related AWS resources in the same region.

---

# 3. Create VPC — Click by Click

AWS Console → **VPC → Your VPCs → Create VPC**.

Select **VPC and more** and enter:

```text
Name: student-attendance-vpc
IPv4 CIDR: 10.0.0.0/16
Availability Zones: 2
Public subnets: 2
Private subnets: 2
NAT gateways: 1 (or None for low-cost testing)
VPC endpoints: None
```

Click **Create VPC**.

Verify:

```bash
aws ec2 describe-vpcs --filters Name=tag:Name,Values=student-attendance-vpc
aws ec2 describe-subnets
```

---

# 4. Verify Internet Gateway

VPC → **Internet gateways**.

Confirm the Internet Gateway is attached to `student-attendance-vpc`.

```bash
aws ec2 describe-internet-gateways
```

---

# 5. Create IAM Role for EC2

IAM → Roles → **Create role**.

```text
Trusted entity: AWS service
Use case: EC2
```

Attach:

```text
AmazonSSMManagedInstanceCore
```

If S3 access is required, add a least-privilege S3 policy rather than AdministratorAccess.

Role name:

```text
student-attendance-ec2-role
```

Click **Create role**.

---

# 6. Create Security Groups

EC2 → Security Groups → Create security group.

## 6.1 ALB Security Group

```text
Name: student-alb-sg
```

Inbound:

```text
HTTP  80   → 0.0.0.0/0
HTTPS 443  → 0.0.0.0/0
```

Outbound: All traffic.

## 6.2 EC2 Security Group

```text
Name: student-ec2-sg
```

Inbound:

```text
HTTP 80 → student-alb-sg
SSH 22 → My IP (only if SSH is required)
```

Do not expose the backend HTTP port directly to the whole internet when ALB is the public entry point.

---

# 7. Create EC2-1

EC2 → Instances → **Launch instance**.

Use:

```text
Name: student-attendance-ec2-1
AMI: Amazon Linux 2023
Instance type: t3.micro (if suitable for your account)
VPC: student-attendance-vpc
Subnet: Public Subnet AZ-1
Auto-assign Public IP: Enable
Security group: student-ec2-sg
IAM instance profile: student-attendance-ec2-role
Storage: 8–20 GiB gp3
```

Select/create your key pair and click **Launch instance**.

---

# 8. Create EC2-2

Repeat the same process:

```text
Name: student-attendance-ec2-2
AMI: Amazon Linux 2023
Instance type: t3.micro
VPC: student-attendance-vpc
Subnet: Public Subnet AZ-2
Auto-assign Public IP: Enable
Security group: student-ec2-sg
IAM instance profile: student-attendance-ec2-role
Storage: 8–20 GiB gp3
```

Click **Launch instance**.

### Why 2 EC2?

The ALB distributes requests between both backend instances and can stop routing traffic to an unhealthy target.

---

# 9. Connect to EC2

Console method:

EC2 → Instances → select instance → **Connect → EC2 Instance Connect → Connect**.

SSH method:

```bash
chmod 400 <YOUR_KEY>.pem
ssh -i <YOUR_KEY>.pem ec2-user@<EC2_PUBLIC_IP>
```

---

# 10. Install Backend Software

Run on **both EC2 instances**:

```bash
sudo dnf update -y
sudo dnf install -y python3 python3-pip git
python3 --version
pip3 --version
```

Clone the project:

```bash
git clone https://github.com/nitindrathod4-alt/student-attendance-aws-project.git
cd student-attendance-aws-project
```

Go to the backend directory:

```bash
cd Student_Attendance_AWS_Project/backend
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

---

# 11. Create MongoDB Atlas Database

MongoDB Atlas → create/select project → **Build a Database** → create cluster.

Then:

**Database Access → Add New Database User**

Example:

```text
Username: attendance_app
Database: studentdb
```

Give the minimum required database permissions.

## Network Access

MongoDB Atlas → **Security → Network Access → Add IP Address**.

Allow only the required EC2 application egress IP/network configuration.

Avoid permanent `0.0.0.0/0` access.

## Get URI

MongoDB Atlas → Database → **Connect → Drivers** → Python → copy connection string.

---

# 12. Configure MongoDB on EC2

On each EC2:

```bash
export MONGODB_URI='mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>/<DATABASE>?retryWrites=true&w=majority'
export DB_NAME='studentdb'
```

Check only the non-secret variable:

```bash
echo "$DB_NAME"
```

Never commit the MongoDB URI/password to GitHub.

For production, use AWS Secrets Manager or Systems Manager Parameter Store instead of putting secrets directly in shell/service files.

---

# 13. Test Backend

From the backend directory:

```bash
python3 app.py
```

In another terminal:

```bash
curl http://localhost/
curl http://localhost/api/students
```

If the application uses port 5000:

```bash
curl http://localhost:5000/
```

The application must listen on `0.0.0.0` for ALB access.

Stop temporary execution with `CTRL+C`.

---

# 14. Create Target Group

EC2 → **Target Groups → Create target group**.

```text
Target type: Instances
Name: student-attendance-tg
Protocol: HTTP
Port: 80
VPC: student-attendance-vpc
Health check protocol: HTTP
Health check path: /
```

Click **Next**.

Select both:

```text
student-attendance-ec2-1
student-attendance-ec2-2
```

Click **Include as pending below → Create target group**.

Wait for target health.

---

# 15. Create Application Load Balancer

EC2 → Load Balancers → **Create Load Balancer → Application Load Balancer**.

```text
Name: student-attendance-alb
Scheme: Internet-facing
IP address type: IPv4
VPC: student-attendance-vpc
Availability Zones: 2
Subnets: Public Subnet AZ-1 + Public Subnet AZ-2
Security group: student-alb-sg
Listener: HTTP : 80
Default action: student-attendance-tg
```

Click **Create load balancer**.

---

# 16. Test ALB

EC2 → Load Balancers → `student-attendance-alb` → copy DNS name.

```bash
curl http://<ALB_DNS_NAME>/
curl http://<ALB_DNS_NAME>/api/students
```

Browser:

```text
http://<ALB_DNS_NAME>/
```

Both targets should become **Healthy**.

---

# 17. Upload Frontend to S3

S3 → **Create bucket**.

Example:

```text
student-attendance-<unique-name>
```

Upload the frontend files:

```bash
aws s3 cp Student_Attendance_AWS_Project/frontend/ s3://<BUCKET_NAME>/ --recursive
```

Keep sensitive information out of S3/frontend files.

---

# 18. Configure Frontend API

Open:

```text
Student_Attendance_AWS_Project/frontend/js/app.js
```

For temporary testing:

```javascript
const API_URL = "http://<ALB_DNS_NAME>/api/students";
```

For final production:

```javascript
const API_URL = "https://attendance.yourdomain.com/api/students";
```

Upload updated files:

```bash
aws s3 cp Student_Attendance_AWS_Project/frontend/ s3://<BUCKET_NAME>/ --recursive
```

---

# 19. Route 53 Domain

Route 53 → **Hosted zones → Create hosted zone**.

```text
Domain name: yourdomain.com
Type: Public hosted zone
```

If your domain is registered outside Route 53, copy the Route 53 nameservers and replace the registrar's nameservers with them.

---

# 20. Route 53 Alias to ALB

Route 53 → Hosted zones → your domain → **Create record**.

Example:

```text
Record name: attendance
Record type: A
Alias: ON
Route traffic to: Application Load Balancer
Region: ap-south-1
Target: student-attendance-alb
```

Click **Create records**.

Test:

```bash
nslookup attendance.yourdomain.com
dig attendance.yourdomain.com
```

---

# 21. HTTPS with ACM

AWS Certificate Manager → **Request certificate → Public certificate**.

Domain:

```text
attendance.yourdomain.com
```

Choose **DNS validation** and create the validation record in Route 53.

Wait for:

```text
Status: Issued
```

Then:

EC2 → Load Balancers → ALB → Listeners → **Add listener**.

```text
Protocol: HTTPS
Port: 443
Certificate: ACM certificate
Default action: student-attendance-tg
```

Change HTTP 80 listener to redirect to HTTPS 443.

Final URL:

```text
https://attendance.yourdomain.com
```

---

# 22. Run Backend as systemd Service

On each EC2:

```bash
sudo nano /etc/systemd/system/student-attendance.service
```

Example:

```ini
[Unit]
Description=Student Attendance Backend
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/student-attendance-aws-project/Student_Attendance_AWS_Project/backend
ExecStart=/usr/bin/python3 app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Configure MongoDB credentials securely using Secrets Manager/Parameter Store or another secure mechanism; do not hard-code the password in this file.

Enable service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable student-attendance
sudo systemctl start student-attendance
sudo systemctl status student-attendance
```

Logs:

```bash
sudo journalctl -u student-attendance -f
```

Repeat on EC2-2.

---

# 23. Verify Target Health

EC2 → Target Groups → `student-attendance-tg` → Targets.

Expected:

```text
EC2-1 → Healthy
EC2-2 → Healthy
```

If unhealthy:

```bash
curl http://localhost/
sudo systemctl status student-attendance
sudo journalctl -u student-attendance --no-pager -n 100
```

Check target port, health-check path and security groups.

---

# 24. CloudWatch Monitoring

CloudWatch can monitor:

```text
EC2
 ├── CPUUtilization
 ├── NetworkIn / NetworkOut
 └── StatusCheckFailed

ALB
 ├── RequestCount
 ├── TargetResponseTime
 ├── HTTP 4XX / 5XX
 ├── HealthyHostCount
 └── UnHealthyHostCount
```

Create CloudWatch alarms for important production metrics.

---

# 25. Useful AWS CLI Commands

```bash
aws sts get-caller-identity
aws ec2 describe-vpcs
aws ec2 describe-subnets
aws ec2 describe-instances --output table
aws ec2 describe-security-groups --output table
aws elbv2 describe-load-balancers --output table
aws elbv2 describe-target-groups --output table
aws elbv2 describe-target-health --target-group-arn <TARGET_GROUP_ARN>
aws s3 ls
aws route53 list-hosted-zones --output table
```

---

# 26. End-to-End Testing

DNS:

```bash
nslookup attendance.yourdomain.com
```

HTTPS:

```bash
curl -I https://attendance.yourdomain.com/
```

API:

```bash
curl https://attendance.yourdomain.com/api/students
```

Browser:

```text
https://attendance.yourdomain.com
```

Verify:

```text
✓ Login
✓ Student registration
✓ Student search
✓ Attendance tracking
✓ Attendance percentage
✓ Result management
✓ Admin dashboard
✓ REST API
✓ MongoDB persistence
✓ ALB target health
✓ Route 53 DNS
✓ HTTPS
```

---

# 27. Troubleshooting

## 502 Bad Gateway

Check:

```bash
sudo systemctl status student-attendance
sudo journalctl -u student-attendance -n 100 --no-pager
curl http://localhost/
```

Also verify target port, application listening address and EC2 security group.

## MongoDB connection error

Check:

```text
MONGODB_URI
DB_NAME
MongoDB Atlas user
MongoDB Atlas Network Access
EC2 outbound connectivity
```

## Route 53 not resolving

```bash
nslookup attendance.yourdomain.com
dig attendance.yourdomain.com
```

Verify the Alias record points to the correct ALB and nameservers are correct at the registrar.

## Target unhealthy

Verify:

```text
Backend process running
Correct application port
Correct target group port
Correct health check path
ALB → EC2 security group rule
```

---

# 28. Cleanup — Avoid Unwanted Charges

When finished testing:

```text
1. Delete Route 53 records/hosted zone if unused
2. Delete ALB
3. Delete Target Group
4. Terminate EC2-1
5. Terminate EC2-2
6. Delete NAT Gateway if created
7. Release unused Elastic IPs
8. Delete S3 objects/bucket if no longer needed
9. Remove unused VPC resources
10. Delete MongoDB Atlas cluster if no longer needed
11. Check AWS Billing
```

---

# 29. Final Checklist

```text
☐ VPC created
☐ 2 Availability Zones
☐ 2 Public Subnets
☐ 2 EC2 instances
☐ IAM role attached
☐ ALB security group created
☐ EC2 security group created
☐ MongoDB Atlas cluster created
☐ MongoDB network access configured
☐ Backend running on EC2-1
☐ Backend running on EC2-2
☐ Target group created
☐ Both targets healthy
☐ ALB created
☐ Frontend uploaded to S3
☐ Route 53 hosted zone configured
☐ Route 53 Alias → ALB
☐ ACM certificate issued
☐ HTTPS listener configured
☐ Frontend API URL updated
☐ CloudWatch monitoring verified
☐ End-to-end application tested
```

## 🎯 Final Flow

```text
User
 ↓
Route 53
 ↓
ACM / HTTPS
 ↓
Application Load Balancer
 ↓
EC2-1 + EC2-2
 ↓
MongoDB Atlas

Frontend → S3
Monitoring → CloudWatch
Security → IAM + Security Groups
```

**Deployment complete. 🎉**
