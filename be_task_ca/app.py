from fastapi import FastAPI

from be_task_ca.item.delivery.api.v1.item_router import item_router
from be_task_ca.user.delivery.api.v1.user_router import user_router


app = FastAPI()
app.include_router(user_router)
app.include_router(item_router)


@app.get("/")
async def root():
    return {
        "message": "Thanks for shopping at Nile!"
    }  # the Nile is 250km longer than the Amazon
