from fastapi import FastAPI #Imports the FastAPI class.

app = FastAPI() #Creates your API application.


# You've now built and practiced:
# - Root endpoint: /
# - Dynamic path parameter: /hello/{name}
# - Optional query parameter: /search
# - Integer query parameter and calculation: /square

@app.get("/") #Registers a route that responds to HTTP GET requests at /.
def read_root(): #Defines the function FastAPI calls for that route.
    return {"message": "My first FastAPI application is running!"} # Returns a Python dictionary that FastAPI converts to JSON.

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/search")
def search(name: str | None = None):
    if name:
        return {"message": f"You searched for {name}"}
    else:
        return {"message": "You didn't enter a name"}

@app.get("/square")
def number_square(number: int):
    num_sqr = number * number
    return {
        "number": number,
        "square": num_sqr
    }