# 📝 Blog API Documentation

Welcome to the **Blog API**! This backend allows you to:

* ✅ Sign up and authenticate users using JWT
* ✅ Create, read, update, and delete blog posts
* ✅ Secure access with token-based authentication



## 🔐 Authentication Overview

This API uses **JWT (JSON Web Tokens)** for authentication via the `Authorization: Bearer <access_token>` header.

You get two tokens when you log in or sign up:

* **Access Token**: Used for API access (short-lived)
* **Refresh Token**: Used to obtain a new access token (long-lived)



## 🚀 API Endpoints



### ✅ 1. **Signup (Register New User)**

* **URL**: `/api/signup/`

* **Method**: `POST`

* **Body** (JSON):

  ```json
  {
    "username": "yourname",
    "email": "you@example.com",
    "password": "yourpassword"
  }
  ```

* **Response (201 Created)**:

  ```json
  {
    "access": "<access_token>",
    "message": "Account created successfully."
    "refresh": "<refresh_token>",

  }
  ```
---

### 🔐 2. **Login**

* **URL**: `/api/login/`
* **Method**: `POST`
* **Body** (JSON):

  ```json
  {
    "email": "you@example.com",
    "password": "yourpassword"
  }
  ```
* **Response (200 OK)**:

  ```json
  {
    "refresh": "<refresh_token>",
    "access": "<access_token>"
  }
  ```

---

### 🔁 3. **Refresh Access Token**

* **URL**: `/api/token/refresh/`

* **Method**: `POST`

* **Body** (JSON):

  ```json
  {
    "refresh": "<your_refresh_token>"
  }
  ```

* **Response (200 OK)**:

  ```json
  {
    "access": "<new_access_token>"
  }
  ```

* ❗ **Note**: Refresh tokens are **blacklisted** after logout and cannot be reused.

---

### 🚪 4. **Logout**

* **URL**: `/api/logout/`

* **Method**: `POST`

* **Body** (JSON):

  ```json
  {
    "refresh": "<your_refresh_token>"
  }
  ```

* **Headers**:

  * `Authorization: Bearer <access_token>`

* **Response**:

  ```json
  {
    "detail": "Logout successful"
  }
  ```

* 🔒 Logs out the user by **blacklisting the refresh token**


## 📝 Blog Endpoints

This endpoints require `Authorization: Bearer <access_token>` in headers.



### 📥 5. **Create Blog**

* **URL**: `/api/blogs/`
* **Method**: `POST`
* **Body** (JSON):

  ```json
  {
    "title": "My First Blog",
    "content": "This is the blog content."
  }
  ```
* **Response**:

  ```json
  {
    "id": 1,
    "title": "My First Blog",
    "content": "This is the blog content.",
    "author": "yourname"
  }
  ```

---

### 📄 6. **List All Blogs**

* **URL**: `/api/blogs/`
* **Method**: `GET`
* **Response**:

  ```json
  [
    {
      "id": 1,
      "title": "My First Blog",
      "content": "This is the blog content.",
      "author": "yourname"
    },
    ...
  ]
  ```

---
### 📄 7. **List a Blog**

* **URL**: `/api/blogs/<id>/`
* **Method**: `GET`
* **Response**:

  ```json
  [
    {
      "id": 1,
      "title": "My First Blog",
      "content": "This is the blog content.",
      "author": "yourname"
    },
  ]
  ```

---


### 📝 8. **Update a Blog**
This endpoints require `Authorization: Bearer <access_token>` in headers.

* **URL**: `/api/blogs/<id>/`
* **Method**: `PUT`
* **Body**:

  ```json
  {
    "title": "Updated Title",
    "content": "Updated Content"
  }
  ```

---

### ❌ 8.9**Delete a Blog**
This endpoints require `Authorization: Bearer <access_token>` in headers.
* **URL**: `/api/blogs/<id>/edit/`
* **Method**: `DELETE`
* **Response**:

  * `204 No Content` on success


## ⚠️ Error Examples

### ❌ Invalid Login

```json
{
  "detail": "No active account found with the given credentials"
}
```

### ❌ Token Expired or Blacklisted

```json
{
  "detail": "Token is blacklisted",
  "code": "token_not_valid"
}
```


## 🔒 Security Notes

* Tokens are stored client-side (browser/app).
* Logout endpoint **blacklists the refresh token**, making it unusable.
* After logout, you must re-login to receive new tokens.
