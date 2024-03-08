from pydantic import BaseModel


class api_items(BaseModel):
    ProductCode:str
    ProductName:str
    ModelType:str
    BrandName:str

class api_case(BaseModel):
    TrDate:str
    CustomerID:int
    ProductID:int
    ProDes:str
    CaseStatus:str
    SerialNo:str
    WarrentyType:str


class api_customer(BaseModel):
    CustomerCode:int
    CustomerName:str
    CusAddress:str
    CusMobile:str


class api_orders(BaseModel):
    FirstName:str
    LastName:str
    MobileNo:str
    Address:str
    OrderNotes:str
    Status:str

class api_contact(BaseModel):
    Name:str
    Mobile:str
    Email:str
    Message:str

###########################################################################################
###########################################################################################
###########################################################################################


class api_ricketts(BaseModel):
    Weather:str
    Location:str
    Env:str
    Alerts:str
    Transport:str
    Groups:str


class api_hickory(BaseModel):
    Weather:str
    Location:str
    Env:str
    Alerts:str
    Transport:str
    Groups:str


class api_ohiopyle(BaseModel):
    Weather:str
    Location:str
    Env:str
    Alerts:str
    Transport:str
    Groups:str


class api_worldsEnd(BaseModel):
    Weather:str
    Location:str
    Env:str
    Alerts:str
    Transport:str
    Groups:str


class api_appalachian(BaseModel):
    Weather:str
    Location:str
    Env:str
    Alerts:str
    Transport:str
    Groups:str

class api_messages(BaseModel):
    Messages:str


class api_messagesHickory(BaseModel):
    Messages:str


class api_messagesOhiopyle(BaseModel):
    Messages:str


class api_messagesWorldsEnd(BaseModel):
    Messages:str


class api_messagesAppalachian(BaseModel):
    Messages:str
    