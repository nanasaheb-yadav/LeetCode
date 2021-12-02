try:
    import os
    import uuid
    import time
    from exchangelib import Credentials, Account, Message, DELEGATE, FileAttachment, ItemAttachment, HTMLBody
except ImportError as error:
    print("Import Error...Script stopped " + str(error))
    exit()


class ExchangeMail:

    def __init__(self, mail_account, mail_user, mail_pass):
        # Initialization of the Credentials, Account
        try:
            self.cred = Credentials(mail_user, mail_pass)
            self.account = Account(mail_account, credentials=self.cred, autodiscover=True, access_type=DELEGATE)
        except Exception as e:
            TwoMinute = 1
            while TwoMinute < 5:
                time.sleep(30)
                self.account = Account(mail_account, credentials=self.cred, autodiscover=True, access_type=DELEGATE)
                TwoMinute += 1

    def SendMail(self, to_recipients, cc_recipients=None, bcc_recipients=None, mail_subject='', mail_body='',
                 mail_attachments=None, is_htmlbody=False, save_mail=True):
        # You can also send emails. If you don't want a local copy:
        """
            Method to Send Mail via Exchange
            to_recipents,cc_recipients & bcc_recipients: List of "To" Mail recipients,"Cc" Mail recipients & "Bcc" Mail recipients.
            type: list
            mail_subject, mail_body: Subject line, Mail body.
            type: str
            mail_attachments: List of attachments.
            type: list
            is_htmlbody: True/False
            type: boolean
            return: True
            rtype:boolean
        """
        try:
            attachments = []
            if is_htmlbody:
                mail_body = HTMLBody(mail_body)
            msg = Message(
                account=self.account,
                subject=mail_subject,
                body=mail_body,
                to_recipients=to_recipients,
                cc_recipients=cc_recipients,
                bcc_recipients=bcc_recipients
            )
            if mail_attachments:
                for attachment in mail_attachments:
                    print(attachment)
                    with open(attachment, 'rb') as f:
                        content = f.read()
                        attachments.append((attachment, content))
                for attachment_name, attachment_content in attachments or []:
                    file = FileAttachment(name=attachment_name, content=attachment_content)
                    msg.attach(file)
            msg.send(save_copy=save_mail)
            return True
        except Exception as e:
            return e

    def ReadMail(self, mail_subject, mail_folder='', top=0, read_body=True, get_attachments=False, attachment_path='',
                 deleteFlag=False, fileExtentsion='.xlsx', movemail=None):

        """
            Method to Read Mail via Exchange
            mail_folder,mail_subject, attachment_path
            type: str
            get_attachments: True/False
            type: boolean
            read_body: True/False
            type: boolean
            return: List of content in body of email.
            rtype:list
        """
        try:
            response_list = list()
            sub_folder = self.account.inbox
            if mail_folder:
                sub_folder = self.account.inbox / mail_folder
            if top:
                all_mails = sub_folder.filter(subject__contains=mail_subject)[:top]
            else:
                all_mails = sub_folder.filter(subject__contains=mail_subject)
            for mail in all_mails:
                response_dict = dict()
                response_dict['email_id'] = mail.sender.email_address
                if read_body:
                    response_dict['body'] = mail.text_body
                    print(mail.text_body)

                if get_attachments:
                    for attachment in mail.attachments:
                        if isinstance(attachment, FileAttachment):
                            if str(attachment.name).lower().endswith(fileExtentsion):
                                attach_path = os.path.join(attachment_path, attachment.name)
                                with open(attach_path, 'wb') as fp, attachment.fp as attachfp:
                                    buffer = attachfp.read(1024)
                                    while buffer:
                                        fp.write(buffer)
                                        buffer = attachfp.read(1024)
                                response_dict['attach_name'] = attachment.name
                        elif isinstance(attachment, ItemAttachment):
                            print("Attached file is ItemAttachment type")
                if deleteFlag:
                    mail.delete()
                if movemail:
                    self.copymailObj = mail
                    mail.move(to_folder=sub_folder / movemail)

                response_list.append(response_dict)

            return response_list

        except Exception as e:
            return e

    def ReadMail_body(self, mail_subject, mail_folder='', top=0, read_body=True, get_attachments=False,
                      attachment_path='',
                      deleteFlag=False, fileExtentsion='.xlsx', movemail=None):

        """
            Method to Read Mail via Exchange
            mail_folder,mail_subject, attachment_path
            type: str
            get_attachments: True/False
            type: boolean
            read_body: True/False
            type: boolean
            return: List of content in body of email.
            rtype:list
        """
        try:
            response_list = list()
            sub_folder = self.account.inbox
            if mail_folder:
                sub_folder = self.account.inbox / mail_folder
            if top:
                all_mails = sub_folder.filter(subject__contains=mail_subject)[:top]
            else:
                all_mails = sub_folder.filter(subject__contains=mail_subject)
            count = 0
            for mail in all_mails:
                if deleteFlag:
                    mail.delete()
                if movemail:
                    self.copymailObj = mail
                    mail.move(to_folder=sub_folder / movemail)
                count += 1
                """print(msg)
                print("attachments       ={}".format(msg.attachments))
                print("conversation_id   ={}".format(msg.conversation_id))
                print("last_modified_time={}".format(msg.last_modified_time))
                print("datetime_sent     ={}".format(msg.datetime_sent))
                print("sender            ={}".format(msg.sender))
                print("text_body={}".format(msg.text_body))
                print("#" * 80)"""

            if count == 0:
                return None
            else:
                return all_mails

        except Exception as e:
            return e

    def reply_sub_body(self, requestid):
        replyall = self.copymailObj.reply_all(subject="RE: " + self.copymailObj.subject,
                                              body='Hello \n \n Please find your request id ' + str(
                                                  requestid) + "\n \n Regards \n Automation Team")
        return replyall

# obj = ExchangeMail('nanasaheb.yadav@xyz.com','nanasaheb.yadav@xyz.com','xxxxx')
# obj.SendMail(['santhosh-kumar@sx.com'],['santhosh@ss.com'],"Subject","<h1>test</h1>",True,False)
# MessageInstanceList = obj.ReadMail(mail_subject="Change for",get_attachments=True,attachment_path=r"C:\\Creation_Poland\Records",deleteFlag=False,movemail="DELETED")
# print(MessageInstanceList)
