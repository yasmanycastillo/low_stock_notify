{
    'name' : 'Low Stock Notify',
    'version' : '1.0',
    'author' : 'Mbs Standoffs, Travis Waelbroeck',
    'summary' : '',
    'description' : '',
    'category' : 'Sales Management',
    'depends' : ['base', 'product', 'mage2odoo'],
    'data':[
    			'data/email_template.xml',
                'views/product_template.xml',
                'views/ir_cron.xml'
    		],
    'installable': True
}
