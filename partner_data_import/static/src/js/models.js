odoo.define('partner_data_import.customer', function (require) {
    "use strict";
        var models = require('point_of_sale.models');
        models.load_fields('res.partner', ['badge']);
        var _super_posmodel = models.PosModel.prototype;
            models.PosModel = models.PosModel.extend({
                initialize: function(session,attributes)
                {
                    var contact_model = _.find(this.models,function(model)
                    {
                        return model.model === 'res.partner';
                    });
                    contact_model.fields.push('badge');
                    return _super_posmodel.initialize.call(this,session,attributes);
                },
            });
        });
