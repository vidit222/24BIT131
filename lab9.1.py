def count_lower_upper(s):
    counts = {"uppercase": 0, "lowercase": 0}
    for char in s:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
    return counts

sample_string = "Hello World! I'm Jenil Parsaniya"
counts = count_lower_upper(sample_string)
print(f"Uppercase Letters: {counts['uppercase']}")
print(f"Lowercase Letters: {counts['lowercase']}")
