from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import orm
from .database import Base


class api_items(Base):
    __tablename__ = "Items"
    id = Column(Integer,primary_key=True,index=True)
    ProductCode = Column(String)
    ProductName = Column(String)
    ModelType = Column(String)
    BrandName = Column(String)



class api_case(Base):
    __tablename__ = "CaseTable"
    id = Column(Integer,primary_key=True,index=True)
    TrDate = Column(String)
    CustomerID = Column(Integer)
    ProductID = Column(Integer)
    ProDes = Column(String)
    CaseStatus = Column(String)
    SerialNo = Column(String)
    WarrentyType = Column(String)


class api_customer(Base):
    __tablename__ = "Customer"
    id = Column(Integer,primary_key=True,index=True)
    CustomerCode = Column(Integer)
    CustomerName = Column(String)
    CusAddress = Column(String)
    CusMobile = Column(String)



class api_orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer,primary_key=True,index=True)
    FirstName = Column(String)
    LastName = Column(String)
    MobileNo = Column(String)
    Address = Column(String)
    OrderNotes = Column(String)
    Status = Column(String)


class api_contact(Base):
    __tablename__ = "Contact"
    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String)
    Mobile = Column(String)
    Email = Column(String)
    Message = Column(String)



###########################################################################################
###########################################################################################
###########################################################################################


class api_ricketts(Base):
    __tablename__ = "Ricketts"
    id = Column(Integer,primary_key=True,index=True)
    Weather = Column(String)
    Location = Column(String)
    Env = Column(String)
    Alerts = Column(String)
    Transport = Column(String)
    Groups = Column(String)


class api_hickory(Base):
    __tablename__ = "Hickory"
    id = Column(Integer,primary_key=True,index=True)
    Weather = Column(String)
    Location = Column(String)
    Env = Column(String)
    Alerts = Column(String)
    Transport = Column(String)
    Groups = Column(String)


class api_ohiopyle(Base):
    __tablename__ = "Ohiopyle"
    id = Column(Integer,primary_key=True,index=True)
    Weather = Column(String)
    Location = Column(String)
    Env = Column(String)
    Alerts = Column(String)
    Transport = Column(String)
    Groups = Column(String)


class api_worldsEnd(Base):
    __tablename__ = "WorldsEnd"
    id = Column(Integer,primary_key=True,index=True)
    Weather = Column(String)
    Location = Column(String)
    Env = Column(String)
    Alerts = Column(String)
    Transport = Column(String)
    Groups = Column(String)


class api_appalachian(Base):
    __tablename__ = "Appalachian"
    id = Column(Integer,primary_key=True,index=True)
    Weather = Column(String)
    Location = Column(String)
    Env = Column(String)
    Alerts = Column(String)
    Transport = Column(String)
    Groups = Column(String)


class api_messages(Base):
    __tablename__ = "Messages"
    id = Column(Integer,primary_key=True,index=True)
    Messages = Column(String)


class api_messagesHickory(Base):
    __tablename__ = "MessagesHickory"
    id = Column(Integer,primary_key=True,index=True)
    Messages = Column(String)


class api_messagesOhiopyle(Base):
    __tablename__ = "MessagesOhiopyle"
    id = Column(Integer,primary_key=True,index=True)
    Messages = Column(String)


class api_messagesWorldsEnd(Base):
    __tablename__ = "MessagesWorldsEnd"
    id = Column(Integer,primary_key=True,index=True)
    Messages = Column(String)


class api_messagesAppalachian(Base):
    __tablename__ = "MessagesAppalanchian"
    id = Column(Integer,primary_key=True,index=True)
    Messages = Column(String)