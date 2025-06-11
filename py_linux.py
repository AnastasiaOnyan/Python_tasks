#shell utilites (shutil) for file and disk operations (here we need it to get disk space info)
import shutil

#threshold, percents
threshold = 80
    
#it returns a tuple with three values of bytes: (total, used, free) -> total disk space, how much used, free space
total, used, free = shutil.disk_usage("/")

# in GigaBytes 
total_GB = total / (1024 ** 3)
used_GB = used / (1024 ** 3)
free_GB = free / (1024 ** 3)

# Calculate used space percentage
percent_used = (used_GB / total_GB) * 100

# :.2f - a format specifier; : - start of formatting instructions, .2 - show 2 digits after the decimal point, f - float 
print(f"Disk usage: {percent_used:.2f}%")

#check if it exceeds the threshold
if percent_used > threshold:
    print("WARNING: Disk usage is above threshold!")
else:
    print("Disk usage is OK.")
