
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generate RSA Key Pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

print("RSA Key Pair Generated!\n")


# Message to Sign
message = b"Hello TYcs Students, this is Digital Signature Demo!"

print("Original Message:", message.decode())


# Sign the Message with Private Key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nMessage signed successfully!")

print("Digital Signature (in bytes):", signature[:50], "...")


# Verify the Signature using Public Key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("\nSignature Verified! Message is authentic and untampered.")

except Exception:
    print("\nSignature Verification Failed! Message was changed.")
