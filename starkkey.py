from starkware.crypto.signature.signature import *
from perpetual_messages import *


# To Generate Public and private key pair for starkex


# private_stark_key = get_random_private_key()
# print(private_stark_key)
# stark_key = private_key_to_ec_point_on_stark_curve(private_stark_key)[0]
# print(stark_key)

# Generate message hash to sign.
transfer_msg_hash = get_transfer_msg(
    asset_id=
286442224669982855773917167725901379555005478797788066723536016706544965407,
    asset_id_fee=0,
    receiver_public_key=
2825868930652315540133093693348064822157481518754303749560050236804923333506,
    sender_position_id=3,
    receiver_position_id=4,
    src_fee_position_id=3,
    nonce=0,
    amount=3,
    max_amount_fee=0,
    expiration_timestamp=20000000)

# Sign message with previously generated private key.
r, s = sign(
    msg_hash=transfer_msg_hash,
    priv_key=2039715394537995157078655585918023710256920365615264397456354803482530021769)

# Verify signature matches message and stark key.
verify(
    msg_hash=transfer_msg_hash,
    r=r,
    s=s,
    public_key=729444128562970529772220197207218943961743802667126218259376735833498015466)
# Display signature components as hex.
print("r value is {} ",hex(r))
print("s value is {} s", hex(s))