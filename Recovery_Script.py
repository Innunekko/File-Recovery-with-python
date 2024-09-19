drive = "\\\\.\\E:"    # Enter the disk/drive letter in place of 'E'
fileD = open(drive, "rb") #drive is opened in raw bytes
size = 1024              # Size of bytes to read
byte = fileD.read(size) # Read 'size' bytes
offs = 0                # Offset location
drec = False            # Recovery mode
     # Recovered file ID
pngid= 1                
jepegid = 1
mp4id = 1
pdfid=1
docid=1
docoff =0
while byte:
    #PNG
    found = byte.find(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')  #This is the staring hex File Signaure
    if found >= 0:
        drec = True
        print('==== Found PNG at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open('recovered\\' + str(pngid) + '.png', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x44\xae\x42\x60\x82') #This it the trailing signature
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
    #DOC        
    found = byte.find(b'\x50\x4B\x03\x04\x14\x00\x06\x00')
    if found >= 0:
        drec = True
        print('==== Found doc at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open('recovered\\' + str(docid) + '.docx', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x50\x4b\x05\x06')
            if bfind >= 0:
                fileN.write(byte[:bfind+22])
                fileD.seek((docoff+12)*size)
                print('==== Wrote doc to location: ' + str(docid) + '.docx ====\n')
                drec = False
                docid += 1
                docoff += 15
                fileN.close()
            else: fileN.write(byte)
    #MP4
    found = byte.find(b'\x66\x74\x79\x70\x6d')
    if found >= 0:
        drec = True
        print('==== Found MP4 at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open('recovered\\' + str(mp4id) + '.mp4', "wb")
        fileN.write(byte[found-4:])
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
    docoff += 1    
    byte = fileD.read(size)
    offs += 1
fileD.close()