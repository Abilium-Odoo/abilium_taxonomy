# -*- coding: utf-8 -*-
{
    'name': "Taxonomy",

    'summary': """
        
    """,

    'description': """
        
    """,

    'author': "Abilium GmbH",
    'website': "https://www.abilium.io",

    'category': 'Uncategorized',
    'version': '0.1',
    'application': False,

    'depends': [
        'base'
    ],

    'data': [
        'security/ir.model.access.csv',

        'views/taxonomy_tag.xml',

        'views/taxonomy_menus.xml',
    ]
}