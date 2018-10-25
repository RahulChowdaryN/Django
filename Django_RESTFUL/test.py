import sys
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

print(sys.executable)
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


print(LEXERS,"LEXERS")
print("Language_Choices",LANGUAGE_CHOICES)

print("Style_Choices",STYLE_CHOICES)

