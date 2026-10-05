import re
import os

def extract_emails(input_filename, output_filename):
    """Scans a text document for email addresses and saves them to a new file."""
    
    # Regular expression pattern for matching standard email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Check if the input file actually exists before trying to open it
    if not os.path.exists(input_filename):
        print(f"Error: Could not find '{input_filename}'. Please create it and add some text.")
        return

    # 1. File Handling (Read)
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # 2. re (Regex)
    # findall() searches the entire string and returns a list of all matches
    found_emails = re.findall(email_pattern, content)
    
    # Clean up the list by removing duplicates
    unique_emails = list(set(found_emails))
    
    # 3. File Handling (Write)
    with open(output_filename, 'w', encoding='utf-8') as out_file:
        for email in unique_emails:
            out_file.write(email + '\n')
            
    print(f"Success! Extracted {len(unique_emails)} unique email(s).")
    print(f"Saved to: {output_filename}")

if __name__ == "__main__":
    # Define the files you want to use
    source_file = "raw_data.txt"
    destination_file = "emails_only.txt"
    
    # (Optional) Create a dummy file automatically so you can test the script immediately
    with open(source_file, 'w') as dummy:
        dummy.write("Contact us at support@example.com or reach out to sales@example.org. "
                    "Don't email fake@fake, it won't work. "
                    "You can also CC admin@my-website.net.")
    
    # Run the automation tool
    extract_emails(source_file, destination_file)