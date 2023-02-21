# Copyright 2020 Manuel Calero <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'


    def xmlrpc_mail_message_post(self, thread_model, thread_id, body, attachment_name, attachment_encode):
        print("*" * 80)
        print("thread_model", thread_model)
        print("thread_id", thread_id)
        print("body", body)
        print("attachment_name", attachment_name)
        print("attachment_encode", attachment_encode)
        print("*" * 80)

        post_data = {"partner_ids": [thread_id], "body": body, "message_type": "comment", "subtype_xmlid": "mail.mt_comment"}

        if attachment_name and attachment_encode:
            attachment = self.env["ir.attachment"].create(
                {
                    "name": attachment_name,
                    "datas": attachment_encode
                })
            post_data.update({"attachment_ids": [attachment.id]})

        print("*" * 80)
        print("attachment", attachment)
        print("*" * 80)

        print("*" * 80)
        print("post_data", post_data)
        print("*" * 80)

        thread = self.env[thread_model].browse(int(thread_id)).exists()
        if not thread:
            return

        print("*" * 80)
        print("thread", thread)
        print("*" * 80)

        return thread.message_post(**{key: value for key, value in post_data.items() if
                                      key in {'attachment_ids', 'body', 'message_type', 'partner_ids', 'subtype_xmlid',
                                              'parent_id'}}).message_format()[0]
