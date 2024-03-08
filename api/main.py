from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .import schemas
from .import models
from .database import engine, SessionLocal
from fastapi.params import Depends
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(engine)
def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

@app.get('/ListOfItems')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_items).all()
    return ListOfItems


@app.post('/AddItem')
def product(header:schemas.api_items,db:Session=Depends(get_db)):
    new_item = models.api_items(ProductCode=header.ProductCode, ProductName=header.ProductName, ModelType=header.ModelType, BrandName=header.BrandName)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.put('/UpdateItem/{id}')
def UpdateItem(id,Pro:schemas.api_items,db:Session=Depends(get_db)):
    Item = db.query(models.api_items).filter(models.api_items.id==id)
    Item.update(Pro.dict())
    db.commit()
    return Pro


@app.delete('/DeleteItem/{id}')
def DeleteItem(id,db:Session=Depends(get_db)):
    items = db.query(models.api_items).filter(models.api_items.id==id).delete(synchronize_session=False)
    db.commit()
    return "Success"




@app.get('/ListOfCase')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_case).all()
    return ListOfItems


@app.post('/AddCase')
def NewCase(header:schemas.api_case,db:Session=Depends(get_db)):
    new_case = models.api_case(TrDate=header.TrDate, CustomerID=header.CustomerID, ProductID=header.ProductID, ProDes=header.ProDes, CaseStatus=header.CaseStatus, SerialNo=header.SerialNo, WarrentyType=header.WarrentyType)
    db.add(new_case)
    db.commit()
    db.refresh(new_case)
    return header


@app.put('/UpdateCase/{id}')
def UpdateItem(id,Pro:schemas.api_case,db:Session=Depends(get_db)):
    Item = db.query(models.api_case).filter(models.api_case.id==id)
    Item.update(Pro.dict())
    db.commit()
    return Pro


@app.delete('/DeleteCase/{id}')
def DeleteItem(id,db:Session=Depends(get_db)):
    items = db.query(models.api_case).filter(models.api_case.id==id).delete(synchronize_session=False)
    db.commit()
    return "Success"





@app.get('/ListOfCustomer')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_customer).all()
    return ListOfItems


@app.post('/AddCustomer')
def product(header:schemas.api_customer,db:Session=Depends(get_db)):
    new_cus = models.api_customer(CustomerCode=header.CustomerCode, CustomerName=header.CustomerName, CusAddress=header.CusAddress, CusMobile=header.CusMobile)
    db.add(new_cus)
    db.commit()
    db.refresh(new_cus)
    return header


@app.put('/UpdateCustomer/{id}')
def UpdateItem(id,Pro:schemas.api_customer,db:Session=Depends(get_db)):
    Cus = db.query(models.api_customer).filter(models.api_customer.id==id)
    Cus.update(Pro.dict())
    db.commit()
    return Pro


@app.delete('/DeleteCustomer/{id}')
def DeleteItem(id,db:Session=Depends(get_db)):
    Custom = db.query(models.api_customer).filter(models.api_customer.id==id).delete(synchronize_session=False)
    db.commit()
    return "Success"



################################################################################################################################################################################################################################
################################################################################################################################################################################################################################


@app.get('/ListOfOrders')
def itemlist(db:Session=Depends(get_db)):
    ListOfOrders = db.query(models.api_orders).all()
    return ListOfOrders


@app.post('/AddOrders')
def product(header:schemas.api_orders,db:Session=Depends(get_db)):
    new_item = models.api_orders(FirstName = header.FirstName, LastName = header.LastName, MobileNo = header.MobileNo, Address = header.Address, OrderNotes = header.OrderNotes, Status = header.Status)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.put('/UpdateOrder/{id}')
def UpdateItem(id,Pro:schemas.api_orders,db:Session=Depends(get_db)):
    Cus = db.query(models.api_orders).filter(models.api_orders.id==id)
    Cus.update(Pro.dict())
    db.commit()
    return Pro


@app.delete('/DeleteOrder/{id}')
def DeleteItem(id,db:Session=Depends(get_db)):
    Custom = db.query(models.api_orders).filter(models.api_orders.id==id).delete(synchronize_session=False)
    db.commit()
    return "Success"


################################################################################################################################################################################################################################
################################################################################################################################################################################################################################



@app.post('/AddContact')
def product(header:schemas.api_contact,db:Session=Depends(get_db)):
    new_contact = models.api_contact(Name = header.Name, Mobile = header.Mobile, Email = header.Email, Message = header.Message)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return header


################################################################################################################################################################################################################################
################################################################################################################################################################################################################################


@app.get('/RickettsGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_ricketts).all()
    return ListOfItems


@app.post('/RickettsPost')
def product(header:schemas.api_ricketts,db:Session=Depends(get_db)):
    new_item = models.api_ricketts(Weather = header.Weather, Location = header.Location, Env = header.Env, Alerts = header.Alerts, Transport = header.Transport, Groups = header.Groups)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.put('/RickettsUpdate/{id}')
def UpdateItem(id,Pro:schemas.api_ricketts,db:Session=Depends(get_db)):
    Item = db.query(models.api_ricketts).filter(models.api_ricketts.id==id)
    Item.update(Pro.dict())
    db.commit()
    return Pro


@app.get('/HickoryGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_hickory).all()
    return ListOfItems


@app.post('/HickoryPost')
def product(header:schemas.api_hickory,db:Session=Depends(get_db)):
    new_item = models.api_hickory(Weather = header.Weather, Location = header.Location, Env = header.Env, Alerts = header.Alerts, Transport = header.Transport, Groups = header.Groups)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.put('/HickoryUpdate/{id}')
def UpdateItem(id,Pro:schemas.api_hickory,db:Session=Depends(get_db)):
    Item = db.query(models.api_hickory).filter(models.api_hickory.id==id)
    Item.update(Pro.dict())
    db.commit()
    return Pro


@app.get('/OhiopyleGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_ohiopyle).all()
    return ListOfItems


@app.post('/OhiopylePost')
def product(header:schemas.api_ohiopyle,db:Session=Depends(get_db)):
    new_item = models.api_ohiopyle(Weather = header.Weather, Location = header.Location, Env = header.Env, Alerts = header.Alerts, Transport = header.Transport, Groups = header.Groups)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.put('/OhiopyleUpdate/{id}')
def UpdateItem(id,Pro:schemas.api_ohiopyle,db:Session=Depends(get_db)):
    Item = db.query(models.api_ohiopyle).filter(models.api_ohiopyle.id==id)
    Item.update(Pro.dict())
    db.commit()
    return Pro


@app.get('/WorldsEndGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_worldsEnd).all()
    return ListOfItems


@app.post('/WorldsEndPost')
def product(header:schemas.api_worldsEnd,db:Session=Depends(get_db)):
    new_item = models.api_worldsEnd(Weather = header.Weather, Location = header.Location, Env = header.Env, Alerts = header.Alerts, Transport = header.Transport, Groups = header.Groups)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.put('/WorldsEndUpdate/{id}')
def UpdateItem(id,Pro:schemas.api_worldsEnd,db:Session=Depends(get_db)):
    Item = db.query(models.api_worldsEnd).filter(models.api_worldsEnd.id==id)
    Item.update(Pro.dict())
    db.commit()
    return Pro


@app.get('/AppalachianGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_appalachian).all()
    return ListOfItems


@app.post('/AppalachianPost')
def product(header:schemas.api_appalachian,db:Session=Depends(get_db)):
    new_item = models.api_appalachian(Weather = header.Weather, Location = header.Location, Env = header.Env, Alerts = header.Alerts, Transport = header.Transport, Groups = header.Groups)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.put('/AppalachianUpdate/{id}')
def UpdateItem(id,Pro:schemas.api_appalachian,db:Session=Depends(get_db)):
    Item = db.query(models.api_appalachian).filter(models.api_appalachian.id==id)
    Item.update(Pro.dict())
    db.commit()
    return Pro


@app.get('/MessageGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_messages).all()
    return ListOfItems


@app.post('/MessagePost')
def product(header:schemas.api_messages,db:Session=Depends(get_db)):
    new_item = models.api_messages(Messages = header.Messages)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.get('/HickoryMessageGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_messagesHickory).all()
    return ListOfItems


@app.post('/HickoryMessagePost')
def product(header:schemas.api_messagesHickory,db:Session=Depends(get_db)):
    new_item = models.api_messagesHickory(Messages = header.Messages)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.get('/OhiopyleMessageGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_messagesOhiopyle).all()
    return ListOfItems


@app.post('/OhiopyleMessagePost')
def product(header:schemas.api_messagesOhiopyle,db:Session=Depends(get_db)):
    new_item = models.api_messagesOhiopyle(Messages = header.Messages)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.get('/WorldsEndMessageGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_messagesWorldsEnd).all()
    return ListOfItems


@app.post('/WorldsEndMessagePost')
def product(header:schemas.api_messagesWorldsEnd,db:Session=Depends(get_db)):
    new_item = models.api_messagesWorldsEnd(Messages = header.Messages)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header


@app.get('/AppalachianMessageGet')
def itemlist(db:Session=Depends(get_db)):
    ListOfItems = db.query(models.api_messagesAppalachian).all()
    return ListOfItems


@app.post('/AppalachianMessagePost')
def product(header:schemas.api_messagesAppalachian,db:Session=Depends(get_db)):
    new_item = models.api_messagesAppalachian(Messages = header.Messages)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return header

