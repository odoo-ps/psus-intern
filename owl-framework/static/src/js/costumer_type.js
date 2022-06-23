odoo.define("pos_costumer_type.pos_costumer_type", require => {
  "use strict";
  var models = require("point_of_sale.models");
  models.load_fields("res.partner","costumer_type");
});
