from typing import Any, Iterable, Mapping
from helpers.parsers.resume import re
from model.connect import get_ollama_response


def generate_cover_letter(info: dict) -> Iterable[Mapping[str, Any]]:
    """
    Generate a cover letter for a candidate

    Args:
        info (dict): A dictionary containing the following keys:
            - name (str): The name of the candidate
            - email (str): The email of the candidate
            - phone (str): The phone number of the candidate
            - skills (list): A list of the candidate's skills
            - experience (list): A list of the candidate's experience
            - job_description (str): The job description
            - company (str): The company the candidate is applying for

    Returns:
        Iterable[Mapping[str, Any]]: A stream of data from Ollama
    """

    prompt = f"""
    Please put anything that the user has to change in []
    Generate a cover letter for a candidate whose's name is {info['name']} and applying a job for {info['company']}.
    Always include a section about the candidate's experience.
    Be sure to convey that the candidate is a good fit for the job and is excited to learn and grow with the company.
    """

    if "skills" in info:
        prompt += f"The candidate's skills are: {",".join(info['skills'])}"

    if "experience" in info:
        prompt += " The candidate's experiences are:"
        for exp in info["experience"]:
            prompt += f"""
            {exp['name']}
            {exp['position']}
            {exp['description']}
            """

    if "projects" in info:
        prompt += "The candidate's projects are:"
        for proj in info["projects"]:
            prompt += f"""
            {proj['name']}
            {proj['description']}
            """

    prompt += f"""
    The job description is as follows:

    {info['job_description']}

    The candidate's resume is as follows:

    Name: {info['name']}
    Email: {info['email']}
    """

    prompt += """
    NOTE: 
    - Don't include an address in the cover letter.
    - Be polite and professional.
    - Be concise, yet get the point across.
    - DO NOT leave any blanks to be filled in by the user. Use the already provided information and the user's
    resume.
    """

    return get_ollama_response(prompt)


def find_tokens(text):
    to_replace = re.findall(r"\[(.*?)\]", text)

    return to_replace


def replace_tokens(haystack, tokens):
    for token in tokens:
        haystack = haystack.replace("[" + token + "]", tokens[token])

    return haystack
