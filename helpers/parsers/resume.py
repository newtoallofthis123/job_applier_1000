import re
from spacy import load as spacy_load
from spacy.language import Language

from helpers.exceptions import PersonMissingException

# The possible sections in a resume
# TODO: Make this automated and configurable
SECTIONS = [
    "summary",
    "experience",
    "education",
    "skills",
    "projects",
    "certifications",
    "awards",
    "publications",
    "languages",
    "interests",
    "references",
]


class ResumeParser:
    def __init__(self, content: str, nlp: Language = spacy_load("en_core_web_sm")):
        self.content = content
        self.nlp = nlp
        self.doc = self.nlp(content.lower())

    def parse_candidate_name(self) -> str:
        # NOTE: The possible list is only left here for debugging purposes
        possible = []

        for ent in self.doc.ents:
            if ent.label_ == "PERSON":
                possible.append(ent.text)

        if possible:
            return possible[0]

        raise PersonMissingException("Person name not found")

    def parse_email(self) -> str | None:
        email_re = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

        res = re.search(email_re, self.content)

        if res:
            return res.group().strip()
        else:
            return None

    def parse_mobile(self) -> str | None:
        mobile_res = r"(\+?\d{1,2}\s?)?(\d{3}\s?\d{3}\s?\d{4})"

        res = re.search(mobile_res, self.content)

        if res:
            return res.group().strip()
        else:
            return None

    def parse(self) -> dict:
        email = self.parse_email()
        phone = self.parse_mobile()
        name = self.parse_candidate_name().title()

        res = {
            "name": name,
            "email": email,
            "phone": phone,
        }

        return res
