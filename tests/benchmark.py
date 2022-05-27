#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip modules
import numpy as np
import cv2

# built-in modules
import time


from display_server_interactions import DSI

dsi = DSI()
_window = dsi.get_active_window()
_geo = _window.geometry


def benchmark(function, times: int = 100, show: bool = False) -> np.ndarray:
    results = np.zeros(times, dtype=np.float64)

    for i in range(times):
        last_time = time.time()
        img = function()
        fps = (1 / (time.time() - last_time))
        if show:
            cv2.imshow("OpenCV/Numpy normal", img)
            cv2.waitKey(1)
        print("FPS:", fps, end="\r")
        results[i] = fps

    return results


def benchmark_DSI(**args) -> np.ndarray:
    def func(): return np.array(_window.get_image(_geo))
    return benchmark(function=func, **args)


def benchmark_PIL(**args) -> np.ndarray:
    import PIL.ImageGrab
    def func(): return PIL.ImageGrab.grab(bbox=_geo)
    return benchmark(function=func, **args)


def benchmark_MSS(**args) -> np.ndarray:
    import mss
    with mss.mss() as sct:
        monitor = {"top": _geo[0], "left": _geo[1],
                   "width": _geo[2], "height": _geo[3]}

        def func(): return np.array(sct.grab(monitor))
    return benchmark(function=func, **args)


def main():
    to_benchmark = {
        "DSI": benchmark_DSI,
        "MSS": benchmark_MSS,
        "PIL": benchmark_PIL,
    }

    results = {}

    for name, function in to_benchmark.items():
        print("Benchmarking:", name)
        results[name] = function(show=False, times=200)
        print("\n")

    print("Results:")

    for name, result in results.items():
        print("Benchmark of", name)
        print("\tAverage FPS:", np.mean(result))
        print("\tBest FPS:", np.max(result))
        print("\tWorst FPS:", np.min(result))
        print()

    print("Done.")


if __name__ == "__main__":
    main()
