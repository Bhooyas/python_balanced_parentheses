import sys

def check_parentheses(s):
	count = 0
	for i in s:
		if i == "(":
			count += 1
		elif i == ")":
			count -= 1
			if count < 0:
				return False
	if count == 0:
		return True
	return False

if __name__ == '__main__':
	print(check_parentheses(sys.argv[1]))