from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


# data = {
#     "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
#     "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
# }


# class OwnerError(Exception):
#     pass


# def get_username():
#     try:
#         yield "Rick"
#     except OwnerError as e:
#         raise HTTPException(status_code=400, detail=f"Owner error: {e}")


# @app.get("/items/{item_id}")
# def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
#     if item_id not in data:
#         raise HTTPException(status_code=404, detail="Item not found")
#     item = data[item_id]
#     if item["owner"] != username:
#         raise OwnerError(username)
    # return item 
    

class InternalError(Exception):
    pass


def get_username():
    try:
        yield "Morty"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise
        


@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id