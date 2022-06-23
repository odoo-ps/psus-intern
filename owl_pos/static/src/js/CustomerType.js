odoo.define('pos_add_field.pos_add_field', function (require) {
    "use strict";
    
    var models = require('point_of_sale.models');
    
    models.load_fields('res.partner','customer_type');
    
    });
    