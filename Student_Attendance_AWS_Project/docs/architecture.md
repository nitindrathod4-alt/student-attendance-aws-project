# AWS Architecture

```text
                         USER
                           |
                           v
                    +-------------+
                    | CloudFront  |
                    +------+------+
                           |
                           v
                    +-------------+
                    |     S3      |
                    |  Frontend   |
                    +------+------+
                           |
                         API
                           |
                           v
                    +-------------+
                    |     ALB     |
                    +------+------+
                           |
                 +---------+---------+
                 |                   |
                 v                   v
            +---------+         +---------+
            | EC2 AZ1 |         | EC2 AZ2 |
            | Backend |         | Backend |
            +----+----+         +----+----+
                 |                   |
                 +---------+---------+
                           |
                           v
                    +-------------+
                    | RDS MySQL   |
                    |  Database   |
                    +-------------+
```

Data flow: CloudFront serves S3 frontend; JavaScript calls ALB; ALB forwards to healthy EC2; backend reads RDS; JSON returns to frontend.
