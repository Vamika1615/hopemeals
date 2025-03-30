from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS Middleware
from routes import donations, ngo, user, volunteer

app = FastAPI(title="AI-Powered Food Distribution System")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend domains if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers
)

# Register Routes
app.include_router(donations.router, prefix="/donations", tags=["Donations"])
app.include_router(ngo.router, prefix="/ngo", tags=["NGOs"])
app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(volunteer.router, prefix="/volunteer", tags=["Volunteers"])

@app.get("/")
async def root():
    return {"message": "Welcome to AI-Powered Food Distribution API"}
