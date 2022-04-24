from fastapi import APIRouter
import os
from api.routes import translate

router = APIRouter()

deploy_type = os.environ.get("DEPLOY_TYPE")
translate_router = translate.create_translator_router(deploy_type)
router.include_router(translate_router, tags=["translate-chinese"])
