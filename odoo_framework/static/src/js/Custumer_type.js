odoo.define("odoo_framework.add_customer_type", function (require) {
  "use strict";

  var models = require("point_of_sale.models");

  models.load_fields("res.partner", "customer_type");
});
