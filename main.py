from tqdm import tqdm

if __name__ == "__main__":
    W = 256
    H = 256

    with open("output.ppm", "w") as f:
        f.write("P3\n")
        f.write(f"{W} {H}\n")
        f.write("255\n")
        for j in range(H):
            for i in tqdm(range(W)):
                r = i / (W - 1)
                g = j / (H - 1)
                b = 0

                r = int(r * 255)
                g = int(g * 255)

                f.write(f"{r} {g} {b}\n")
