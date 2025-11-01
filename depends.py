from fastapi import FastAPI, HTTPException
from typing import Annotated

app = FastAPI()

### First way to implement
class Logger:
    def log(self,message:str):
        print(f"Loggin message: {message}")

def get_logger():
    return Logger()

@app.get('/log/message')
def get_secure_data(log: Logger = Depends(get_logger)):
    log.log("testing...")
    return {"message":"Hello..."}

######## Other way
class AuthService:
    def authenticate(self, token:str):
        if token == "valid":
            return True
        else:
            raise HTTPException(status_code=401, detail="Unauthenticate")
            
def get_auth_service():
    return AuthService()

auth_service_dependencies = Annotated[AuthService, Depends(get_auth_service)]

@app.get('/auth')
def get_secure_data(token: str, auth_service: auth_service_dependencies):
    if auth_service.authenticate('valid'):
        return {"data":"Data is secure..."}
    
