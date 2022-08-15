from flask import jsonify, request

from app import app
from core.product_handlers import ProductHandlers


@app.route('/product', methods=['GET'])
@app.route('/product/<int:page>', methods=['GET'])
def get_product_info():
    keyword = request.args.get('keyword')
    page = request.args.get('page', 1, int)
    per_page = request.args.get('per_page', 10, int)
    result, pager = ProductHandlers.get_product_info(
        page=page,
        per_page=per_page,
        keyword=keyword,
    )
    return jsonify(result=result, pager=pager)
