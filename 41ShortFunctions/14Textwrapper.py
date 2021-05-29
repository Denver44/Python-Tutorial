import textwrap

value = """wraps the input paragraph such that each line
in the paragraph is at most width characters long."""


#------------ 1ST METHOD-----------------------


# wrapper = textwrap.TextWrapper(width=10)
# word_list = wrapper.wrap(text=value)
# Print each line.
# for element in word_list:
#     print(element)
#


#------------ 2ND METHOD-----------------------
result = textwrap.fill(value,20)
# print(result)

