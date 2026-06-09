# MongoDB Schema – Advanced DB Final Project
Database: `advanced_db`

## Collections
- `users`
- `dataset`
- `models`
- `predictions`

---

## 1) users
**Purpose:** Store user registration/login data.

### Fields
- `_id` : ObjectId
- `name` : string
- `email` : string (unique)
- `password_hash` : string
- `created_at` : date

### Example Document
```json
{
  "name": "Kareem Gaber",
  "email": "kareem@example.com",
  "password_hash": "hashed_password_here",
  "created_at": "2025-12-23T00:00:00Z"
}
"user_id": "<user ObjectId>"
