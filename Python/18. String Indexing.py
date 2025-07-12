#indexing = accessing elements of a sequence using [start : end : step]

credit_number = "987-654-3210"
print(credit_number[0])
print(f"First four Digits in credit card: {credit_number[0:3]}")
print(f"Next four Digits in credit card: {credit_number[4:7]}")
print(f"Last Digits in credit card: {credit_number[-2]}")

print(f"with Step 2: ({credit_number[1::2]})")

print(f"Last four Digits in credit card: XXXX-XXXX{credit_number[-5:]}")