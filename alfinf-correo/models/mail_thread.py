# -*- coding: utf-8 -*-
from odoo import api, models, tools


class MailThread(models.AbstractModel):
    """
    Overwrite to redefine message routing and process corresponding exceptions
    """
    _inherit = "mail.thread"

    @api.model
    def message_route(self, message, message_dict, model=None, thread_id=None, custom_values=None):
        """
        Overwrite to catch and mark unattached messages

        1. Send notificaion if defined in settings
        """
        res = []
        try:
            res = super(MailThread, self).message_route(
                message, message_dict, model=model,
                thread_id=thread_id, custom_values=custom_values
            )
        except ValueError:

            email_from = message_dict.get("email_from")

            parent_id = None
            user_id = self._mail_find_user_for_gateway(email_from) or self.env.user

            if not user_id:
                return

            parent_id = self._get_email_from_partner(user_id, message_dict)

            if not parent_id:
                return
            else:
                route = self._routing_check_route(
                    message, message_dict,
                    ('res.partner', parent_id.id, custom_values, user_id.id, None),
                    raise_exception=False)
                if route:
                    return [route]

        return res

    @api.model
    def _get_email_from_partner(self, user_id, message_dict):
        email_from = message_dict.get("email_from")

        if not email_from:
            return None
        partner_id = self.env['res.partner'].sudo().search([
            ('email', '=', tools.email_normalize(email_from)), ('company_id', '=', user_id.company_id.id)], limit=1)
        if not partner_id:
            partner_id = self.env['res.partner'].sudo().search([
                ('email', '=', tools.email_normalize(email_from))], limit=1)
        return partner_id
