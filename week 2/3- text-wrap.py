#text-wrap : Task to wrap the string into a paragraph of given width.

import textwrap

def wrap_text(text, width):
    return textwrap.fill(text, width)

if __name__ == "__main__":
    input_text = "Python is a powerful high-level programming language that lets you work quickly and integrate systems more effectively."
    wrap_width = 40 
    wrapped = wrap_text(input_text, wrap_width)
    print("Wrapped Text:")
    print(wrapped)
