from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

names = ["Mahneera", "Mindi", "Minhera"]

@app.get("/")  # path operation decorator => url

def get_function(): #jb Url call hoga tb ye function call hoga
    return names # ye func ek JSON response dega

# .............................................................................

class Data(BaseModel):
    name: str 

#  create krna
@app.post("/")
def post_function(data : Data): 
    names.append(data.name)
    return names # ye func ek JSON response dega


# .............................................................................

@app.delete("/{name}") # url
def delete_data(name: str): 
    names.remove(name) # ye name ko remove kr dega
    return names


# .............................................................................
@app.put("/{name}")
def update_data(name: str, data: Data):
    for i, n in enumerate(names):
        if n == name:
            names[i] = data.name
    return names
# .............................................................................
    



