

## 📬 How to Use the API

Here are all the ways you can interact with the API:

---

### 📥 GET Request (Fetch all names)
**URL:** `http://127.0.0.1:8000/`  
**Method:** `GET`  
**What it does:** Returns a list of all names.

#### Example Output:
```json
["Mahneera", "Mindi", "Minhera"]
```

---

### ➕ POST Request (Add a new name)
**URL:** `http://127.0.0.1:8000/`  
**Method:** `POST`  
**What it does:** Adds a new name to the list.

#### Request Body (JSON):
```json
{
  "name": "John"
}
```

#### Example Output:
```json
["Mahneera", "Mindi", "Minhera", "John"]
```

---

### ❌ DELETE Request (Remove a name)
**URL:** `http://127.0.0.1:8000/{name}`  
**Method:** `DELETE`  
**What it does:** Deletes a name from the list by matching it.

#### Example:
`http://127.0.0.1:8000/John`  
This will remove "John" from the list.

---

### 🔁 PUT Request (Update a name)
**URL:** `http://127.0.0.1:8000/{name}`  
**Method:** `PUT`  
**What it does:** Replaces an existing name with a new one.

#### Example:
You want to change "John" to "Johnny".

**URL:** `http://127.0.0.1:8000/John`  
**Request Body (JSON):**
```json
{
  "name": "Johnny"
}
```

#### Example Output:
```json
["Mahneera", "Mindi", "Minhera", "Johnny"]
```

---

## ✅ Summary of Endpoints

| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| GET    | `/`                 | Get all names        |
| POST   | `/`                 | Add a new name       |
| DELETE | `/{name}`           | Delete a name        |
| PUT    | `/{name}`           | Update a name        |

---

## 🎉 Done!

Now you have a working API to play with!  
You can test it using [Postman](https://www.postman.com/) or any REST client.

 