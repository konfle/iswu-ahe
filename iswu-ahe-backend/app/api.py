from fastapi import FastAPI, HTTPException, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware

#import app.inference as ai
#import app.db as ad

from inference import infer
from models import UserInput
from db import get_rules_from_database

app = FastAPI(title="Application System for Selection of Optimal Programming Language",
              description="An inference system that, using prior information about the IT project and the user's "
                          "goals, helps select the most appropriate programming language for the task at hand.",
              contact={"name": "konfle", "url": "https://github.com/konfle"})
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @router.get(path="/user_input", tags=["Collection of User Data"])
# def get_user_input(app_type: str, performance: bool):
#     rules_from_db = ad.get_rules_from_database()
#     user_input = {"app_type": app_type, "performance": performance}
#     language = ai.infer(user_input, rules_from_db)
#     if language:
#         return {"decision": language}
#     else:
#         raise HTTPException(status_code=400, detail="Sorry, something went wrong.")


@router.post(path="/user_input", response_model=dict, tags=["Collection of User Data"])
def get_user_input(user_input: UserInput, rules_from_db=Depends(get_rules_from_database)):
    language = infer(user_input.dict(), rules_from_db)
    if language:
        return {"decision": language}
    else:
        raise HTTPException(status_code=400, detail="Sorry, something went wrong.")


app.include_router(router)
