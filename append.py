#THIS FILE APPENDS THE ``` TO PREVENT DISCORD FROM FORMATING THE HOUSE.TXT FILE
def append_text_to_file(file_path, text_to_append):
    try:
        with open(file_path, "a") as file:
            file.write(text_to_append)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# THIS SECTION IS FOR CONFIGURING WHAT FILE AND WHAT TO APPEND
file_path = "house.txt"
text_to_append = "```"
#-CONFIG END-

append_text_to_file(file_path, text_to_append)
