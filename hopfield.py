# Hopfield digit recognition demo (6x6) with an animated GIF showing how learning strength (alpha) affects the recalled output.
# You can change `target_digit`, `noise_level`, `alphas`, or even the patterns to experiment.
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from pathlib import Path

# ----------------------------
# 1) Define 6x6 digit patterns
# ----------------------------
# We represent black pixel as +1, white pixel as -1 for Hopfield.
# Patterns below are hand-crafted; feel free to tweak shapes.
def patt_from_strings(rows):
    arr = []
    for r in rows:
        arr.append([1 if c == "#" else -1 for c in r])
    return np.array(arr, dtype=int)

digit_patterns = {
    0: patt_from_strings([
        "######",
        "#....#",
        "#....#",
        "#....#",
        "#....#",
        
        "######",
    ]),
    1: patt_from_strings([
        "..#...",
        ".##...",
        "..#...",
        "..#...",
        "..#...",
        ".###..",
    ]),
    2: patt_from_strings([
        "####.#",
        "....#.",
        "...#..",
        "..#...",
        ".#....",
        "#####.",
    ]),
    3: patt_from_strings([
        "####..",
        "....#.",
        "..###.",
        "....#.",
        "....#.",
        "####..",
    ]),
    4: patt_from_strings([
        "#...#.",
        "#...#.",
        "#####.",
        "....#.",
        "....#.",
        "....#.",
    ]),
    5: patt_from_strings([
        "#####.",
        "#.....",
        "####..",
        "....#.",
        "....#.",
        "####..",
    ]),
    6: patt_from_strings([
        ".####.",
        "#.....",
        "####..",
        "#...#.",
        "#...#.",
        ".###..",
    ]),
    7: patt_from_strings([
        "#####.",
        "....#.",
        "...#..",
        "..#...",
        ".#....",
        ".#....",
    ]),
    8: patt_from_strings([
        ".###..",
        "#...#.",
        ".###..",
        "#...#.",
        "#...#.",
        ".###..",
    ]),
    9: patt_from_strings([
        ".###..",
        "#...#.",
        "#...#.",
        ".####.",
        "....#.",
        ".###..",
    ]),
}

# Replace '.' with -1 and '#' with +1 already in patt_from_strings.


# ---------------------------------
# 2) Hopfield training & recall API
# ---------------------------------
def train_hopfield(patterns, alpha=1.0):
    """
    patterns: list of 6x6 arrays with entries in {-1, +1}
    alpha: learning strength (scales the Hebbian sum)
    Returns weight matrix W of shape (N, N), N = 36
    """
    N = patterns[0].size
    W = np.zeros((N, N), dtype=float)
    for P in patterns:
        v = P.reshape(-1)
        W += np.outer(v, v)
    # Remove self-connections
    np.fill_diagonal(W, 0.0)
    # Scale by alpha / N (common normalization)
    W *= (alpha / N)
    return W

def recall(W, init_state, steps=12):
    """
    Synchronous updates: s_{t+1} = sign(W s_t), with sign(0)=+1.
    Returns the final state and the sequence of states (including initial).
    """
    s = init_state.copy()
    traj = [s.copy()]
    for _ in range(steps):
        h = W @ s
        s = np.where(h >= 0, 1, -1)
        traj.append(s.copy())
    return s, traj

def add_noise(pattern, noise_level=0.15, rng=None):
    """
    Flip a given fraction of bits (noise_level in [0,1]).
    """
    if rng is None:
        rng = np.random.default_rng(0)
    v = pattern.reshape(-1).copy()
    N = v.size
    k = int(noise_level * N)
    idx = rng.choice(N, size=k, replace=False)
    v[idx] *= -1
    return v


# ----------------------------
# 3) User-configurable settings
# ----------------------------
target_digit = 5     # <- change this to any digit from 0-9
noise_level = 0.25   # <- fraction of flipped pixels in input
alphas = np.linspace(0.2, 2.0, 16)  # learning strengths to sweep
rng = np.random.default_rng(42)


# ----------------------------------------------
# 4) Prepare training set & the (noisy) test set
# ----------------------------------------------
all_patterns = [digit_patterns[d] for d in range(10)]
target = digit_patterns[target_digit]
noisy_input_vec = add_noise(target, noise_level, rng=rng)


# ----------------------------------------------------
# 5) Create frames: for each alpha, recall and visualize
# ----------------------------------------------------
frames = []
tmp_dir = Path("/mnt/data")
gif_path = tmp_dir / "hopfield_digits_alpha_sweep.gif"

for a in alphas:
    W = train_hopfield(all_patterns, alpha=a)
    out_vec, traj = recall(W, noisy_input_vec, steps=10)
    out_img = out_vec.reshape(6,6)

    # Render a single frame with three panels: Target | Noisy Input | Output
    fig = plt.figure(figsize=(6,2.2), dpi=140)
    plt.suptitle(f"Digit {target_digit}  |  alpha={a:.2f}  |  noise={noise_level:.2f}")
    for i, img in enumerate([target, noisy_input_vec.reshape(6,6), out_img]):
        ax = plt.subplot(1,3,i+1)
        ax.imshow(img, cmap="gray", vmin=-1, vmax=1, interpolation="nearest")
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(["Target","Noisy In","Recalled"][i], fontsize=8)
    fig.canvas.draw()
    # Convert to image array for GIF
    frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(frame)
    plt.close(fig)

# Save GIF
imageio.mimsave(gif_path, frames, duration=0.5)

gif_path.as_posix()
