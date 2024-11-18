import re


class ResumeParser:
    def __init__(self, content: str):
        self.content = content

    def parse_email(self):
        email_re = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

        res = re.search(email_re, self.content)

        # return the first email found
        if res:
            return res.group().strip()
        else:
            return None

    def parse_mobile(self):
        mobile_res = r"(\+?\d{1,2}\s?)?(\d{3}\s?\d{3}\s?\d{4})"

        res = re.search(mobile_res, self.content)

        if res:
            return res.group().strip()
        else:
            return None

    def parse(self):
        email = self.parse_email()
        phone = self.parse_mobile()

        res = {
            "email": email,
            "phone": phone,
        }

        return res
