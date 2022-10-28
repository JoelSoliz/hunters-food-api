from sqlalchemy import Column, String, DateTime, FLOAT, ForeignKey, LargeBinary, Integer

from data import Base


class Product(Base):
    __tablename__ = 'product'
    id_product = Column(String(4), primary_key=True)
    id_business = Column(String(4), ForeignKey('business.id_business'))
    name = Column(String(100), nullable=False)
    price = Column(FLOAT(10.2), nullable=False)
    product_type = Column(String(100), nullable=False)
    image = Column(LargeBinary((2**32)-1), nullable=False)
    discount = Column(FLOAT(10.2), default=0)
    amount = Column(Integer(), default=0)
    start_time = Column(DateTime(), nullable=False)
    final_time = Column(DateTime(), nullable=False)
    description = Column(String(256), nullable=False)

    def __str__(self):
        return self.name_product
