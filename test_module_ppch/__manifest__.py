{
    'name': "Rental Deposit",
    'version': '1.0',
    'depends': ['website_sale_renting'],
    'author': "ppch",
    'category': 'Category',
    'description': """
    Rental Deposit is configured and it will be added as deposit product whenever any product
    which has deposit required will be true and it will work in both frontend and backend
    """,
    'license': "LGPL-3",
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
}