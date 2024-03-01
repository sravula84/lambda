# Lambda Deployment Guide

Follow these steps to deploy your Lambda function using the Serverless Framework.

## Prerequisites

- Make sure you have Node.js and npm installed on your machine.
- You need to have an AWS account and obtain your AWS access key and secret.

## Installation Steps

### 1. Install Serverless Framework

```bash
npm install -g serverless
```

### 2. Install Serverless Plugins

```bash
serverless plugin install -n serverless-python-requirements
```

### 3. Configure AWS Credentials

```bash
serverless config credentials --provider aws --key YOUR_KEY --secret YOUR_SECRET
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

### 5. Deploy Lambda

```bash
sls deploy
```
