from color import Color, format
from tqdm import tqdm

if __name__ == "__main__":
    # image
    W = 256
    H = 256

    # render
    with open("output.ppm", "w") as f:
        f.write("P3\n")
        f.write(f"{W} {H}\n")
        f.write("255\n")
        for j in range(H):
            for i in tqdm(range(W)):
                r = i / (W - 1)
                g = j / (H - 1)
                b = 0

                color = Color(r, g, b)

                f.write(f"{format(color)}\n")
