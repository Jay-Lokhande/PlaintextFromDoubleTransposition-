import itertools

PLAIN_TEXT = "COEP-25"

def create_matrix(text, num_cols):
    num_rows = len(text) // num_cols + (len(text) % num_cols != 0)
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, char in enumerate(text):
        row = i // num_cols
        col = i % num_cols
        matrix[row][col] = char
    return matrix

def read_matrix_by_key(matrix, key):
    num_rows = len(matrix)
    num_cols = len(key)
    result = ''
    for k in key:
        for row in range(num_rows):
            if matrix[row][k] != '':
                result += matrix[row][k]
    return result

def double_transposition_decrypt(ciphertext, row_key, col_key):
    num_cols_row = len(row_key)
    num_cols_col = len(col_key)

    matrix = create_matrix(ciphertext, num_cols_col)
    col_transposed_text = read_matrix_by_key(matrix, col_key)

    matrix = create_matrix(col_transposed_text, num_cols_row)
    plaintext = read_matrix_by_key(matrix, row_key)

    return plaintext

def generate_permutations(length):
    return list(itertools.permutations(range(length)))

def is_valid_plaintext(text):
    return all(char.isascii() and char.isprintable() for char in text)

ciphertext = "52POCE-"

row_key_length = 5
col_key_length = 5

row_key_permutations = generate_permutations(row_key_length)
col_key_permutations = generate_permutations(col_key_length)

found = False

for row_key in row_key_permutations:
    if found:
        break
    for col_key in col_key_permutations:
        plaintext_guess = double_transposition_decrypt(ciphertext, row_key, col_key)

        if is_valid_plaintext(plaintext_guess):
            print("Possible plaintext found:")
            print(plaintext_guess)
            print("Row key:", row_key)
            print("Column key:", col_key)
            if (PLAIN_TEXT == plaintext_guess):
                print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                print("PLAIN TEXT FOUND")
                found = True
                break
