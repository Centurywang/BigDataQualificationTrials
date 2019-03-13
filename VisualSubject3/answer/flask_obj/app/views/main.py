import json
from flask import Blueprint, render_template,jsonify
from app.models import Tbl_Sales_Rom_Count,Tbl_Sales_Ram_Count,Tbl_Sales_Os_Count,Tbl_Sales_Cpu_Count
from app.extensions import db
from sqlalchemy import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('/main/index.html')

@main.route('/index/')
def display():
    tscc_res = get_sales_cpu_count()
    tsrac_res = get_sales_ram_count()
    tsroc_res = get_sales_rom_count()
    tsoc_res = get_sales_os_count()
    return render_template('/main/index.html',tscc_res=tscc_res,tsrac_res=tsrac_res,tsroc_res=tsroc_res,tsoc_res=tsoc_res)

#查询Tbl_Sales_Cpu_Count类中所有数据，按fld_sale_count字段排列
def get_sales_cpu_count():
    tscc_res = Tbl_Sales_Cpu_Count.query.order_by(asc('fld_sale_count')).all()
    return tscc_res

#查询Tbl_Sales_Ram_Count类中所有数据，按fld_sale_count字段排列
def get_sales_ram_count():
    tsrac_res = Tbl_Sales_Ram_Count.query.order_by(asc('fld_sale_count')).all()
    return tsrac_res

#查询Tbl_Sales_Rom_Count类中所有数据，按fld_sale_count字段排列
def get_sales_rom_count():
    tsroc_res = Tbl_Sales_Rom_Count.query.order_by(asc('fld_sale_count')).all()
    return tsroc_res

#查询Tbl_Sales_Os_Count类中所有数据，按fld_sale_count字段排列
def get_sales_os_count():
    tsoc_res = Tbl_Sales_Os_Count.query.order_by(desc('fld_sale_count')).all()
    return tsoc_res



