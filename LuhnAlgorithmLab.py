# Implement the Luhn Algorithm


def verify_card_number(card_number) -> str:
    # Remove any spaces or hyphens from the input
    digits = [int(d) for d in card_number if d.isdigit()]
    
    # Reverse the list to work from right to left
    digits.reverse()
    
    total_sum = 0
    
    for index, digit in enumerate(digits):
        if index % 2 == 1:  # Every second digit
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
        
    if total_sum % 10 == 0:
        return 'VALID!'
    return 'INVALID!'