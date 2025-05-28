from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from src.router import user, project, session_router
from src.router import report_router
from src.router import session
from src.router import upload

from src.database import connect_to_databse

app = FastAPI(lifespan=connect_to_databse)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Change this to the actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

# Include routers
app.include_router(user.router)
app.include_router(project.router)
app.include_router(session.router)
app.include_router(session_router.session_router)
app.include_router(report_router.router)
app.include_router(upload.router, prefix="/api", tags=["uploads"])



# Root endpoint
@app.get("/")
def read_root():
    return {"message": "API V1 running."}
