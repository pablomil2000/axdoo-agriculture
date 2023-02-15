# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Message(models.Model):
    _inherit = 'mail.message'
    _description = 'Message'


    def send(self):
        for message in self:

            print("*"*80)
            print("message", message)
            print("message.is_thread_message", message.is_thread_message())
            print("*"*80)

            if message.is_thread_message():
                self.env[message.model].browse(message.res_id).with_context(
                    do_not_send_copy=True
                )._notify_thread(message)

            tracking_email = self.env["mail.tracking.email"].search(
                [
                    ("mail_message_id", "=", message.id),
                    ("partner_id", "=", self.recipient.id),
                ]
            )

            print("*"*80)
            print("tracking_email.state", tracking_email.state)
            print("tracking_email.error_type", tracking_email.error_type)
            print("tracking_email.state",tracking_email.state,)
            print("*"*80)
