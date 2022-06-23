odoo.define('owl_framework', function (require) {
    "use strict";
    
    var models = require('point_of_sale.models');

    models.load_fields('res.partner','customer_type');

});
