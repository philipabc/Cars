num=123
print(f'{num=:#x} {num=:#b} {num=:#o}')


#%%
# https://docs.python.org/2/library/string.html#format-specification-mini-language
# format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# fill        ::=  <any character>
# align       ::=  "<" | ">" | "=" | "^"
# sign        ::=  "+" | "-" | " "
# width       ::=  integer
# precision   ::=  integer
# type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

#%%
a=-1234567890.0947 # width=1+10+1+4, precision=4
print(f'{a=}')
print(f'{a=:@<+#015,.4f}')
print(f'{a=:@<+#015,.1f}')
print(f'{a=:@<+#20.4f}\n')

print(f'{a=:@>+#25,.6f}')
print(f'{a=:@>+#025,.6f}')
print(f'{a=:@^+#025,.6f}')
print(f'{a=:@=+#025,.6f}')
print(f'{a=:@=#025,.6f}')
print(f'{a=:@^#025,.6f}')
print(f'{a=:@^#025,.6f}\n')

print(f'{a=:^#025,.2f}')
print(f'{a=:<#025,.2f}')
print(f'{a=:>#025,.2f}')
# %%
