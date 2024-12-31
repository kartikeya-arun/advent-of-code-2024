with open('input.txt', 'r') as file:
    def get_valid_sections(text):
        """Get sections of text that come after do() but not after don't()"""
        sections = []
        i = 0
        current_section = ""
        ignore_mode = False

        while i < len(text):
            # Check for "don't()"
            if i + 7 <= len(text) and text[i:i+7] == "don't()":
                ignore_mode = True
                i += 7
                continue

            # Check for "do()"
            if i + 4 <= len(text) and text[i:i+4] == "do()":
                ignore_mode = False
                if current_section:
                    sections.append(current_section)
                current_section = ""
                i += 4
                continue

            # Collect text if we're not in ignore mode
            if not ignore_mode:
                current_section += text[i]
            i += 1

        # Add the last section if it exists
        if current_section:
            sections.append(current_section)

        return sections

    def find_mul_patterns(text):
        results = []
        i = 0

        while i < len(text) - 3:  # Need at least "mul("
            # Check for "mul("
            if text[i:i+4] == "mul(":
                i += 4
                number1 = ""
                number2 = ""

                # Get first number
                while i < len(text) and text[i].isdigit():
                    number1 += text[i]
                    i += 1

                # Check for comma
                if i < len(text) and text[i] == ',':
                    i += 1

                    # Get second number
                    while i < len(text) and text[i].isdigit():
                        number2 += text[i]
                        i += 1

                    # Check for closing parenthesis
                    if i < len(text) and text[i] == ')':
                        if number1 and number2:  # Ensure both numbers were found
                            results.append((number1, number2))
            i += 1

        return results
    inp = file.read()
    ans = 0
    matches = []
    valid_sections = get_valid_sections(inp)
    for section in valid_sections:
        matches += (find_mul_patterns(section))
    for match in matches:
        op1, op2 = int(match[0]), int(match[1])
        ans += (op1*op2)
    print(ans)
