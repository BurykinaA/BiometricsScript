import csv
import io
import os
import numpy as np
from PIL import Image
from MiniFasNet.test import get_sreenshot
from torchvision import transforms
import torch
from MCNN.inference import get_score
from MobileNet.inference import get_score_mobil
import time
from torchvision.io import read_image
import json
import pandas as pd


transform = transforms.Compose(
    [
        transforms.ToPILImage(),
        transforms.Resize((128, 128)),  # Изменение размера изображения
        transforms.ToTensor(),
    ]
)


def get_predict():

    directory = "ImagesForTest"

    # Инициализация словаря для результатов
    results = {}

    # Проходим по всем файлам в директории
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path = os.path.join(directory, filename)
            img = np.array(Image.open(path))
            minifasnet = "real" if get_sreenshot(img) == 1 else "fake"
            results[filename] = minifasnet
            """
            Получение результата всех трех сетей 
                numpy_array = read_image(path)
                # print(numpy_array)
                X = transform(numpy_array)
                X = X * 255
                X = X.unsqueeze(0)
                # print(X)
                img = np.array(Image.open(path))

                print(filename)
                mcnn = "real" if get_score(X) == 1 else "fake"
                print(mcnn)
                mobilenet = "real" if get_score_mobil(X) == 1 else "fake"
                print(mobilenet)
                minifasnet = "real" if get_sreenshot(img) == 1 else "fake"
                print(minifasnet)
            """

    # Возвращаем результаты в формате JSON
    print(json.dumps(results))

    df = pd.DataFrame(list(results.items()), columns=["Image", "Result"])
    df.to_csv("results.csv", index=False)

    return json.dumps(results)


if __name__ == "__main__":
    get_predict()
