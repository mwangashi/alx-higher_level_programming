#!/usr/bin/python3

class MagicStringCounter:
    def __init__(self):
        self.count = 0
    
    def magic_string(self):
        self.count += 1
        return "BestSchool" * self.count

# Example Usage:
counter = MagicStringCounter()
print(counter.magic_string())  # Output: "BestSchool"
print(counter.magic_string())  # Output: "BestSchoolBestSchool"
print(counter.magic_string())  # Output: "BestSchoolBestSchoolBestSchool"
