odoo.define("owl_framework_pos_changes.models", function (require) {
  "use strict";

  var module = require("point_of_sale.models");
  var models = module.PosModel.prototype.models;
  var partner = models.find((x) => x.model === "res.partner");
  partner.fields.push("customer_type");
});
