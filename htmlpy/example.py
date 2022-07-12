from htmlpy import *

def example():
    d = Document(
        head=Head([
            Title("My Page"),
            Meta("author", "Me"),
            Reference("style.css", "stylesheet")
        ]),
        body=Body([
            Comment("This is a comment"),
            Link("/code",
                 "Click here",
                 global_attr=GlobalAttributes(id="link")),
            Div([
                Audio([Source("audio.mp3"),
                       Source("audio.opus")]),
                Audio(Source("audio.m4a"))
            ]),
            Div([
                Bold("Bold Text"),
                Bold([Link("/bold", "I am bold")]),
            ]),
            LineBreak(),
            Button(Bold("Hey")),
            Video(Source("vid.mp4"), poster="vid.png", height=1080),
            Style("background: red;"),
            Span("text"),
            Script(inner="print('Inline Script');"),
            Script(src="script.js"),
            Paragraph(["This is a", Bold("Paragraph")]),
            Image("pic.png", 500, 500, "Picture"),
            Heading(1, "Heading"),
            Form("formreq", [
                Selection([
                    OptionGroup(
                        "Swedish Cars",
                        [Option("volvo", "Volvo"),
                         Option("saab", "Saab")]),
                    OptionGroup("German Cars", [
                        Option("mercedes", "Mercedes"),
                        Option("audi", "Audi")
                    ])
                ], "cars"),
                TextArea("This is a text"),
                Input("Enter Password", InputType.Password, minlength=8),
                Input("Submit", InputType.Submit)
            ])
        ],
                  global_attr=GlobalAttributes(css_class="theme-dark")))

    print(d.to_code())


if __name__ == "__main__":
    example()
