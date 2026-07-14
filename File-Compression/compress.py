import zlib,base64

data = open('demo.txt','r').read()
data_bytes = bytes(data,'utf-8')
compress_data = base64.b64encode(zlib.compress(data_bytes,9))
decoded_data = compress_data.decode('utf-8')
compress_file =open('compressed.txt','w')
compress_file.write(decoded_data)

decompress_data = zlib.decompress(base64.b64decode(compress_data))
print(decompress_data)