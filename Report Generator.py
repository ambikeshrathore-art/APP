def bold_text(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"**{text}**"
    return wrapper


class Report:

    
    templates = {}


    def __init__(self, title, content):
        self.title = title
        self.content = content


    @classmethod
    def add_template(cls, name, template_function):
        cls.templates[name] = template_function

 
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    
    def __call__(self, template_name):

        template = self.get_template(template_name)

        if template:
            return template(self.title, self.content)

        return "Template not found!"

    
    def __str__(self):
        return f"Report: {self.title}"

   
    def __repr__(self):
        return (
            f"Report(title='{self.title}', "
            f"content='{self.content}')"
        )



def simple_template(title, content):
    return f"""
----- SIMPLE REPORT -----
Title: {title}
Content: {content}
-------------------------
"""



@bold_text
def fancy_template(title, content):
    return f"""
===== FANCY REPORT =====
Title: {title}
Content: {content}
========================
"""


def main():

    
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

 
    title = input("Enter report title: ")
    content = input("Enter report content: ")

    
    report = Report(title, content)

    print("\n1. Simple Template")
    print("2. Fancy Template")

    choice = input("\nChoose template (1/2): ")

    if choice == "1":
        print(report("simple"))

    elif choice == "2":
        print(report("fancy"))

    else:
        print("Invalid choice!")


    print("\nUsing __str__:")
    print(report)

    print("\nUsing __repr__:")
    print(repr(report))


if __name__ == "__main__":
    main()