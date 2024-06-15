import numpy as np
import urllib
import ssl

ssl_context = ssl._create_unverified_context()
image_src = "https://56fa32efe8bd3d139e.gradio.live/file=/content/drive/MyDrive/Fooocus/outputs/2024-06-14/2024-06-14_10-47-05_9036.png"
req = urllib.request.urlopen(image_src, context=ssl_context)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = arr[:, :, ::-1]
img