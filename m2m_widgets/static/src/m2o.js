/** @odoo-module */

import fieldRegistry from 'web.field_registry';
import { FieldX2Many } from 'web.relational_fields';
import { _t } from 'web.core';
import ListRenderer from 'web.ListRenderer';

const xml = String.raw;

export const FieldMany2OneListRenderer = ListRenderer.extend({
    isStudioEditable: true,
    /**
     * @override
     */
    _renderRow(record) {
        const tr = this._super(record);
        return $(tr).prepend(
            xml`
                <td class="o_data_cell text-center">
                    <input type="radio"
                           name="${record._fieldName}"
                           value="${record.id}"
                           ${record.id == this.state.activeId && 'checked'} />
                </td>`
        )
    },
    /**
     * @override
     */
    _renderHeader() {
        const thead = this._super();
        $('tr', thead).prepend(
            xml`<th class="text-center">${_t('Select')}</th>`
        );
        return thead;
    },
    /**
     * @override
     * @param {Event} event 
     */
    _onRowClicked(event) {
        const radio = $(':radio', event.currentTarget)[0];
        radio.checked = true;
        this.state.activeId = radio.value;
        // Hack, passed the parent as the state since this.__parentedParent is not stable (?)
        this.state.widget.quickEdit({ id: radio.value })
    },
    /**
     * @override
     */
    async updateState() {
        // We don't want the default behavior of the ListRenderer here.
    }
})

export const FieldMany2OneList = FieldX2Many.extend({
    description: _t('Many2One List'),
    supportedFieldTypes: ['many2one'],
    /**
     * @override
     */
    init() {
        this._super(...arguments);
        this.view = this.view || this.attrs.views.list
        /**
         * A Many2One field only manages its own ID, but to be able to render to
         * a X2Many view, we need to create a record wrapper that mimics one
         * expected by X2Many.
         * 
         * TODO(vidi): Write a new model-agnostic X2Many component
         */
        this.value = {
            activeId: this.value && this.value.data.id,
            groupedBy: [],
            orderedBy: [],
            data: [], // populated by willStart
            widget: this,
            ...this.attrs.views.list,
        };
    },
    /**
     * @override
     */
    async willStart() {
        const { records } = await this._rpc({
            route: '/web/dataset/search_read',
            model: this.field.relation,
            limit: this.attrs.limit,
            domain: this.attrs.domain || []
        });
        for (const record of records) {
            // Hack: Stub only the methods/attributes needed to get things to work.
            record.evalModifiers = this.record.evalModifiers.bind(record);
            record.data = record;
            record._fieldName = this.field.name;
        }
        this.value.data = records;
    },
    /**
     * @override
     * @return {import('web.BasicRenderer') | undefined} BasicRenderer
     */
    _getRenderer() {
        if (this.view.arch.tag === 'tree') return FieldMany2OneListRenderer;
        return this._super();
    },
    /**
     * @override
     */
    commitChanges() {
        this._setValue(this.value.activeId);
    }
})

fieldRegistry.add('many2one_list', FieldMany2OneList);