import sys


class StripLines:

    def read_file(self):
        f = None
        openmode = 'rt'
        supported_encodings = ['utf_8_sig', 'cp932']
        if self.filename.endswith('.uni'):
            supported_encodings = ['utf_16_le', 'utf_8_sig']

        for encoding in supported_encodings:
            try:
                with open(self.filename, openmode, encoding=encoding) as f:
                    self.lines = f.read().splitlines()
                    self.encoding = encoding
                    return
            except UnicodeDecodeError:
                pass

    def write_file(self):
        fileout = self.filename + '.txt'
        with open(fileout, 'wt', encoding=self.encoding) as f:
            for idx,line in enumerate(self.lines):
                if line.rstrip() != '':
                    f.write('%7d: %s\n' % (idx + 1,line))
                    #f.write('%s\n' % (line))
        print('Generate ' + fileout)

    def run(self):
        self.read_file()
        self.write_file()

    def __init__(self, filename):
        self.filename = filename
        self.lines = []


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 2:
        print('Usage: python strip_lines.py <file>')
        sys.exit(1)
    StripLines(argv[1]).run()
    sys.exit(0)
