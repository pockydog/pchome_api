from models.models import Product
from sqlalchemy import or_


class ProductHandlers:

    @classmethod
    def get_product_info(cls, page, per_page, keyword=None):
        conditions = list()
        if keyword:
            conditions.append(
                or_(
                    Product.name.like(f'%{keyword}%'),
                    Product.type.like(f'%{keyword}%'),
                )
            )
        product = Product.query.filter(*conditions).paginate(page=page, per_page=per_page, error_out=False)
        pager = {
            'page': product.page,
            'per_page': product.per_page,
            'total': product.total,
        }
        products = product.items
        results = list()
        for product_ in products:
            result = {
                'id': product_.id,
                'name': product_.name,
                'price': product_.price,
                'code': product_.code,
                'pic_url': product_.pic_url,
                'type': product_.type,
                'create_datetime': product_.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                'update_datetime': product_.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            }
            results.append(result)
        return results, pager
