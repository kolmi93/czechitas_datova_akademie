import numpy as np

# Šifrovací mřížka
coding_matrix = np.array([[1, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0]])

# Zašifrovaný text
ciphertext = "GTYJOIROEUBDIATD"

# Vytvoříme matici pro dekódování
input_matrix = np.empty([4, 4], dtype=str)
for i in range(len(ciphertext)):
    input_matrix[i % 4][i // 4] = ciphertext[i]

# Dekódujeme text
decoded_text = ""
for i in range(4):
    coding_matrix = np.rot90(coding_matrix, -1)
    for j in range(4):
        decoded_text += input_matrix[j][i]

print(decoded_text)