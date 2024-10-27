import re
number_regex = re.compile(r"""
^                      # Start of string
[+-]?                  # Optional sign
(                      # Group for number part
    \d+(\.\d*)?          # Digits, optionally followed by a dot and more digits
    |                    # OR
    \.\d+                # A dot followed by digits
)
([eE][+-]?\d+)?        # Optional exponent part
$                      # End of string
""", re.VERBOSE)

# Match the string against the rege x
return bool(number_regex.match(s))
