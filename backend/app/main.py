from fastapi import FastAPI;     #importing fast api into the project 

app = FastAPI()

#Checking fastAPI works 
@app.get("/health")
def health():
    return {"status" : "ok"}

