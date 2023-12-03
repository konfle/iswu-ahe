from fastapi import FastAPI, HTTPException

import inference
import db

app = FastAPI()

@app.get("/get_user_input")
def get_user_input(app_type: str, performance: bool):
    #rules_from_db = get_rules_from_database()  # another endpoint?
    user_input = {"app_type": app_type, "performance": performance}
    language = inference.infer(user_input, db.knowledge_base)
    if language:
        return {"decision": language}
    else:
        raise HTTPException(status_code=400, detail="Sorry, something went wrong.")
