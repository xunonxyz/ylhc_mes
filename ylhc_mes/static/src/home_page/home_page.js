/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";


export class HomePage extends Component {

    setup() {
        // super.setup();
        this.state = useState({})
    }

}

HomePage.defaultProps = {
    name: 'Odoo'
}

HomePage.props = {
    name: { type: String, optional: true }
};
HomePage.template = "odoo_tutor.client_demo";
HomePage.components = {};

registry.category("actions").add("client_demo", HomePage);
