from __init__ import *

print(gen_rawdata(), type(gen_rawdata()))
print(gen_random_int(1, 32), type(gen_random_int(1, 32)))
print(gen_random_bytes(None), type(gen_random_bytes(None)))
print(gen_random_urlsafe_token(None), type(gen_random_urlsafe_token(None)))
print(gen_random_single_digit(), type(gen_random_single_digit()))
print(gen_random_true_or_false(), type(gen_random_true_or_false()))
