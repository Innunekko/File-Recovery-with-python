drive = "\\\\.\\D:"    # Open drive as raw bytes
disc= 'C' 
fileD = open(drive, "rb")
size = 1024              # Size of bytes to read
byte = fileD.read(size) # Read 'size' bytes
offs = 0                # Offset location
drec = False            # Recovery mode
pngid= 1                # Recovered file ID
jepegid = 1
mp4id = 1
pdfid=1
docid=1
while byte:
    #PNG
    found = byte.find(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')
    if found >= 0:
        drec = True
        print('==== Found PNG at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open('recovered\\' + str(pngid) + '.png', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x44\xae\x42\x60\x82')
            if bfind >= 0:
                fileN.write(byte[:bfind+5])
                fileD.seek((offs+1)*size)
                print('==== Wrote PNG to location: ' + str(pngid) + '.png ====\n')
                drec = False
                pngid += 1
                fileN.close()
            else: fileN.write(byte)
    #JPEG
    found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
    if found >= 0:
        drec = True
        print('==== Found JPG at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open('recovered\\' + str(jepegid) + '.jpg', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\xff\xd9')
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                fileD.seek((offs+1)*size)
                print('==== Wrote JPG to location: ' + str(jepegid) + '.jpg ====\n')
                drec = False
                jepegid += 1
                fileN.close()
            else: fileN.write(byte)
    #MP4
    found = byte.find(b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d')
    if found >= 0:
        drec = True
        print('==== Found MP4 at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open('recovered\\' + str(mp4id) + '.mp4', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x08\x58\x74\x72\x61')
            if bfind >= 0:
                fileN.write(byte[:bfind+4])
                fileD.seek((offs+1)*size)
                print('==== Wrote MP4 to location: ' + str(mp4id) + '.mp4 ====\n')
                drec = False
                mp4id += 1
                fileN.close()
            else: fileN.write(byte)
    #PDF        
    found = byte.find(b'\x25\x50\x44\x46\x2d')
    if found >= 0:
        drec = True
        print('==== Found PDF at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open('recovered\\' + str(pdfid) + '.pdf', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x45\x4f\x46\x0a')
            if bfind >= 0:
                fileN.write(byte[:bfind+4])
                fileD.seek((offs+1)*size)
                print('==== Wrote pdf to location: ' + str(pdfid) + '.pdf ====\n')
                drec = False
                pdfid += 1
                fileN.close()
            else: fileN.write(byte)
   
            
    byte = fileD.read(size)
    offs += 1
fileD.close()