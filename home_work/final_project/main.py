from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    order_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)
    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    orders = relationship("Order", back_populates="product")


class UserCreate(BaseModel):
    first_name: str = Field(..., title='First name', max_length=50)
    last_name: str = Field(..., title='Last name', max_length=50)
    email: str = Field(..., title='Email', max_length=500)
    password: str = Field(..., title='Password', max_length=50)


class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, title='First name', max_length=50)
    last_name: Optional[str] = Field(None, title='Last name', max_length=50)
    email: Optional[str] = Field(None, title='Email', max_length=500)
    password: Optional[str] = Field(None, title='Password', max_length=50)


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class OrderCreate(BaseModel):
    user_id: int = Field(0, title='User ID')
    product_id: int = Field(0, title='Product ID')
    status: str = Field(..., title='Status')


class OrderUpdate(BaseModel):
    user_id: Optional[int] = Field(None, title='User ID')
    product_id: Optional[int] = Field(None, title='Product ID')
    status: Optional[str] = Field(None, title='Status')


class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: datetime
    status: str


class ProductCreate(BaseModel):
    name: str = Field(..., title='Name', max_length=50)
    description: str = Field(..., title='Description', max_length=500)
    price: int = Field(0, title='Price',ge=0,le=10000)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[int] = Field(0, title='Price',ge=0,le=10000)


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: int

app = FastAPI()

# Создаем подключение к базе данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./store.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Получение пользователя по id
@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


# Создание нового пользователя
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Обновление пользователя по id
@app.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    for field, value in user.dict(exclude_unset=True).items():
        setattr(existing_user, field, value)
    db.commit()
    db.refresh(existing_user)
    return existing_user


# Удаление пользователя по id
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}


# Получение заказа по id
@app.get("/orders/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order


# Создание нового заказа
@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


# Обновление заказа по id
@app.put("/orders/{order_id}", response_model=OrderOut)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    existing_order = db.query(Order).filter(Order.id == order_id).first()
    if not existing_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    for field, value in order.dict(exclude_unset=True).items():
        setattr(existing_order, field, value)
    db.commit()
    db.refresh(existing_order)
    return existing_order


# Удаление заказа по id
@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted"}


# Получение товара по id
@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


# Создание нового товара
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# Обновление товара по id
@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    for field, value in product.dict(exclude_unset=True).items():
        setattr(existing_product, field, value)
    db.commit()
    db.refresh(existing_product)
    return existing_product


# Удаление товара по id
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}
