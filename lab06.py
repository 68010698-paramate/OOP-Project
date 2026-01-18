print("="*15)
print("68010968-Paramate")
print("Lab06-Git and GitHub")
print("Hello Git!")
print("="*15)

def calculate_VAT(price):
    VAT_rate = 0.07
    VAT = price * VAT_rate
    return VAT

def discount(price, discount_rate):
    discount_amount = price * discount_rate
    return price - discount_amount

def main():
    price = 158.22
    VAT = calculate_VAT(price)
    discount_rate = 0.10  # 10% discount
    
    price_after_discount = discount(price, discount_rate)
    total_price_with_VAT = price + VAT
    
    print(f"Price: {price:.2f}")
    print(f"VAT: {VAT:.2f}")
    print(f"Total Price: {total_price_with_VAT:.2f}")
    print("="*15)
    print(f"Price after {discount_rate*100:.0f}% discount: {price_after_discount:.2f}")
    

if __name__ == "__main__":
    main()