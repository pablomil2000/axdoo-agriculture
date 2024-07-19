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

            print("*"*80)
            print("ValueError")
            print("*"*80)

            parent_id = None
            user_id = self._get_email_to_user(message_dict)


            print("*"*80)
            print("user_id", user_id)
            print("*"*80)

            if not user_id:
                return

            print("*"*80)
            print("user_id.company_id", user_id.company_id)
            print("*"*80)

            if user_id.company_id:
                parent_id = self._get_email_from_partner(user_id, message_dict)

            print("*"*80)
            print("parent_id", parent_id)
            print("*"*80)

            if not parent_id:
                return
            else:
                message_dict.update({
                    "model": "res.partner",
                    "res_id": parent_id.id,
                })

            print("*"*80)
            print("message_dict", message_dict)
            print("*"*80)

            # self._create_notification(user_id, parent_id)

            self._create_message(user_id, parent_id, **message_dict)

        return res

    def _create_notification(self, user_id, parent_id):
        self.env['mail.message'].create({
            'message_type': 'notification',
            'subject': 'Email recibido',
            'model': 'res.partner',
            'res_id': parent_id.id,
            'partner_ids': [user_id.partner_id.id],
            'author_id': self.env.user.partner_id.id,
            'notification_ids': [(0, 0, {
                'res_partner_id': user_id.partner_id.id,
                'notification_type': 'inbox',
            })],
        })


    def _create_message(self, user_id, parent_id, **message_dict):

        print("*"*80)
        print("_create_message")
        print("-"*80)
        print("user_id", user_id)
        print("-"*80)
        print("parent_id", parent_id)
        print("*"*80)


        values = {
            'body': message_dict.get('body'),
            'author_id': parent_id.id
        }

        try:

            attachments = attachments or []
            attachment_ids = attachment_ids or []
            attachment_values = self._message_post_process_attachments(attachments, attachment_ids, values)
            values.update(attachment_values)

        except Exception:
            pass

        print("|"*80)
        print("values", values)
        print("|"*80)



        message = parent_id.message_post(values)

        return message


    @api.model
    def _get_email_to_user(self, message_dict):
        email_to = message_dict.get("to")

        if not email_to:
            return None

        user_id = self.env['res.users'].sudo().search([
            ('login', '=', 'admin')
        ], limit=1)

        return user_id

    @api.model
    def _get_email_from_partner(self, user_id, message_dict):
        email_from = message_dict.get("email_from")

        print("*"*80)
        print("email_from", email_from)
        print("*"*80)

        if not email_from:
            return None
        partner_id = self.env['res.partner'].sudo().search([
            ('email', '=', tools.email_normalize(email_from)), ('company_id', '=', user_id.company_id.id)], limit=1)
        if not partner_id:
            partner_id = self.env['res.partner'].sudo().search([
                ('email', '=', tools.email_normalize(email_from))], limit=1)
        return partner_id
