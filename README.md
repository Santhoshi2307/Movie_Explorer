🎬 **Movie Explorer Website**

A full-stack web application for browsing, filtering, and viewing movies, actors, and directors with detailed profiles.

------------------
🛠 **Tech Stack**

Layer        Technology

Frontend     React (Vite), Bootstrap

Backend      Python Flask (REST API)

Database     MongoDB

API Docs     Swagger / OpenAPI

------------------
 🚀**Getting Started**

1. Clone the Repository

 git clone https://github.com/yourusername/movie-explorer.git
 cd movie-explorer

2. Run with Docker (Recommended)

 make build    # Build both frontend & backend containers
 make up       # Start services (frontend, backend, mongo)

Access the app:

 Frontend: http://localhost:3000
 
 Backend API: http://localhost:5000
 
 Swagger Docs: http://localhost:5000/apidocs

🧪 **Testing**

 Backend Tests

  make test

 Frontend Tests

  cd frontend
  npm test

🧹 **Linting**

 make lint


🔧 **Features**

 🔍 Filter movies by actor, director, genre (backend-based filtering)
 
 📜 View full profiles of movies, actors, and directors
 
 🧾 Auto-documented REST API with Swagger



✅ **Requirements**

 Node.js & Python (for local dev without containers)


✍️ **API Documentation**

Available at: http://localhost:5000/apidocs

Defined using OpenAPI 3.0 (Swagger)
