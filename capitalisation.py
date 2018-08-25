import re
import fileinput

library = 'library_clean.bib'

import re

def re_sub_verbose(pattern, replace, string):
  def substitute(match):
    return match.expand(replace)

  result = re.sub(pattern, substitute, string)

  return result

for line in fileinput.input(library, inplace=1):
    print re_sub_verbose("booktitle = \{(.*)\},", "booktitle = {{\\1}},", line)
