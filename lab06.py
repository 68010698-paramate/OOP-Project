print("="*15)
print("68010968-Paramate")
print("Lab06-Git and GitHub")
print("Hello Git!")
print("="*15)

def calculate_VAT(price):
    VAT_rate = 0.07
    VAT = price * VAT_rate
    return VAT

def main():
    price = 158.22
    VAT = calculate_VAT(price)
    total_price = price + VAT
    print(f"Price: {price:.2f}")
    print(f"VAT: {VAT:.2f}")
    print(f"Total Price: {total_price:.2f}")

if __name__ == "__main__":
    main()