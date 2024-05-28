#multiplicand = a
#multiplier = b
#product = c
#where are looking for a * b = c where 1-9 are used exactly once

#we're limit to either 2 and 3 digits multiples or 4 multiples that can be come 5 digits through products
#basically products like 2 * 31 can always be picked because we know they won't equal a six digit number

pandigital = "123456789"
pandigitals_found = set()

def pandigital_check(number):
	number = ''.join(sorted(number))
	return number == pandigital

for a in range(2,99):
	for b in range(12,987):
		c = a * b
		if pandigital_check(str(a) + str(b) + str(c)):
			pandigitals_found.add(c)

for a in range(2,10):
	for b in range(1000,9999):
		c = a * b
		if pandigital_check(str(a) + str(b) + str(c)):
			pandigitals_found.add(c)

print(pandigitals_found)
print(sum(pandigitals_found))


