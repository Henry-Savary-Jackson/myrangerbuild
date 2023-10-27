def get_term_cmd():
    import os

    term = os.environ.get("TERMCMD", os.environ["TERM"])

    if term in ["xterm", "xterm-256color"]:
        term = "xterm"
    if term in ["xterm-kitty"]:
        term = "kitty"
    if term in ["xterm-termite"]:
        term = "termite"
    if term in ["st", "st-256color"]:
        term = "st"

    if term in [
        "urxvt",
        "rxvt-unicode",
        "rxvt-unicode-256color" "rxvt",
        "rxvt-256color",
    ]:
        term = "urxvt"
    return term
