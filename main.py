from fastapi import FastAPI

# Create a fastapi object
app = FastAPI()


# Create an endpoint (route)
@app.get("/")
async def root():
    return {"message": "Hello World, I AM ALIVE!"}


# Another endpoint with parameter
@app.get("/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}
    # f"Hello, {name}!" is equivalent to:
    #   1 - "Hello, " + name + "!" 
    #   2 - "Hello, {}!".format(name) 
    #   3 - ("Hello, ", name, "!")
