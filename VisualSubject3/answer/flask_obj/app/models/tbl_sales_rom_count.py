from app.extensions import db

class Tbl_Sales_Rom_Count(db.Model):
    __tablename__ = 'tbl_sales_rom_count_pro'
    fld_index = db.Column(db.Integer,primary_key=True)
    fld_rom_name = db.Column(db.String(256),unique=True)
    fld_sale_count = db.Column(db.Integer,unique=True)