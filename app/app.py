import glob

import cv2
import numpy as np
import sklearn
import streamlit as st


def app():
    st.title("たべっ子水族館へようこそ！")

    image_paths = sorted(glob.glob("/datasets/tabekko_suizokukan/images/250314a/*"))
    image_index = st.sidebar.number_input(
        "イメージ番号", min_value=0, max_value=len(image_paths) - 1
    )
    image_path = image_paths[image_index]
    image = cv2.imread(image_path)

    pixels = image.reshape(-1, 3)

    model = sklearn.cluster.KMeans(n_clusters=2)
    model.fit(pixels)
    labels = model.predict(pixels)
    mask = labels.reshape(image.shape[:2])
    mask = mask.astype(np.uint8) * 255

    columns = st.columns(2)
    columns[0].image(
        image, channels="BGR", caption=f"たべっ子水族館の画像: {image_index}"
    )
    columns[1].image(mask, caption="クラスタリング結果")


if __name__ == "__main__":
    app()
