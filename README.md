# Baggage Guardian: AI-Powered Automated Baggage Counter System

**An intelligent, scalable solution for secure and efficient baggage management in large public spaces**

## 📋 Project Overview

**Baggage Guardian** is an advanced AI-driven automated baggage counter system engineered to enhance security and efficiency in high-traffic public environments such as malls, shops, and transportation hubs. Leveraging **Raspberry Pi** as the central processing unit, **ESP32** for IoT connectivity, an **electronic lock system** for secure access, and a **display screen** for user interaction, this platform automates the allocation of free counters, captures customer images, and securely encodes data into a centralized database. Upon reaching the assigned counter, customers scan to access their baggage, while the system continuously monitors bag retention times and alerts security to anomalies. Optimized for handling large datasets with minimal latency, BaggageGuardian simplifies management oversight and addresses the critical lack of safe, cost-effective baggage storage in public areas.

Developed by an Electronic & Telecommunication Engineering enthusiast, this project exemplifies cutting-edge hardware-software integration, real-time monitoring, and data optimization, making it a robust solution for modern public space challenges.

## 🚀 Features

- **AI-Driven Counter Allocation**:  
  Intelligently assigns free counters based on real-time availability using AI algorithms.
- **Secure Authentication**:  
  Captures customer images and encodes data into a centralized database, accessible via scanning at the counter.
- **Electronic Lock Integration**:  
  Utilizes ESP32-controlled electronic locks for secure baggage storage and release.
- **Real-Time Monitoring**:  
  Tracks baggage retention times and triggers security alerts for irregularities.
- **Low-Latency Data Handling**:  
  Implements optimization techniques to process large datasets efficiently, ensuring rapid response times.
- **User-Friendly Interface**:  
  Features a display screen for customer guidance and status updates.
- **Centralized Management**:  
  Provides administrators with a unified dashboard to oversee all counters and security events.

## 🛠️ Technologies Used

- **Hardware**: Raspberry Pi (core processor), ESP32 (IoT module), Electronic Lock System, LCD/LED Screen
- **Software**: Python (AI and control logic), SQLite/MySQL (central database), MQTT (real-time communication)
- **AI/ML**: TensorFlow Lite for image processing and anomaly detection
- **Tools**: Git for version control, Raspberry Pi OS, Arduino IDE for ESP32 programming
- **Optimization**: Custom caching and indexing for low-latency data retrieval

## 📈 System Architecture

BaggageGuardian employs a distributed architecture with:

- **Central Controller**: Raspberry Pi orchestrates AI processing, database management, and screen interactions.
- **IoT Layer**: ESP32 modules manage lock systems and sensor data, communicating via MQTT.
- **Database Layer**: SQLite/MySQL stores encrypted customer data, retention logs, and security alerts.
- **AI Module**: TensorFlow Lite processes images and monitors anomalies in real-time.
- **User Interface**: Custom-built display for customer interaction, integrated with hardware controls.

## 📝 Setup Instructions

### Prerequisites
- Raspberry Pi (Model 4B+ recommended)
- ESP32 Development Board
- Camera Module
- Electronic Lock System (12V compatible)
- LCD/LED Screen (HDMI or GPIO-compatible)
- Python 3.9+, TensorFlow Lite, SQLite/MySQL
- Internet connection for MQTT

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mugesram/Baggage-Guardian.git
   cd Baggage-Guardian
   ```
2. **Set Up Hardware**:
   - Connect ESP32 to electronic locks and sensors.
   - Attach LCD screen to Raspberry Pi via HDMI or GPIO.


## 🖥️ Usage

1. **Customer Workflow**:
   - Request a counter via the display screen.
   - Scan QR code or ID at the assigned counter to access baggage.
2. **Admin Workflow**:
   - Log in to the central dashboard to monitor counters and review alerts.
   - Configure thresholds for anomaly detection.
3. **Security Monitoring**:
   - System automatically flags bags left beyond the time limit and notifies security.

## 🌟 Why BaggageGuardian?

- **Security**: AI and electronic locks ensure safe baggage storage.
- **Efficiency**: Automates counter allocation and reduces management overhead.
- **Scalability**: Handles large crowds with optimized data processing.
- **Innovation**: Combines Raspberry Pi, ESP32, and AI for a cutting-edge solution.


## 🔮 Future Enhancements

- **Facial Recognition**: Enhance authentication with AI-based face matching.
- **Mobile App**: Develop a companion app for customer notifications.
- **Cloud Integration**: Sync data with a cloud server for multi-location management.
- **Energy Optimization**: Implement power-saving modes for hardware.

## 🤝 Contributing





## 📧 Contact

For inquiries or support, reach out via GitHub Issues or email Mugesh Krish at mugeshkrish007@gmail.com.

## 🌍 Acknowledgments

- University of Moratuwa for fostering technical innovation.
- Raspberry Pi and ESP32 communities for hardware support.
- Contributors and public space managers for valuable feedback.

---

**BaggageGuardian** redefines baggage management with AI precision and hardware synergy, ensuring safety and efficiency in crowded public spaces. Join us in advancing this transformative technology! 🌟
