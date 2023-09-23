import base64
import hashlib
import hmac
import random
import secrets
import uuid


def gen_rawdata() -> str:
    rawdata_1 = secrets.token_urlsafe(None)
    random.seed(str(uuid.uuid4()))
    key = random.randint(1, 32)
    rawdata_2 = str(random.randbytes(key))
    rawdata_raw = rawdata_1 + rawdata_2
    mykdf = hashlib.pbkdf2_hmac(
        "sha256", rawdata_raw.encode("utf-8"), b"", 10**6, dklen=16
    )
    the_uuid = str(uuid.UUID(bytes=mykdf)).upper()
    rawdata = hmac.new(
        bytes(rawdata_2.encode()), the_uuid.encode(), hashlib.sha256
    ).hexdigest()
    return rawdata


def gen_random_int(a: int, b: int) -> int:
    random.seed(gen_rawdata())
    return random.randint(a, b)


DEFALT_NUMBER_OF_BYTES = 32


def gen_random_bytes(nbytes: int = None) -> bytes:
    if nbytes is None:
        nbytes = DEFALT_NUMBER_OF_BYTES
    random.seed(gen_rawdata())
    return random.randbytes(nbytes)


def gen_random_urlsafe_token(nbytes: int = None) -> str:
    tok = gen_random_bytes(nbytes)
    return base64.urlsafe_b64encode(tok).rstrip(b"=").decode("ascii")


def gen_random_single_digit() -> int:
    string = gen_rawdata()
    h = hashlib.sha3_512()
    h.update(string.encode("utf-8"))
    n = int(h.hexdigest(), base=16)
    s = 0
    while True:
        s += n % 10
        n //= 10
        if n > 10:
            break
        else:
            continue
    return s


def gen_random_true_or_false() -> bool:
    num = gen_random_single_digit()
    if num % 2 == 0:
        return True
    else:
        return False
