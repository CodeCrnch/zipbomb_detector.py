import zipfile

with zipfile.ZipFile("bomb.zip") as z:
    
    total_files_size= sum(i.file_size for i in z.infolist())
    compressed_size = sum(file_info.compress_size for file_info in z.infolist())
    decompressed_size = total_files_size

    print(f"Compressed size is: {compressed_size/1024:.2f} KB")
    print(f"Decompressed size is: {decompressed_size/1024**3:.2f} GB")
    if decompressed_size > compressed_size*1000:
        print("Possible ZIP bomb!!!")
    else:
        print("Not a ZIP bomb.")

    
    
    
