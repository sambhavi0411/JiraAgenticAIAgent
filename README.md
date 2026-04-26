# 🤖 AI Agent for Automatic JIRA Ticket Creation

## 📌 Overview
This project is an **Agentic AI system** that automatically analyzes issues (like logs, errors, or user messages) and creates **JIRA tickets** without manual intervention.

The goal is to reduce manual effort, improve response time, and automate issue tracking in a production environment.

---

## 🚀 What This Project Does

1. Takes input from a source (logs / API / Slack message)
2. Uses an AI model to understand the issue
3. Decides whether a JIRA ticket should be created
4. Extracts important details:
   - Title
   - Description
   - Priority
5. Automatically creates a JIRA ticket using REST API

---

## 🧠 Why This is "Agentic AI"

This is not just automation. The system:
- **Understands context** using AI
- **Makes decisions** (create ticket or ignore)
- **Uses tools** (JIRA API)
- Can be extended with memory, retries, and validations

---

## 🏗️ Architecture
Input Source (Logs / API / Slack)
↓
AI Agent (LLM)
↓
Decision Logic
↓
JIRA API Call
↓
Ticket Created

## 🔄 Workflow

1. User or system sends input (error/log/message)
2. AI processes input and generates structured output
