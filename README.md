# plant-watering-reminder-aws-iot
An IoT-based Plant Watering Reminder System built using AWS IoT Core, AWS Lambda, and Amazon SNS. The system monitors soil moisture levels in real time and sends email or SMS notifications to users when plants need watering.
📌 Abstract
This project presents an IoT-based Plant Watering Reminder System that helps users maintain healthy plants by monitoring soil moisture levels. The system uses AWS IoT Core to receive sensor data, AWS Lambda to process the data, and Amazon SNS to send watering reminders via email or SMS when moisture drops below a defined threshold.
📌 Problem Statement
Many people forget to water their plants regularly, leading to unhealthy or dead plants. Manual monitoring of soil moisture is inefficient and inconvenient.
📌 Solution
The proposed system automatically monitors soil moisture using an IoT sensor and sends real-time notifications when watering is required, ensuring timely plant care.
📌 Technologies Used
AWS IoT Core
AWS Lambda
Amazon SNS
MQTT Protocol
ESP32 / Arduino (conceptual)
Python
JSON
📌 System Architecture
Soil Moisture Sensor
        ↓
   IoT Device (ESP32)
        ↓  (MQTT)
   AWS IoT Core
        ↓
   AWS Lambda
        ↓
   AmazonSNS
        ↓
 Email / SMS Notification
 📌 Workflow
Soil moisture sensor reads moisture value
Device publishes data to AWS IoT Core
Lambda function evaluates moisture level
If below threshold → SNS sends notification
User receives email or SMS alert
📌 Advantages
Automated plant care reminders
Real-time monitoring
Serverless and scalable
Low maintenance system
📌 Future Enhancements
Mobile app integration
Dashboard using AWS QuickSight
Automatic watering system
Multi-plant support
🌱 Plant Watering Reminder System using AWS IoT
📖 Overview
This project is an IoT-based system that monitors soil moisture levels and sends notifications to users when their plant needs watering.
It uses AWS cloud services such as AWS IoT Core, AWS Lambda, and Amazon SNS to provide a scalable and serverless solution.
🛠️ Technologies
AWS IoT Core
AWS Lambda
Amazon SNS
Python
MQTT
JSON
🏗️ Architecture
IoT Device → AWS IoT Core → AWS Lambda → Amazon SNS → Email / SMS
🚀 Features
Real-time soil moisture monitoring
Automated watering reminders
Email and SMS notifications
Serverless cloud architecture
📂 Repository Structure
plant-watering-reminder-aws-iot/
│
├── README.md
├── report/
│   └── project-report.md
│
├── lambda/
│   └── moisture_check.py
│
├── iot/
│   ├── device-simulator.py
│   └── payload.json
│
├── sns/
│   └── sns-setup.md
│
├── architecture/
│   └── architecture-diagram.png
│
└── docs/

    ├── setup-guide.md
    └── workflow.md
    ⚙️ Setup Overview
Create an IoT Thing in AWS IoT Core
Attach IoT policy and certificates
Deploy Lambda function
Create SNS topic and subscription
Publish moisture data via MQTT
✅ Outcome
Automated plant watering reminders
Improved plant health
Hands-on experience with AWS IoT services
Developed an IoT-based Plant Watering Reminder System using AWS IoT Core,
AWS Lambda, and Amazon SNS to monitor soil moisture and send automated
email/SMS alerts for timely plant watering.
Interview One-Line Explanation
“Sensor data is sent to AWS IoT Core, processed by Lambda, and SNS sends alerts when moisture drops below threshold.”
