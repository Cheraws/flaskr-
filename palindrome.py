def large_palindrome():
	max = 0
	for i in range(500):
		for j in range(500):
			first = i+500
			second = j+500
			combo = first*second;
			if(palindrome(combo) and combo>max):
				max = combo;
	return max;

def palindrome(x):
	num = [int(x) for x in str(x)]
	for i in range(len(num)/2):
		if(i == len(num) - 1):
			return True
		if(not(num[i] == num[len(num)-1-i])):
			return False
	return True

