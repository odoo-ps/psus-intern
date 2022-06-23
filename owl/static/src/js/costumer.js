odoo.define("odoo_framework", function(require) {
    "use strict";

    var models = require("point_of_sale.models");
    models.load_fields("res.partner", "costumer_type");
})
