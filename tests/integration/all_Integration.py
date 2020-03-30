import nose
import sys

argv = sys.argv[:]
argv.insert(1, "--verbosity=2")
nose.main(argv=argv)