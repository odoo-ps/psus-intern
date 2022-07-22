odoo.define('survey.form_inherit', function (require) {
    'use strict';
    
    var SurveyFormWidget = require('survey.form');
    
    SurveyFormWidget.include({
        events: {
            'change .o_survey_form_choice_item': '_onChangeChoiceItem',
            'click .o_survey_matrix_btn': '_onMatrixBtnClick',
            'click button[type="submit"]': '_onSubmit',
            'click button[type="test"]': '_onTest',
        },
        
        _onTest: function (event) {
            event.preventDefault();
            var options = {};
            options.isTest = true;
            this._submitForm(options);
        },

        // SUBMIT
        // -------------------------------------------------------------------------

        /**
        * This function will send a json rpc call to the server to
        * - start the survey (if we are on start screen)
        * - submit the answers of the current page
        * Before submitting the answers, they are first validated to avoid latency from the server
        * and allow a fade out/fade in transition of the next question.
        *
        * @param {Array} [options]
        * @param {Integer} [options.previousPageId] navigates to page id
        * @param {Boolean} [options.skipValidation] skips JS validation
        * @param {Boolean} [options.initTime] will force the re-init of the timer after next
        *   screen transition
        * @param {Boolean} [options.isFinish] fades out breadcrumb and timer
        * @param {Boolean} [options.isTest] used to Test the input code
        * @private
        */
        _submitForm: function (options) {
            var self = this;
            var params = {};

            if (options.isTest){
                params.isTest = options.isTest;
            }

            if (options.previousPageId) {
                params.previous_page_id = options.previousPageId;
            }
            var route = "/survey/submit";

            if (this.options.isStartScreen) {
                route = "/survey/begin";
                // Hide survey title in 'page_per_question' layout: it takes too much space
                if (this.options.questionsLayout === 'page_per_question') {
                    this.$('.o_survey_main_title').fadeOut(400);
                }
            } else {
                var $form = this.$('form');
                var formData = new FormData($form[0]);

                if (!options.skipValidation) {
                    // Validation pre submit
                    if (!this._validateForm($form, formData)) {
                        return;
                    }
                }

                this._prepareSubmitValues(formData, params);
            }

            // prevent user from submitting more times using enter key
            this.preventEnterSubmit = true;

            if (this.options.sessionInProgress) {
                // reset the fadeInOutDelay when attendee is submitting form
                this.fadeInOutDelay = 400;
                // prevent user from clicking on matrix options when form is submitted
                this.readonly = true;
            }

            var submitPromise = self._rpc({
                route: _.str.sprintf('%s/%s/%s', route, self.options.surveyToken, self.options.answerToken),
                params: params,
            });
            this._nextScreen(submitPromise, options);
            },
          
        // PREPARE SUBMIT TOOLS
        // -------------------------------------------------------------------------
        /**
        * For each type of question, extract the answer from inputs or textarea (comment or answer)
        *
        *
        * @private
        * @param {Event} event
        */
        _prepareSubmitValues: function (formData, params) {
            var self = this;
            formData.forEach(function (value, key) {
                switch (key) {
                    case 'isTest':
                    case 'csrf_token':
                    case 'token':
                    case 'page_id':
                    case 'question_id':
                        params[key] = value;
                        break;
                }
            });
    
            // Get all question answers by question type
            this.$('[data-question-type]').each(function () {
                switch ($(this).data('questionType')) {
                    case 'text_box':
                    case 'char_box':
                    case 'code_box':
                    case 'numerical_box':
                        params[this.name] = this.value;
                        break;
                    case 'date':
                        params = self._prepareSubmitDates(params, this.name, this.value, false);
                        break;
                    case 'datetime':
                        params = self._prepareSubmitDates(params, this.name, this.value, true);
                        break;
                    case 'simple_choice_radio':
                    case 'multiple_choice':
                        params = self._prepareSubmitChoices(params, $(this), $(this).data('name'));
                        break;
                    case 'matrix':
                        params = self._prepareSubmitAnswersMatrix(params, $(this));
                        break;
                }
            });
        },

        /**
         * Handle server side validation and display eventual error messages.
        *
        * @param {string} result the HTML result of the screen to display
        * @param {Object} options see '_submitForm' for details
        */
        _onNextScreenDone: function (result, options) {
        var self = this;

        if (!(options && options.isFinish)
            && !this.options.sessionInProgress) {
            this.preventEnterSubmit = false;
        }

        if (result && !result.error) {
            this.$(".o_survey_form_content").empty();
            this.$(".o_survey_form_content").html(result.survey_content);

            if (result.survey_progress && this.$surveyProgress.length !== 0) {
                this.$surveyProgress.html(result.survey_progress);
            } else if (options.isFinish && this.$surveyProgress.length !== 0) {
                this.$surveyProgress.remove();
            }

            if (result.survey_navigation && this.$surveyNavigation.length !== 0) {
                this.$surveyNavigation.html(result.survey_navigation);
                this.$surveyNavigation.find('.o_survey_navigation_submit').on('click', self._onSubmit.bind(self));
            }

            // Hide timer if end screen (if page_per_question in case of conditional questions)
            if (self.options.questionsLayout === 'page_per_question' && this.$('.o_survey_finished').length > 0) {
                options.isFinish = true;
            }

            this.$('div.o_survey_form_date').each(function () {
                self._initDateTimePicker($(this));
            });
            if (this.options.isStartScreen || (options && options.initTimer)) {
                this._initTimer();
                this.options.isStartScreen = false;
            } else {
                if (this.options.sessionInProgress && this.surveyTimerWidget) {
                    this.surveyTimerWidget.destroy();
                }
            }
            if (options && options.isFinish) {
                this._initResultWidget();
                if (this.surveyBreadcrumbWidget) {
                    this.$('.o_survey_breadcrumb_container').addClass('d-none');
                    this.surveyBreadcrumbWidget.destroy();
                }
                if (this.surveyTimerWidget) {
                    this.surveyTimerWidget.destroy();
                }
            } else {
                this._updateBreadcrumb();
            }
            self._initChoiceItems();
            self._initTextArea();

            if (this.options.sessionInProgress && this.$('.o_survey_form_content_data').data('isPageDescription')) {
                // prevent enter submit if we're on a page description (there is nothing to submit)
                this.preventEnterSubmit = true;
            }

            this.$('.o_survey_form_content').fadeIn(this.fadeInOutDelay);
            $("html, body").animate({ scrollTop: 0 }, this.fadeInOutDelay);
            self._focusOnFirstInput();
        }
        else if (result && result.fields && result.error === 'validation') {
            this.$('.o_survey_form_content').fadeIn(0);
            if (options.isTest){
                this.$('.o_survey_question_success').removeClass("slide_in")
            }
            this._showErrors(result.fields);
        } else {
            var $errorTarget = this.$('.o_survey_error');
            $errorTarget.removeClass("d-none");
            this._scrollToError($errorTarget);
        }
    },

    }); 
});
    