import sys
import tiktoken

encoding = tiktoken.encoding_for_model("text-embedding-ada-002")

count = 0

for line in sys.stdin:
    count += len(encoding.encode(line))

print(count)
