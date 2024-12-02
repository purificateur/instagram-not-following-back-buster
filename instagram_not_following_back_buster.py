import re

# Place the div that wraps users in the corresponding text files
followers_input = 'followers.txt'
followeds_input = 'followeds.txt'
result_output = 'result.txt'

def extract_usernames(input_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
    pattern = r'dir="auto">([^<]+)<\/span>'
    matches = re.findall(pattern, text)
    return set(matches)

def find_unique_elements(followers_matches, followed_matches):
    unique_to_res2 = followed_matches - followers_matches
    return unique_to_res2

followers = extract_usernames(followers_input)
followeds = extract_usernames(followeds_input)

unique_elements = find_unique_elements(followers, followeds)

with open(result_output, 'w', encoding='utf-8') as result_file:
    for item in unique_elements:
        result_file.write(f"{item}\n")

print(f"List of users who aren't following you back have been written to {result_output}")
