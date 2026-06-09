# 💻 Laptop Price Prediction & Analytics System

An end-to-end full-stack application that combines **Advanced Database concepts** with **Machine Learning** to analyze laptop listings, provide interactive analytics dashboards, and predict laptop prices in real time.

---

## 📌 Project Overview

The **Laptop Price Prediction & Analytics System** is designed to manage and analyze large-scale e-commerce laptop data using modern technologies. The system allows users to:

* Store and manage laptop listings efficiently.
* Perform advanced analytical queries and aggregations.
* Predict laptop prices using a trained Machine Learning model.
* Visualize insights through an interactive dashboard.
* Manage user accounts securely using authentication and authorization.

The project integrates database technologies with machine learning to deliver a production-ready intelligent application.

> "A complete Advanced Database solution enhanced with AI-powered price prediction."

---

## 🚀 Features

### 🔐 User Authentication

* User registration (Sign Up)
* Secure login using JWT authentication
* Password hashing
* Protected API endpoints

### 📊 Analytics Dashboard

* Dataset statistics
* Interactive visualizations
* Price distributions
* Country-based analysis
* Product condition analysis

### 🤖 Machine Learning Prediction

* Predict laptop prices based on specifications.
* Real-time inference through FastAPI.
* Save prediction history for each user.

### 🗄️ Advanced Database Operations

* CRUD operations
* Aggregation pipelines
* Indexing optimization
* Transactions
* Rollback mechanisms
* Replica set support

### 👤 User Management

* Profile management
* Usage tracking
* Secure account deletion
* Automatic deletion of related prediction records.

---

## 🏗️ System Architecture

```text
React Frontend
      ↓
FastAPI Backend
      ↓
MongoDB Atlas
      ↓
Machine Learning Model
(Random Forest)
```

---

## 🛠️ Tech Stack

### Frontend

* React.js
* JavaScript
* HTML/CSS

### Backend

* FastAPI
* Python

### Database

* MongoDB Atlas
* PyMongo

### Machine Learning

* Scikit-learn
* Random Forest Regressor
* SHAP Explainability

### Authentication

* JWT Tokens
* Password Hashing

---

## 📂 Dataset Information

The dataset was collected using **web scraping techniques** from e-commerce platforms selling laptops.

### Dataset Characteristics

* Total Records: **5,000 laptop listings**
* Format: Structured/Semi-Structured
* Storage: MongoDB Documents (JSON)

### Main Features

#### Product Information

* Title
* Price
* Condition

#### Hardware Specifications

* RAM (GB)
* Storage (GB)
* Processor
* Screen Size (Inches)

#### Seller Information

* Seller Name
* Seller Score
* Seller Reviews

#### Logistics

* Shipping Cost
* Country

#### Metadata

* Created At
* Updated At

---

## 🗃️ Database Design

### Users Collection

Stores user information and authentication data.

Fields:

```text
User ID
Name
Email
Password (Hashed)
Created At
```

---

### Dataset Collection

Stores laptop listings used for analytics and model training.

Fields:

```text
Title
Price
RAM_GB
Storage_GB
Processor
Screen_Size_Inch
Condition
Shipping_Cost
Seller_Score
Seller_Reviews
Country
Listing_Type
Created_At
```

---

### Predictions Collection

Stores prediction history for each user.

Fields:

```text
Prediction ID
User ID
Input Features
Predicted Price
Model Version
Created At
```

---

## 🧹 Data Preprocessing

The raw dataset underwent several preprocessing steps:

* Removed duplicate records.
* Handled missing values.
* Standardized categorical variables.
* Normalized numerical features.
* Prepared data for analytics and machine learning.

Processed features included:

```text
Price
RAM_GB
Storage_GB
Shipping_Cost
Condition
Country
Processor
```

---

## 🤖 Machine Learning Model

### Model Used

```text
Random Forest Regressor
```

### Objective

Predict laptop prices based on hardware specifications and listing attributes.

### Workflow

1. Data preprocessing.
2. Feature engineering.
3. Model training.
4. Model evaluation.
5. SHAP explainability.
6. Deployment through FastAPI.

---

## 🔍 Explainable AI

The system incorporates **SHAP (SHapley Additive Explanations)** to interpret model predictions.

Benefits include:

* Feature importance analysis.
* Increased model transparency.
* Better understanding of prediction outcomes.
* Improved trust in AI decisions.

---

## 🌐 API Endpoints

### Authentication

#### Register

```http
POST /signup
```

Creates a new user account.

---

#### Login

```http
POST /login
```

Authenticates users and returns a JWT token.

---

### User Profile

#### Get Profile

```http
GET /profile
```

Returns authenticated user information.

---

### Prediction

#### Predict Laptop Price

```http
POST /predict
```

Returns predicted laptop price and stores the prediction.

---

### Dashboard

#### Analytics Statistics

```http
GET /dashboard/stats
```

Returns analytical insights and dashboard data.

---

### Account Management

#### Delete Account

```http
DELETE /delete-account
```

Deletes user data and associated predictions using transactions.

---

## 🔄 CRUD Operations

### Create

* Register users.
* Login users.
* Save predictions.

### Read

* Retrieve profiles.
* View prediction history.
* Access dashboard analytics.

### Update

* Modify user information.
* Update usage statistics.

### Delete

* Delete accounts securely.
* Remove associated prediction records atomically.

---

## ⚡ MongoDB Indexing

Indexes were implemented to improve performance.

Examples:

```text
users.email
predictions.user_id
```

Benefits:

* Faster authentication.
* Efficient retrieval of prediction history.
* Improved query execution.

---

## 📈 Aggregation Pipelines

Implemented MongoDB aggregations including:

### Dataset Statistics

* Count
* Average Price
* Minimum Price
* Maximum Price

### Price Distribution

Using:

```text
$bucket
```

### Top Conditions Analysis

Identify the most common product conditions.

### Country Analysis

Top countries by listing count.

### Average Price Analysis

Average price grouped by condition.

### Collection Joins

Using:

```text
$lookup
```

to combine users and predictions.

---

## 🔐 Transactions & Replication

### Transactions

Ensured atomic operations during account deletion.

Features:

* Verification before deletion.
* Commit on success.
* Rollback on failure.

### Replication

MongoDB Replica Sets were used to provide:

* High availability.
* Data redundancy.
* Improved reliability.

---

## 📊 Results

The system successfully:

✅ Built a full-stack intelligent application.

✅ Integrated MongoDB Atlas, FastAPI, React, and Machine Learning.

✅ Delivered real-time laptop price prediction.

✅ Implemented advanced database concepts.

✅ Provided interactive analytical dashboards.

✅ Supported secure user workflows.

---

## 🔮 Future Improvements

* Deploy the system to cloud platforms.
* Add recommendation capabilities.
* Support additional product categories.
* Implement continuous model retraining.
* Introduce advanced visualization dashboards.

---

## 👨‍💻 Authors

**Karim Gaber Ali Al-Shafi**
Student ID: 221003403

**Team Member**
Student ID: 231000323

---

## 👨‍🏫 Supervised By

* Prof. Osama Badawy
* Eng. Mazen Aziz

---

## 📄 License

This project was developed as part of the **DS311 – Advanced Database** course at the **Arab Academy for Science, Technology & Maritime Transport (AASTMT)** for educational purposes.
