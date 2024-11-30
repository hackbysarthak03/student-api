# Student API Calls 

Live: https://student-api-fus8.onrender.com/


API Calls using:

- MongoDB Database
- Python Backend ( Pymongo for Connecting to MongoDB )
- Fast API Framework


## API Routes Guide: Read before you begin!
```bash
  BASE URL: https://student-api-fus8.onrender.com
```

| Routes | Request Type     | Description                |
| :-------- | :------- | :------------------------- |
| `/api/students` | `GET` | List all Students |
| `/api/students` | `PUT` | To create a Student and return ID as response |
| `/api/students/{id}` | `GET` | To GET a student |
| `/api/students/{id}` | `PATCH` | To Update a student's field |
| `/api/students/{id}` | `DELETE` | To DELETE a student |






  
### Installation

1. Clone the repository:
```bash
git clone https://github.com/hackbysarthak03/whatbytes.git
```



2. Install dependencies:
```bash
pip install -r requirements.txt
```


3. In the project directory
```bash
fastapi dev app.py
```



And Boom 💥 your server started and now you can make API Calls!
