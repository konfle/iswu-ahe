from fastapi import FastAPI, HTTPException

import app.inference as ai
import app.db as ad

app = FastAPI()

@app.get("/user_input")
def get_user_input(app_type: str, performance: bool):
    rules_from_db = ad.get_rules_from_database()
    user_input = {"app_type": app_type, "performance": performance}
    language = ai.infer(user_input, rules_from_db)
    if language:
        return {"decision": language}
    else:
        raise HTTPException(status_code=400, detail="Sorry, something went wrong.")
