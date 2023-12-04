from fastapi import FastAPI, HTTPException, APIRouter

import app.inference as ai
import app.db as ad

app = FastAPI(title="Application System for Selection of Optimal Programming Language",
              description="An inference system that, using prior information about the IT project and the user's "
                          "goals, helps select the most appropriate programming language for the task at hand.",
              contact={"name": "konfle", "url": "https://github.com/konfle"})
router = APIRouter()


@router.get(path="/user_input", tags=["Collection of User Data"])
def get_user_input(app_type: str, performance: bool):
    rules_from_db = ad.get_rules_from_database()
    user_input = {"app_type": app_type, "performance": performance}
    language = ai.infer(user_input, rules_from_db)
    if language:
        return {"decision": language}
    else:
        raise HTTPException(status_code=400, detail="Sorry, something went wrong.")


app.include_router(router)
