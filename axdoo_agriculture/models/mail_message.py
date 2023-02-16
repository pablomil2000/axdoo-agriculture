# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def message_send(self):
        message = (
            self.env["mail.message"]
            .sudo()
            .create(
                {
                    "subject": "Message test",
                    "author_id": self.sender.id,
                    "email_from": self.sender.email,
                    "message_type": "comment",
                    "model": "res.partner",
                    "res_id": self.recipient.id,
                    "partner_ids": [(4, self.recipient.id)],
                    "body": "<p>This is a test message</p>",
                }
            )
        )
        if message.is_thread_message():
            self.env[message.model].browse(message.res_id)._notify_thread(message)

        print("*" * 80)
        print("message", message)
        print("*" * 80)

        # [{
        #     "subject": "Subject",
        #     "body": "Body",
        #     "model": "res.partner",
        #     "res_id": 4722,
        #     "attachment_ids": [
        #         [0, false, {
        #             "name": "adjunto.txt",
        #             "datas": "VGVzdA=="
        #         }]
        #     ]


class Message(models.Model):
    _inherit = 'mail.message'
    _description = 'Message'

    def message_send(self):
        message = (
            self.env["mail.message"]
            .sudo()
            .create(
                {
                    "subject": "Message test",
                    "author_id": self.sender.id,
                    "email_from": self.sender.email,
                    "message_type": "comment",
                    "model": "res.partner",
                    "res_id": self.recipient.id,
                    "partner_ids": [(4, self.recipient.id)],
                    "body": "<p>This is a test message</p>",
                }
            )
        )
        if message.is_thread_message():
            self.env[message.model].browse(message.res_id)._notify_thread(message)

        print("*" * 80)
        print("message", message)
        print("*" * 80)

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

