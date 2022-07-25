odoo.define('survey.print_inherit', function (require) {
    'use strict';   
    
    var SurveyPrintWidget = require('survey.print');
    
    SurveyPrintWidget.include({

        //--------------------------------------------------------------------------
        // Widget
        //--------------------------------------------------------------------------
        /**
        * @override
        */
        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self._highlightTextArea();
            });
        },

        _highlightTextArea: function () {
            (async ({}) => {
                
                const {default: HighlightedCode} =
                    await import('https://unpkg.com/highlighted-code');
                
                HighlightedCode.useTheme('monokai-sublime');
                })(self);
        },
    
    });

});
