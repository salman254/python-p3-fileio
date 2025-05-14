# ✅ Writing to a file
with open("log.txt", mode="w", encoding="utf-8") as log_file:
    log_file.write("First log entry\n")

# ✅ Appending to the file
with open("log.txt", mode="a", encoding="utf-8") as log_file:
    log_file.write("Second log entry\n")

# ✅ Reading from the file
with open("log.txt", encoding="utf-8") as log_file:
    content = log_file.read()
    print("Contents of log.txt:")
    print(content)

# ✅ Reading line-by-line (optional)
print("Reading line by line:")
with open("log.txt", encoding="utf-8") as log_file:
    for line in log_file:
        print(line.strip())
