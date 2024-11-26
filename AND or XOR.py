def and_xor_operations(input_string):
    print(f"Original string: {input_string}")
    print("\nResults:")
    print(f"{'Character':<10}{'AND with 127':<15}{'XOR with 127':<15}")
    print("-" * 40)
    
    for char in input_string:
        and_result = ord(char) & 127  # Perform AND operation with 127
        xor_result = ord(char) ^ 127  # Perform XOR operation with 127
        print(f"{char:<10}{and_result:<15}{xor_result:<15}")

# Input string
input_string = "\\Hello world"
and_xor_operations(input_string)
