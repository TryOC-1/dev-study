import re

security = re.compile(
    r"""
    \b(\d{2})
    (\d{2})
    (\d{2})
    -
    (\d{1})
    (\d{6})\b
    """,
    re.VERBOSE,
)

inp = input("주민번호를 입력하세요 : ")
secNum = security.findall(inp)

print(security.sub(r"\1\2\3-\4******", inp))
