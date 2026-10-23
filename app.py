from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello from Anastasiia</h1>"
@app.route("/about")
def about():
    return """
    <h1>Project Idea: AI Business Assistant</h1>

    <p>If I had an evening instead of fifteen minutes,
    I would start building AI Business Assistant, a web
    application designed to help small businesses manage
    customers and enquiries more efficiently.</p>

    <p>My idea is to combine a modern, attractive website
    with a simple CRM system and automated workflows.
    Customers would be able to submit enquiries through
    an online form, while business owners could manage
    requests through a private dashboard.</p>

    <p>The application would store customer information,
    track enquiry statuses, and help owners organise
    their daily tasks. I would also like to introduce
    automated notifications and reminders so that
    important customer requests are not forgotten.</p>

    <p>In the future, I would explore AI features that
    could help categorise enquiries and suggest responses.
    The system could be adapted for different types of
    small businesses, such as beauty salons, cleaning
    companies, or flower shops.</p>

    <p>My goal is to develop a practical, user-friendly
    application that could eventually support my
    freelance work.</p>
    """



if __name__ == "__main__":
    app.run(debug=True)