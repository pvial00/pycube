from pycube import Cube, CubeHMAC, CubeRandom, DataNormalizer
import sys, getpass, time

try:
    mode = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

try:
    input_filename = sys.argv[2]
except IndexError as ier:
    data = raw_input("Enter text to encrypt: ")
    key = getpass.getpass("Enter key: ")
else:
    output_filename = sys.argv[3]

    try:
        infile = open(input_filename, "r")
    except IOError as ier:
        sys.stdout.write("Error: Input file not found")
        sys.exit()
    else:
        data = infile.read()
        infile.close()
        try:
            outfile = open(output_filename, "w")
        except IOError as ier:
            sys.stdout.write("Error: Input file not found")
            sys.exit()

    try:
        key = sys.argv[4]
    except IndexError as ier:
        key = getpass.getpass("Enter key: ")

#start = time.time()
msg = DataNormalizer().normalize(data)

if mode == "encrypt":
    try:
        t = output_filename
    except NameError as ier:
        sys.stdout.write(CubeHMAC().encrypt(msg, key)+"\n")
    else:
        outfile.write(CubeHMAC().encrypt(msg, key))
        outfile.close()
elif mode == "decrypt":
    try:
        t = output_filename
    except NameError as ier:
        sys.stdout.write(CubeHMAC().decrypt(msg, key)+"\n")
    else:
        outfile.write(CubeHMAC().decrypt(msg, key))
        outfile.close()

#end = time.time() - start
#bps = len(data) / end
#sys.stdout.write("Completed in "+str(end)+" seconds\n")
#sys.stdout.write(str(bps)+" bytes per second.\n")
