from fastapi import APIRouter
from app.api.v1 import auth, persons, officers, births, marriages, deaths, divorces, adoptions

api_router = APIRouter()
api_router.include_router(auth.router,      prefix="/auth",      tags=["Auth"])
api_router.include_router(persons.router,   prefix="/persons",   tags=["Persons"])
api_router.include_router(officers.router,  prefix="/officers",  tags=["Officers"])
api_router.include_router(births.router,    prefix="/births",    tags=["Births"])
api_router.include_router(marriages.router, prefix="/marriages", tags=["Marriages"])
api_router.include_router(deaths.router,    prefix="/deaths",    tags=["Deaths"])
api_router.include_router(divorces.router,  prefix="/divorces",  tags=["Divorces"])
api_router.include_router(adoptions.router, prefix="/adoptions", tags=["Adoptions"])