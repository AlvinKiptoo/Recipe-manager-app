# Recipe Manager

##  Project Overview

The **Recipe Manager** is a web application that allows users to manage their favorite recipes. Users can view, add, and filter recipes by category. The app consists of a **Flask backend** and a **React frontend** connected via API requests.

##  Features

- View a list of recipes.
- Filter recipes by category.
- View detailed recipe information.
- Add new recipes.
- Fully functional REST API for managing recipes.

## Tech Stack

- **Frontend:** React, React Router
- **Backend:** Flask, Flask-RESTful, Flask-CORS
- **Database:** SQLite (or any other supported by Flask SQLAlchemy)
- **Deployment:** Render (backend) & Vercel (frontend)

## Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/recipe-manager.git
cd recipe-manager
```

### **2️⃣ Backend Setup (Flask)**

#### **Install Dependencies**

```bash
cd backend
pip install -r requirements.txt
```

#### **Run Flask Server**

```bash
flask run --port=5555
```

The backend will run at `http://localhost:5555`.

### **3️⃣ Frontend Setup (React)**

#### **Install Dependencies**

```bash
cd frontend
npm install
```

#### **Start React Development Server**

```bash
npm start
```

The frontend will run at `http://localhost:3000`.

##  Deployment

### **Deploy Backend on Render**

- Push the backend to GitHub.
- Create a new web service on **[Render](https://render.com/)**.
- Set the **start command**:
  ```bash
  gunicorn app:app
  ```
- Deploy & get your API URL.

### **Deploy Frontend on Vercel**

- Install Vercel globally:
  ```bash
  npm install -g vercel
  ```
- Deploy the frontend:
  ```bash
  vercel
  ```

## Project Structure

```
recipe-manager/
│── backend/              # Flask API
│   ├── app.py            # Main Flask app
│   ├── models.py         # Database models
│   ├── routes.py         # API routes
│   ├── db.sqlite         # SQLite database
│   ├── requirements.txt  # Python dependencies
│── frontend/             # React frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page components
│   │   ├── App.js        # Main App component
│   ├── package.json      # Node dependencies
│── README.md             # Project documentation
```

## API Endpoints

| Method | Endpoint        | Description             |
| ------ | --------------- | ----------------------- |
| GET    | `/recipes`      | Fetch all recipes       |
| POST   | `/recipes`      | Add a new recipe        |
| GET    | `/recipes/<id>` | Fetch a specific recipe |
| PUT    | `/recipes/<id>` | Update a recipe         |
| DELETE | `/recipes/<id>` | Delete a recipe         |
| GET    | `/categories`   | Fetch all categories    |
| POST   | `/categories`   | Add a new category      |

## Future Improvements

- User authentication (login/signup)
- Favorites & ratings for recipes
- Image upload for recipes

## Contributors

- **Your Name** - [GitHub Profile](https://github.com/yourusername)

## License

This project is open-source and available under the [MIT License](LICENSE).

---

The deployed backend link: "https://recipe-manager-app.onrender.com"

The deployed frontend link: "https://alvins-app.netlify.app/"