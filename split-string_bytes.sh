#!/bin/bash

# Function to split a string into individual bytes and assign variables
split_bytes_and_assign() {
    local input=$1
    local length=${#input}

    # Loop through the string, taking two characters at a time
    for ((i = 0; i < length; i += 2)); do
        # Construct variable name with position information
        var_name="byte$((i/2 + 1))"

        # Assign byte to variable
        declare "$var_name"="${input:i:2}"

        # Output byte-variable pair
        echo -n "${input:i:2},$var_name "
    done
}

# Main script
# Example 32-byte string
input_string="0123456789ABCDEF0123456789ABCDEF"

echo "Input String: $input_string"

echo "Byte-Variable Pairs:"
# Call the split_bytes_and_assign function to split the string and assign variables
split_bytes_and_assign "$input_string"
echo "" # For newline
