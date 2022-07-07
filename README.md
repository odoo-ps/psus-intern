# Odoo 15 Custom Modules

## Compatibility Filter

Filters items that are compatible with the product the
customer is buying parts for.

Task ID: 2869113

### TODO:
- MAIN: user input > returns list
    - wizard.action_search()
        - reachable
        - edit behavior to filter out components
    - component.action_search_show_wizard()
        - reachable?
        - edit lines part
- edit security + rules
- menu hierarchy + specifications
    - wizard (root)
        - no creation on forms/list
    - all parts (secondary)
        - creation of new part here only
        - parts by (sub)
            - no creation on forms/list
- make sure manifest is correct