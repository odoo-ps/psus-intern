/** @odoo-module */

import fieldRegistryOwl from "web.field_registry_owl";
import fieldRegistry from "web.field_registry";
import AbstractField from "web.AbstractFieldOwl";
import { ComponentAdapter } from "web.OwlCompatibility";

class Preview extends AbstractField {
  static template = "Preview";
  static supportedFieldTypes = ["char"];
  static components = { ComponentAdapter };

  setup() {
    const widgetName = this.props.record.data.name;
    this.props.record.data[this.value] = this.props.record.data[this.value] ?? {
      data: [],
    };
    if (fieldRegistry.contains(widgetName)) {
      this.component = fieldRegistry.get(widgetName);
      this.legacy = true;
      if (this.component.prototype.specialData) {
        this.props.record.specialData = {
          [this.value]: [],
        };
        console.warn(`Special data for ${widgetName} is not supported`);
      }
    } else if (fieldRegistryOwl.contains(widgetName)) {
      this.component = fieldRegistryOwl.get(widgetName);
      this.legacy = false;
    } else {
      console.warn(`No widget found for ${widgetName}`);
    }
    this.widgetArgs = [this.value, this.props.record, this.props.options];
  }
}

fieldRegistryOwl.add("preview", Preview);

export default Preview;
