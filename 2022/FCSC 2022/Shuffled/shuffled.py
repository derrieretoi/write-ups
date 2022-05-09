import random

flag = list(open("output.txt", "rb").read().strip())
#ORIGINAL CHALLENGE CODE
#random.seed(random.randint(0, 256))
#random.shuffle(flag)
#print(bytes(flag).decode())

def shuffle_under_seed(ls, seed):
	# Shuffle the list ls using the seed `seed`
	random.seed(seed)
	random.shuffle(ls)
	return ls

def unshuffle_list(shuffled_ls, seed):
	n = len(shuffled_ls)
	# Perm is [1, 2, ..., n]
	perm = [i for i in range(1, n + 1)]
	# Apply sigma to perm
	shuffled_perm = shuffle_under_seed(perm, seed)
	# Zip and unshuffle
	ls = list(zip(shuffled_ls, shuffled_perm))
	ls.sort(key=lambda x: x[1])
	return ''.join(chr(a) for (a, b) in ls)

for i in range(0, 256):
	print(unshuffle_list(flag, i))