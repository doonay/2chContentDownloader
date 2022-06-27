import re

class Validator():
	def validator(self, input_string):
		self.result = re.match(r'https://2ch.hk/[a-z]*/res/\d*\.html', input_string)
		return bool(self.result)

if __name__ == '__main__':
	validator = Validator()
	print('https://2ch.hk/wm/res/4779894.html - All right! This is 2ch thread link.') if validator.validator('https://2ch.hk/wm/res/4779894.html') else print('https://2ch.hk/wm/res/4779894.html - No way! This is NOT 2ch thread link!')
	print('https://2ch.hk/fiz/res/1962431.html - All right! This is 2ch thread link.') if validator.validator('https://2ch.hk/fiz/res/1962431.html') else print('https://2ch.hk/fiz/res/1962431.html - No way! This is NOT 2ch thread link!')
	print('https://2ch.hk/media/res/215666.html - All right! This is 2ch thread link.') if validator.validator('https://2ch.hk/media/res/215666.html') else print('https://2ch.hk/media/res/215666.html - No way! This is NOT 2ch thread link!')
	print('https://google.com - All right! This is 2ch thread link.') if validator.validator('https://google.com') else print('https://google.com - No way! This is NOT 2ch link!')
	print('https://2ch.hk/hry/ - All right! This is 2ch thread link.') if validator.validator('https://2ch.hk/hry/') else print('https://2ch.hk/hry/ - No way! This is NOT 2ch link!')
