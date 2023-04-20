def decrypt_transposition_cipher(message, num_columns):
    # Calculate the number of rows needed to hold the message
    num_rows = len(message) // num_columns
    if len(message) % num_columns > 0:
        num_rows += 1

    # Create a list of empty strings to hold the rows of the transposition table
    table = ['' for _ in range(num_rows)]

    # Fill in the table with the encrypted message
    for i in range(len(message)):
        row = i % num_rows
        col = i // num_rows
        index = col * num_rows + row
        table[row] += message[index]

    decrypted_message = ''.join(table)
    return decrypted_message


print(decrypt_transposition_cipher("Hore  lW lo",4).strip())