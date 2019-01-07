import optparse

p = optparse.OptionParser()

p.add_option("-O", action="store", dest="outfile")
p.add_option("--output", action="store", dest="outfile")

p.add_option("-d", action="store_true", dest="debug")
p.add_option("--debug", action="store_true", dest="debug")

p.set_defaults(debug=False)

opts, args = p.parse_args()

outfile = opts.outfile
debbugmode = opts.debug

print(outfile, debbugmode)

# % python prog.py -o outfile -d infile1 ... infileN