from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {
        "blog_name": "new blog"
    }}



@app.get("/blog/{id}")
def show_blog(id: int):
    """
    any /blog/String will be error from this point
    reading line by line
    """
    return {"data": {
        "id": id
    }}


dummy_comments = {
    1: "comment1", 2: "comment2", 3: "comment3",
}


@app.get("/blog/{id}/comment")
def show_blog(id: int):
    return {"data": {
        "comments": dummy_comments.get(id)
    }}
