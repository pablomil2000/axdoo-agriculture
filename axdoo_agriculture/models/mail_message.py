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

    def _get_allowed_message_post_params(self):
        return {'attachment_ids', 'body', 'message_type', 'partner_ids', 'subtype_xmlid', 'parent_id'}

    def xmlrpc_mail_message_post(self, thread_model, thread_id, body, attachment_name, attachment_encode):
        print("*"*80)
        print("thread_model", thread_model)
        print("thread_id", thread_id)
        print("body", body)
        print("attachment_name", attachment_name)
        print("attachment_encode", attachment_encode)
        print("*"*80)

        attachment = None

        if attachment_name and attachment_encode:
            attachment = self.env["ir.attachment"].create(
                {
                    "name": attachment_name,
                    "datas": attachment_encode
                })

        print("*"*80)
        print("attachment", attachment)
        print("*"*80)

 #
 #        post_data = { "partner_ids": [thread_id], "body": body, "attachment_ids" : [attachment_ids], "message_type": "comment", "subtype_xmlid": "mail.mt_comment"
 # }
 #
 #        "attachment_ids": [
 #            [0, false, {
 #                "name": "adjunto.txt",
 #                "datas": "VGVzdA=="
 #            }]],
 #        "body": "Example Body",
 #        "message_type": "comment",
 #        "partner_ids": [4724],
 #        "subtype_xmlid": "mail.mt_comment"
 #
 #        thread = self.env[thread_model].browse(int(thread_id)).exists()
 #        if not thread:
 #            return
 #
 #        print("*"*80)
 #        print("thread", thread)
 #        print("*"*80)
 #
 #        return thread.message_post(**{key: value for key, value in post_data.items() if key in {'attachment_ids', 'body', 'message_type', 'partner_ids', 'subtype_xmlid', 'parent_id'}}).message_format()[0]


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
                    "author_id": 10,
                    "email_from": "antonio@alfinf.com",
                    "message_type": "comment",
                    "model": "res.partner",
                    "res_id": 4722,
                    "partner_ids": [(4, 4722)],
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

