import tempfile
import time

tp = tempfile.NamedTemporaryFile(dir="chapitre3")
tp.write(b'Hello World!')
tp.seek(0)
content = tp.read()
print(content)
time.sleep(10)
tp.close()
