from os import name
from typing import *
from fastapi import APIRouter, Request
from pydantic.types import Json
from api import models
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
router = APIRouter()

templates = Jinja2Templates(directory="templates")

class Table(BaseModel):
    Name: str
    Group: str
    Salary: int
    UniqueID: str
    Description: str


@router.get("/show-all-data/")
def Show_All():
    data = list(models.EmployeeTable.objects.values('Name')) #Fetching Names from the table and showing the list of Employees
    return data

@router.get("/data/{param_id}")
def get_by_id(param_id):
    data = list(models.EmployeeTable.objects.filter(UniqueID = param_id)) #API routing with Django ORM
    return data

@router.post("/data/POST")
def create_item(item: Table):
    item = dict(item)
    m = models.EmployeeTable(**item)
    m.save()
    return {"Message":"The Data has been added to the Model"}

@router.delete("/data/{UniqID}")
def delete_item(UniqID: str):
        data = models.EmployeeTable.objects.filter(UniqueID = UniqID)
        return {"The following data will be deleted": list(data)}
        data.delete()

@router.put("/data/PUT/")
def put_item(Params: Table):
    item = dict(Params)
    m = models.EmployeeTable(**item)
    m.save()
    return {"Message":"The Data has been added to the Model"}

router2 = APIRouter()


@router2.get('/showall')
def show_all():
    data = list(models.EmployeeTable.objects.all().filter(Group = 'SDE1').values('Name')) #Filters the DB for SDE1 and shows their names
    return data


