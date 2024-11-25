from PIL import Image
import numpy as np


# считаем картинку в numpy array
for i in range(3):
    img = Image.open(f"lunar_images/lunar0{i+1}_raw.jpg")
    data = np.array(img)
    print(data.max() - data.min())
    data1 = ((data - data.min())/(data.max()-data.min())*255).round().astype(np.uint8)
    print(data, '\n', data1, "\n", data1.max())
# запись картинки после обработки
    res_img = Image.fromarray(data1)
    res_img.save(f"pics/newlunar0{i+1}.jpg")