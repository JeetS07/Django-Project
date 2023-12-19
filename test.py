import pyotp
import qrcode

key = "jeet"

otp = pyotp.totp.TOTP(key)
print(otp.now())

uri = otp.provisioning_uri(name="jeet", issuer_name="app1")

print(uri)

qrcode.make(uri).save("./templates/totp.png")

print(otp.verify(input("Enter OTP:")))
