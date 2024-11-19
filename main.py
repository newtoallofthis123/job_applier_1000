from helpers.file import setup_file_handlers
from helpers.pdf import PdfExtractor
from helpers.parsers.resume import ResumeParser
from model.cover_letter import find_tokens, generate_cover_letter, replace_tokens

setup_file_handlers()

print("Hello World")

p = PdfExtractor("./IshanJoshi.resume.pdf")
extracted = p.extract()

r = ResumeParser(extracted["text"])
resume = r.parse()
resume["skills"] = ["Python", "JavaScript", "Golang", "Rust"]
resume["experience"] = [
    {
        "name": "Google",
        "position": "Software Engineer",
        "description": "Helped make Google search better and also worked on gemini",
    },
    {
        "name": "Microsoft",
        "position": "Software Engineer",
        "description": "Helped make windows better for enterprise customers",
    },
]
resume["company"] = "Amazon"
resume["job_description"] = """
2025 Marketing Internship - 3 months

Job ID: 2834670 | Amazon EU SARL (UK Branch)
DESCRIPTION

Be involved with planning, executing, and measuring the performance of marketing campaigns. You will play an integral role in building and engaging our customers via demand and lead generation campaigns; creating effective strategies that will promote the long-term growth of Amazon.
How often can you say that your work changes the world? At Amazon, you’ll say it often. Join us and define tomorrow’s innovations in e-commerce.


Key job responsibilities
• Benchmark onsite merchandising best practices globally and develop data-driven recommendations.
• Monitor and optimize performance of marketing campaigns to ensure a flawless customer experience and sustainable growth.
• Develop survey mechanisms and build strategies to optimize internal processes.
• Summarize campaign performance, insights and recommendations for stakeholders
• Build trusted partnerships with the business to influence and support business decisions that promotes improvements and cost reductions.


A day in the life
Your paid 3-month internship includes:
• Mentorship: we care about your career aspirations and strive to assign projects based on your interests. You can learn and be curious with access to unlimited virtual trainings on project management, personal brand, communication skills and many more.

• Get involved: we have with over 13 Amazon Affinity Groups you can join and become an ally to a cause close to your heart (sustainability, diversity, LGBTQ+, mental and/or physical disabilities, local community initiatives, etc.)
"""

res = ""
stream = generate_cover_letter(resume)

for chunk in stream:
    res += chunk["response"]
    print(chunk["response"], end="", flush=True)

print(res)
tokens = find_tokens(res)

print(tokens)

vals = {}
for t in tokens:
    vals[t] = input(f"Enter value for {t}: ")

res = replace_tokens(res, vals)

print(res)
