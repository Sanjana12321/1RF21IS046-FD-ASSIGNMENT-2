from django.http import HttpResponse,request
from datetime import date

def decode_message(request):
    # Directly include the message to be encoded
    message = "Attack submarine near Karachi"
    # Encode the message using the encode function
    decoded_message = decoded(message)
    # Return the encoded message as a plain text response
    return HttpResponse(decoded_message, content_type="text/plain")

def decoded(message):
    # Get today's date
    today = date.today()
    # Determine if today is an even day
    is_even_day = today.day % 2 == 0

    # Function to encode a single character
    def decode_char(c):
        if c.isalpha():
            if is_even_day:
                # Encode for even day
                return str(500 + ord(c.upper()) - ord('A') + 1)
            else:
                # Encode for odd day
                return str(ord(c.upper()) - ord('A') + 1).zfill(2)
        # Return non-alphabet characters as is
        return c

    # Encode each character in the message
    decoded_chars = [decode_char(c) for c in message]
    # Join the encoded characters with spaces
    return ' '.join(decoded_chars)