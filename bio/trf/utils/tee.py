class Tee:
    """Duplicates writes to both original stream and a file (like Unix 'tee')."""
    def __init__(self, original_stream, file):
        self.original_stream = original_stream
        self.file = file

    def write(self, message):
        self.original_stream.write(message)
        self.file.write(message)

    def flush(self):
        self.original_stream.flush()
        self.file.flush()
