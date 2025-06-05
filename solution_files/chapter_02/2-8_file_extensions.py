filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')   # removesuffix() 删除后缀

print(simple_filename)
print(f'{simple_filename} removesuffix 删除后缀 ".txt"')

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://') # removeprefix()  删除前缀
print(f'{simple_url} removeprefix 删除前缀 "hyyps://"')