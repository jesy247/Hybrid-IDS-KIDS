# Hybrid IDS (KIDS Project)

## 📌 Description
This project is a Hybrid Intrusion Detection System (IDS) that combines:
- Kernel-level monitoring using Linux Kprobes
- Behavioral analysis using Python and strace

## ⚙️ Technologies
- C (Kernel Module)
- Python
- Linux (Ubuntu / Kali)
- strace

## 🚀 Features
- Detects program execution in real-time
- Logs process name and PID
- Analyzes system calls behavior
- Flags suspicious programs

## ▶️ How to Run

make
sudo insmod kids.ko
sudo dmesg -wH | grep KIDS
python3 analyzer.py
sudo rmmod kids