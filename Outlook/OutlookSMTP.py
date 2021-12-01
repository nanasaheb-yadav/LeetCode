"""
 pip install email
 pip install pywin32
 """

try:
    import json
    import os
    import sys
    import uuid
    import win32com.client
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.utils import COMMASPACE, formatdate
    from email import encoders
    import smtplib
    import traceback
    from datetime import datetime, time, date, timedelta
    import re
    import logging
    from logger_format import setup_logging
except ImportError as error:
    print("Import Error...Script stopped " + str(error))
    exit()


class Outlook_Mails:
    '''
        Functionality provided by Outlook_Mails are Read specific subject Mail, Send Mail, Reply, Reply All, Forward Mails,
        Move Mail to Folder Inside Inbox, Download Attachment from Mail.
    '''

    def __init__(self):
        """ Initializing Logging and Outlook API and it's folder """
        try:
            try:
                self.outlook = win32com.client.GetActiveObject('Outlook.Application').GetNamespace("MAPI")
            except:
                self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            self.inbox = self.outlook.GetDefaultFolder(6)
        except Exception as e:
            self.logger.exception("Message: Class: Outlook_Mails, Function: __init__, Exception\n {}".format(e),
                                  extra=self.extra_dict_common)

    def ReadSubjectMailFolder(self, SubjectSearch, folder_name, getList=False, range_days=1, mkey=0):
        ''' Read Mail with specific Subject like regex ---"Access <SubjectSearch:"".*"">"--- or complete Subject.
            If getList = True, then it sends all the message that matches the Subject else it will send the first matched Subject.
        '''
        self.logger.info(
            "Message: Class: Outlook_Mails, Function: ReadSubjectMailFolder(),  Subject Regular Expression to be searched is : " + str(
                SubjectSearch), extra=self.extra_dict_common)
        fmt = '%Y-%m-%d'
        current_date = datetime.now().strftime(fmt)
        current_date = datetime.strptime(current_date, fmt)
        try:
            self.messageList = []
            self.messages = self.inbox.Folders.Item(folder_name).Items
            self.logger.info(
                "Message: Class: Outlook_Mails, Function: ReadSubjectMailFolder(),  Mails sorting based on [ReceivedTime]",
                extra=self.extra_dict_common)
            self.messages.Sort("[ReceivedTime]", True)
            self.message = self.messages.GetFirst()
            while self.message:
                received_date_time = None
                new_message_txt = ''
                try:
                    received_date_time = self.message.ReceivedTime
                    new_message_txt = self.message.Subject.strip().replace('FW: ', '').replace('RE:', '')
                except:
                    received_date_time = None
                if received_date_time and new_message_txt:
                    received_date = received_date_time.strftime('%Y-%m-%d')
                    received_date = datetime.strptime(received_date, fmt)
                    delta = (current_date - received_date).days
                    if mkey and re.search(SubjectSearch, new_message_txt) and delta <= range_days:
                        self.logger.info(
                            "Message: Class: Outlook_Mails, Function: ReadSubjectMailFolder(),  Mails got by subject name=%s" % (
                                new_message_txt), extra=self.extra_dict_common)
                        if getList == True:
                            self.messageList.append(self.message)
                        elif getList == False:
                            return self.message
                    elif (not mkey) and (SubjectSearch.strip() == new_message_txt.strip()) and delta <= range_days:
                        self.logger.info(
                            "Class: Outlook_Mails, Function: ReadSubjectMailFolder(), Message: Mails got by subject name=%s" % (
                                new_message_txt), extra=self.extra_dict_common)
                        if getList == True:
                            self.messageList.append(self.message)
                        elif getList == False:
                            return self.message
                self.message = self.messages.GetNext()
            if self.messageList == []:
                return None
            else:
                return self.messageList
        except Exception as e:
            self.logger.exception(
                "Message: Class: Outlook_Mails, Function: ReadSubjectMailFolder(),  Exception Occurred",
                extra=self.extra_dict_common)

    def ReadSubjectMailFolderSub(self, SubjectSearch, folder_name, range_days=7, mkey=0):
        ''' Read Mail with specific Subject like regex ---"Access <SubjectSearch:"".*"">"--- or complete Subject.
            If getList = True, then it sends all the message that matches the Subject else it will send the first matched Subject.
        '''
        self.logger.info(
            "Class: Outlook_Mails, Function: ReadSubjectMailFolderSub(), Message: Subject Regular Expression to be searched is : " + str(
                SubjectSearch), extra=self.extra_dict_common)
        fmt = '%Y-%m-%d'
        current_date = datetime.now().strftime(fmt)
        current_date = datetime.strptime(current_date, fmt)
        try:
            self.messageList = []
            self.messages = self.inbox.Folders.Item(folder_name).Items
            self.logger.info(
                "Class: Outlook_Mails, Function: ReadSubjectMailFolderSub(), Message: Mails sorting based on [ReceivedTime]",
                extra=self.extra_dict_common)
            self.messages.Sort("[ReceivedTime]", True)
            self.message = self.messages.GetFirst()
            while self.message:
                received_date_time = None
                new_message_txt = ''
                try:
                    received_date_time = self.message.ReceivedTime
                    new_message_txt = self.message.Subject.strip().replace('FW: ', '').replace('RE:', '')
                except:
                    received_date_time = None
                if received_date_time and new_message_txt:
                    received_date = received_date_time.strftime('%Y-%m-%d')
                    received_date = datetime.strptime(received_date, fmt)
                    delta = (current_date - received_date).days
                    if mkey and re.search(SubjectSearch, new_message_txt) and delta <= range_days:
                        self.logger.info(
                            "Class: Outlook_Mails, Function: ReadSubjectMailFolderSub(), Message: Mails got by subject name=%s" % (
                                new_message_txt), extra=self.extra_dict_common)
                        self.messageList.append((self.message, new_message_txt))
                    elif (not mkey) and (SubjectSearch.strip() == new_message_txt.strip()) and delta <= range_days:
                        self.logger.info(
                            "Class: Outlook_Mails, Function: ReadSubjectMailFolderSub(), Message: Mails got by subject name=%s" % (
                                new_message_txt), extra=self.extra_dict_common)
                        self.messageList.append((self.message, new_message_txt))
                self.message = self.messages.GetNext()
            return self.messageList
        except Exception as e:
            self.logger.exception(
                "Class: Outlook_Mails, Function: ReadSubjectMailFolderSub(), Message: Exception Occurred",
                extra=self.extra_dict_common)

    def ReadSubjectMailUpdatedFilter(self, SubjectSearch, getList=False, range_days=7):
        ''' Read Mail with specific Subject like regex ---"Access <LoginId:"".*"">"--- or complete Subject.
            If getList = True, then it sends all the message that matches the Subject else it will send the first matched Subject.
        '''
        self.logger.info(
            "Class: Outlook_Mails, Function: ReadSubjectMailUpdatedFilter(), Message: Subject Regular Expression to be searched is : " + str(
                SubjectSearch), extra=self.extra_dict_common)
        fmt = '%Y-%m-%d'
        current_date = datetime.now().strftime(fmt)
        current_date = datetime.strptime(current_date, fmt)
        try:
            # folder = outlook.Folders.Item(mailboxFolder)
            # inbox = folder.Folders.Item(mailboxSubFolder)
            self.messageList = []
            self.messages = self.inbox.Folders.Item("Clarity").Items
            self.logger.info(
                "Class: Outlook_Mails, Function: ReadSubjectMailUpdatedFilter(), Message: Mails sorting based on [ReceivedTime]",
                extra=self.extra_dict_common)
            self.messages.Sort("[ReceivedTime]", True)
            self.message = self.messages.GetFirst()
            while self.message:
                # try:
                #    assert (self.message.ReceivedTime), "Python greater than 3.6 cause error while looping to end message ReceivedTime"
                # except AttributeError as e:
                #    break
                received_date_time = None
                new_message_txt = ''
                try:
                    received_date_time = self.message.ReceivedTime
                    new_message_txt = self.message.Subject.strip().replace('FW: ', '').replace('RE:', '')
                except:
                    received_date_time = None
                if received_date_time and new_message_txt:
                    received_date = received_date_time.strftime('%Y-%m-%d')
                    received_date = datetime.strptime(received_date, fmt)
                    delta = (current_date - received_date).days
                    if re.search(SubjectSearch, new_message_txt) and delta <= range_days:
                        self.logger.info(
                            "Class: Outlook_Mails, Function: ReadSubjectMailUpdatedFilter(), Message: Mails got by subject name=%s" % (
                                new_message_txt), extra=self.extra_dict_common)
                        if getList == True:
                            self.messageList.append(self.message)
                        elif getList == False:
                            return self.message
                self.message = self.messages.GetNext()
            if self.messageList == []:
                return None
            else:
                return self.messageList
        except Exception as e:
            self.logger.exception(
                "Class: Outlook_Mails, Function: ReadSubjectMailUpdatedFilter(), Message: Exception Occurred",
                extra=self.extra_dict_common)

    def ReadSubjectMailUpdated(self, SubjectSearch, getList=False):
        ''' Read Mail with specific Subject like regex ---"Access <LoginId:"".*"">"--- or complete Subject.
            If getList = True, then it sends all the message that matches the Subject else it will send the first matched Subject.
        '''

        self.logger.info(
            "Class: Outlook_Mails, Function: ReadSubjectMail(), Message: Subject Regular Expression to be searched is : " + str(
                SubjectSearch), extra=self.extra_dict_common)
        try:
            # folder = outlook.Folders.Item(mailboxFolder)
            # inbox = folder.Folders.Item(mailboxSubFolder)
            self.messageList = []
            self.messages = self.inbox.Items
            self.logger.info(
                "Class: Outlook_Mails, Function: ReadSubjectMail(), Message: Mails sorting based on [ReceivedTime]",
                extra=self.extra_dict_common)
            self.messages.Sort("[ReceivedTime]", True)
            self.message = self.messages.GetFirst()
            while self.message:
                # try:
                #    assert (self.message.ReceivedTime), "Python greater than 3.6 cause error while looping to end message ReceivedTime"
                # except AttributeError as e:
                #    break
                new_message_txt = self.message.Subject.strip().replace('FW: ', '').replace('RE:', '')
                if re.search(SubjectSearch, new_message_txt):
                    if getList == True:
                        self.messageList.append(self.message)
                    elif getList == False:
                        return self.message

                self.message = self.messages.GetNext()
            if self.messageList == []:
                return None
            else:
                return self.messageList
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: ReadSubjectMail(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)

    def ReadSubjectMail(self, SubjectSearch, getList=False):
        ''' Read Mail with specific Subject like regex ---"Access <LoginId:"".*"">"--- or complete Subject.
            If getList = True, then it sends all the message that matches the Subject else it will send the first matched Subject.
        '''

        self.logger.info(
            "Class: Outlook_Mails, Function: ReadSubjectMail(), Message: Subject Regular Expression to be searched is : " + str(
                SubjectSearch), extra=self.extra_dict_common)

        try:
            # folder = outlook.Folders.Item(mailboxFolder)
            # inbox = folder.Folders.Item(mailboxSubFolder)
            self.messageList = []
            self.messages = self.inbox.Items
            self.logger.info(
                "Class: Outlook_Mails, Function: ReadSubjectMail(), Message: Mails sorting based on [ReceivedTime]",
                extra=self.extra_dict_common)
            self.messages.Sort("[ReceivedTime]", True)
            self.message = self.messages.GetFirst()
            while self.message:
                try:
                    assert (
                        self.message.ReceivedTime), "Python greater than 3.6 cause error while looping to end message ReceivedTime"
                except AttributeError as e:
                    break
                if re.search(SubjectSearch, self.message.Subject.strip()):

                    if getList == True:
                        self.messageList.append(self.message)
                    elif getList == False:
                        return self.message

                self.message = self.messages.GetNext()
            if self.messageList == []:
                return None
            else:
                return self.messageList
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: ReadSubjectMail(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)

    def ForwardMail(self, Subject, to, additionalSubject, additionalBody):
        ''' Forward the searched Subject Mail with additional Subject and Body to Receiver '''

        self.logger.info(
            "Class: Outlook_Mails, Function: ForwardMail(), Message: Subject Regular Expression to be searched and Receiver are : " + str(
                Subject) + " " + str(to), extra=self.extra_dict_common)
        self.logger.info(
            "Class: Outlook_Mails, Function: ForwardMail(), Message: Additional Subject and Body are : " + str(
                additionalSubject) + "\n" + str(additionalBody), extra=self.extra_dict_common)

        try:
            self.forwardMessage = self.ReadSubjectMail(Subject, False)
            if self.forwardMessage is not None:
                self.forwardMessage.Forward()
                if additionalBody is not None:
                    self.forwardMessage.Body = additionalBody + self.forwardMessage.Body
                self.forwardMessage.Subject = additionalSubject + ": " + self.forwardMessage.Subject
                self.forwardMessage.To = str(to)
                self.forwardMessage.Send()
                self.logger.info("Class: Outlook_Mails, Function: ForwardMail(), Message: Mail forwarded successfully",
                                 extra=self.extra_dict_common)
                return True
            else:
                self.logger.info("Class: Outlook_Mails, Function: ForwardMail(), Message: No mail with subject found",
                                 extra=self.extra_dict_common)
                return False
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: ForwardMail(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)
            return False

    def ReplyAll(self, Subject, AdditionalBody):
        ''' ReplyAll the specific Subject Mail to all Receivers mentioned in mail with Additional Body '''

        self.logger.info(
            "Class: Outlook_Mails, Function: ReplyAll(), Message: Subject Regular Expression to be searched and Additional Body are : " + str(
                Subject) + "\n" + AdditionalBody, extra=self.extra_dict_common)

        try:
            self.replyAllMessage = self.ReadSubjectMail(Subject, False)
            if self.replyAllMessage is not None:
                self.replyAllMessage.ReplyAll()
                self.replyAllMessage.Body = AdditionalBody + self.replyAllMessage.Body
                self.replyAllMessage.Send()
                self.logger.info("Class: Outlook_Mails, Function: ReplyAll(), Message: Mail Replied ALL successfully",
                                 extra=self.extra_dict_common)
                return True
            else:
                self.logger.info("Class: Outlook_Mails, Function: ReplyAll(), Message: No mail with subject found",
                                 extra=self.extra_dict_common)
                return False
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: ReplyAll(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)
            return False

    def Reply(self, Subject, AdditionalBody):
        ''' Reply the specific Subject Mail to Sender mentioned in mail with Additional Body '''

        self.logger.info(
            "Class: Outlook_Mails, Function: Reply(), Message: Subject Regular Expression to be searched and Additional Body are : " + str(
                Subject) + "\n" + str(AdditionalBody), extra=self.extra_dict_common)

        try:
            self.replyMessage = self.ReadSubjectMail(Subject, False)
            if self.replyMessage is not None:
                self.replyMessage.Reply()
                self.replyMessage.Body = AdditionalBody + self.replyMessage.Body
                self.replyMessage.Send()
                self.logger.info("Class: Outlook_Mails, Function: Reply(), Message: Mail Replied successfully",
                                 extra=self.extra_dict_common)
                return True
            else:
                self.logger.info("Class: Outlook_Mails, Function: Reply(), Message: No mail with subject found",
                                 extra=self.extra_dict_common)
                return False
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: Reply(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)
            return False

    def MoveToFolderInsideInbox(self, messageInstance, inboxFolder):
        ''' Move the specific message to a particular inboxFolder inside Inbox '''

        try:
            self.logger.info(
                "Class: Outlook_Mails, Function: MoveToFolderInsideInbox(), Message: Moving messageInstance with Subject to folder : " + str(
                    messageInstance.Subject) + "-->" + str(inboxFolder), extra=self.extra_dict_common)
            messageInstance.Move(self.inbox.folders(inboxFolder))
            return True
        except Exception as e:
            logging.exception("Class: Outlook_Mails, Function: MoveToFolderInsideInbox(), Message: Exception Occurred")
            return False

    def DownloadAttachment(self, messageInstance, systemPath):
        ''' Download Attachments to specific System Folder '''

        try:
            for attachment in messageInstance.Attachments:
                attachment.SaveASFile(systemPath + '\\' + attachment.FileName)
                self.logger.info(
                    "Class: Outlook_Mails, Function: DownloadAttachment(), Message: Downloading attachments to System Folder : " + str(
                        attachment.FileName) + " " + str(systemPath), extra=self.extra_dict_common)
                return True
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: Move(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)
            return False

    def DownloadAttachmentpath(self, messageInstance, systemPath):
        ''' Download Attachments to specific System Folder returning full path'''
        downloaded_paths = []
        try:
            for attachment in messageInstance.Attachments:
                fname = systemPath + '\\' + attachment.FileName
                attachment.SaveASFile(fname)
                downloaded_paths.append(fname)
                self.logger.info(
                    "Class: Outlook_Mails, Function: DownloadAttachment(), Message: Downloading attachments to System Folder : " + str(
                        attachment.FileName) + " " + str(systemPath))
            return downloaded_paths
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: Move(), Message: Exception Occurred")
            return downloaded_paths

    def DownloadAttachmentpath_sp_new(self, messageInstance, systemPath, excel_obj):
        ''' Download Attachments to specific System Folder returning full path'''
        downloaded_paths = []
        try:
            for attachment in messageInstance.Attachments:
                date_obj = datetime.now()
                date_str = date_obj.strftime('%Y-%m-%d-%H-%M-%S-%f')
                attach_fname = attachment.FileName
                attach_fname = attach_fname.lower()
                fname = systemPath + '\\' + attach_fname
                attachment.SaveASFile(fname)
                wb = excel_obj.Workbooks.Open(fname, )
                if '.xlsx' in fname:
                    xstr = '.xslx'
                else:
                    xstr = '.xls'
                new_fname = '%s%s' % (date_str, xstr)
                fname = fname.replace(xstr, new_fname)
                wb.SaveAs(fname, FileFormat=56)
                wb.Close()
                downloaded_paths.append(fname)
                self.logger.info(
                    "Class: Outlook_Mails, Function: DownloadAttachment(), Message: Downloading attachments to System Folder : " + str(
                        attachment.FileName) + " " + str(systemPath))
            return downloaded_paths
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: Move(), Message: Exception Occurred")
            return downloaded_paths

    def DownloadAttachmentpath_sp(self, messageInstance, systemPath, excel_obj):
        ''' Download Attachments to specific System Folder returning full path'''
        downloaded_paths = []
        try:
            for attachment in messageInstance.Attachments:
                date_obj = datetime.now()
                date_str = date_obj.strftime('%Y-%m-%d-%H-%M-%S-%f')
                attach_fname = attachment.FileName
                attach_fname = attach_fname.lower()
                fname = systemPath + '\\' + attach_fname
                attachment.SaveASFile(fname)
                wb = excel_obj.Workbooks.Open(fname)
                if '.xlsx' in fname:
                    xstr = '.xslx'
                else:
                    xstr = '.xls'
                new_fname = '%s%s' % (date_str, xstr)
                fname = fname.replace(xstr, new_fname)
                wb.SaveAs(fname, FileFormat=56)
                wb.Close()
                downloaded_paths.append(fname)
                self.logger.info(
                    "Class: Outlook_Mails, Function: DownloadAttachment(), Message: Downloading attachments to System Folder : " + str(
                        attachment.FileName) + " " + str(systemPath))
            return downloaded_paths
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: Move(), Message: Exception Occurred")
            return downloaded_paths

    def GetBodyOfMail(self, messageInstance):
        ''' Get the Body of the Mail '''
        try:
            self.logger.info("Class: Outlook_Mails, Function: GetBodyOfMail(), Message: Get Body of Mail : ",
                             extra=self.extra_dict_common)
            return messageInstance.Body
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: GetBodyOfMail(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)
            return ''

    def GetBodyOfMailHtml(self, messageInstance):
        ''' Get the Body of the Mail '''
        try:
            self.logger.info("Class: Outlook_Mails, Function: GetBodyOfMail(), Message: Get Body of Mail : ")
            return messageInstance.HTMLBody
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: GetBodyOfMail(), Message: Exception Occurred")
            return ''

    def attach_image(self, img_dict):
        with open(img_dict['path'], 'rb') as f:
            # mime = MIMEBase('image', 'png', filename=os.path.basename(img_dict['path']))
            mime = MIMEBase('image', img_dict['img_type'], filename=os.path.basename(img_dict['path']))
            mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(img_dict['path']))
            cid = img_dict['cid']
            mime.add_header('X-Attachment-Id', '%s' % (cid))
            mime.add_header('Content-ID', '<%s>' % (cid))
            # read attachment file content into the MIMEBase object
            mime.set_payload(f.read())
            # encode with base64
            encoders.encode_base64(mime)
            # add MIMEBase object to MIMEMultipart object

            # msg_image = MIMEImage(fp.read(), name = os.path.basename(img_dict['path']))
            # msg_image.add_header('Content-ID', '<{}>'.format(img_dict['cid']))
            return mime

    def SendMailWithImage(self, sender, to, subject, mailBody, attachment, host_name, port_no, password, images=[]):
        ''' Send Mail to specific sender to single/multiple contacts with passed subject and MailBody using SMTP '''

        self.logger.info(
            "Class: Outlook_Mails, Function: SendMail(), Message: Sender and Receiver are : " + str(sender) + " " + str(
                to))
        self.logger.info("Class: Outlook_Mails, Function: SendMail(), Message: Subject and MailBody are : " + str(
            subject) + "\n" + str(mailBody))
        try:
            self.msg = MIMEMultipart('alternative')
            self.msg["From"] = sender
            recipients = to.split('$^$')
            self.msg["To"] = ', '.join(recipients)
            self.msg['Subject'] = subject
            self.smtpString = 'ismtp.corp.capgemini.com'
            login = sender
            Body = []
            Body.append(mailBody)
            self.msg.attach(MIMEText(''.join(Body), 'html'))
            for image_id, image_path in enumerate(images):
                img_type = 'jpg'
                if 'png' in image_path.lower():
                    img_type = 'png'
                msgImage = self.attach_image({'path': image_path, 'cid': image_id, 'img_type': img_type})
                self.msg.attach(msgImage)

            if attachment is not None or attachment is not []:
                for att in attachment:
                    part = MIMEBase('application', "octet-stream")
                    part.set_payload(open(att, "rb").read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                                    % os.path.basename(att))
                    self.msg.attach(part)
                    self.logger.info("Class: Outlook_Mails, Function: SendMail(), Message: File Attached : " + str(att))

            self.smtp = smtplib.SMTP(host=host_name, port=port_no)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.ehlo()
            self.smtp.login(login, password)
            self.smtp.sendmail(sender, recipients, self.msg.as_string())
            self.smtp.close()
            self.logger.info(
                "Class: Outlook_Mails, Function: SendMail(), Message: Mail Sent Successfully using SMTP : " + self.smtpString)
            return True
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: SendMail(), Message: Exception Occurred")
            return False

    def SendMailUpdated(self, sender, to, subject, mailBody, attachment, host_name, port_no, password):
        ''' Send Mail to specific sender to single/multiple contacts with passed subject and MailBody using SMTP '''

        self.logger.info(
            "Class: Outlook_Mails, Function: SendMail(), Message: Sender and Receiver are : " + str(sender) + " " + str(
                to), extra=self.extra_dict_common)
        self.logger.info(
            "Class: Outlook_Mails, Function: SendMailUpdated(), Message: Subject and MailBody are : " + str(
                subject) + "\n" + str(mailBody), extra=self.extra_dict_common)
        try:
            self.msg = MIMEMultipart('alternative')
            self.msg["From"] = sender
            recipients = to.split(',')
            self.msg["To"] = ', '.join(recipients)
            self.msg['Subject'] = subject
            self.smtpString = 'ismtp.corp.capgemini.com'
            login = sender
            Body = []
            Body.append(mailBody)

            self.msg.attach(MIMEText(''.join(Body), 'html'))
            if attachment is not None or attachment is not []:
                for att in attachment:
                    part = MIMEBase('application', "octet-stream")
                    part.set_payload(open(att, "rb").read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                                    % os.path.basename(att))
                    self.msg.attach(part)
                    self.logger.info("Class: Outlook_Mails, Function: SendMail(), Message: File Attached : " + str(att),
                                     extra=self.extra_dict_common)

            self.smtp = smtplib.SMTP(host=host_name, port=port_no)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.ehlo()
            self.smtp.login(login, password)
            self.smtp.sendmail(sender, recipients, self.msg.as_string())
            self.smtp.close()
            self.logger.info(
                "Class: Outlook_Mails, Function: SendMail(), Message: Mail Sent Successfully using SMTP : " + self.smtpString,
                extra=self.extra_dict_common)
            return True
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: SendMail(), Message: Exception Occurred",
                                  extra=self.extra_dict_common)
            return False

    def SendMail(self, sender, to, subject, mailBody, attachment):
        ''' Send Mail to specific sender to single/multiple contacts with passed subject and MailBody using SMTP '''

        self.logger.info(
            "Class: Outlook_Mails, Function: SendMail(), Message: Sender and Receiver are : " + str(sender) + " " + str(
                to))
        self.logger.info("Class: Outlook_Mails, Function: SendMail(), Message: Subject and MailBody are : " + str(
            subject) + "\n" + str(mailBody))

        try:
            self.msg = MIMEMultipart('alternative')
            self.msg["From"] = sender
            recipients = to.split('$^$')
            self.msg["To"] = ', '.join(recipients)
            self.msg['Subject'] = subject
            self.smtpString = 'smtp-mail.outlook.com'
            Body = []
            Body.append(mailBody)
            self.msg.attach(MIMEText(''.join(Body), 'html'))
            if attachment is not None or attachment is not []:
                for att in attachment:
                    part = MIMEBase('application', "octet-stream")
                    part.set_payload(open(att, "rb").read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                                    % os.path.basename(att))
                    self.msg.attach(part)
                    self.logger.info("Class: Outlook_Mails, Function: SendMail(), Message: File Attached : " + str(att))

            self.smtp = smtplib.SMTP(self.smtpString)
            self.smtp.sendmail(sender, recipients, self.msg.as_string())
            self.smtp.close()
            self.logger.info(
                "Class: Outlook_Mails, Function: SendMail(), Message: Mail Sent Successfully using SMTP : " + self.smtpString)
            return True
        except Exception as e:
            self.logger.exception("Class: Outlook_Mails, Function: SendMail(), Message: Exception Occurred")
            return False
