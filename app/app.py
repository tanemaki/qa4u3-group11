import glob

import cv2
import numpy as np
import streamlit as st


def app():
    st.title("たべっ子水族館へようこそ！")

    image_paths = sorted(glob.glob("/datasets/tabekko_suizokukan/images/250314a/*"))
    image_index = st.sidebar.number_input(
        "イメージ番号", min_value=0, max_value=len(image_paths) - 1
    )
    image_path = image_paths[image_index]
    image = cv2.imread(image_path)
    st.image(image, channels="BGR", caption=f"たべっ子水族館の画像: {image_index}")


if __name__ == "__main__":
    app()
