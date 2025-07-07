🎬 **Movie Explorer Website**

A full-stack web application for browsing, filtering, and viewing movies, actors, and directors with detailed profiles.

------------------
🛠 **Tech Stack**

Frontend  -->   React (Vite), Bootstrap

Backend   -->   Python Flask (REST API)

Database  -->   MongoDB

API Docs  -->   Swagger / OpenAPI

------------------
 🚀**Getting Started**

1. Clone the Repository

	 git clone https://github.com/yourusername/movie-explorer.git
	 cd movie_explorer

2. Run with Docker (Recommended)

	 make build    
	 make up
	        
------------------

⚙️ **Makefile Commands**

		make build      # Build all containers
		make up         # Start backend, frontend, and MongoDB
		make down       # Stop all services
		make test       # Run both frontend and backend tests
		make lint       # Run ESLint + Flake8

------------------
**Access the app:**

 **Frontend**: http://localhost:3000
 
 **Backend API**: http://localhost:5000
 
 **Swagger Docs**: http://localhost:5000/apidocs

🧪 **Testing**

 Run All Tests

  make test

Backend Tests

  cd backend
  pytest
 
 
Frontend Tests

  cd frontend
  npm install
  npm test

🧹 **Linting**

 make lint


🔧 **Features**

 🔍 Filter movies by actor, director, genre 
 
 📜 View full profiles of movies, actors, and directors
 
 🧾 Auto-documented REST API with Swagger



✍️ **API Documentation**

Available at: http://localhost:5000/apidocs

Defined using OpenAPI 3.0 (Swagger)
