"""把點陣格子轉成像素風 SVG。用法：python assets/tools/pixel2svg.py
輸出到 assets/chibi-pixel/。每個角色是 16x16 的格子，置中放在 20x18 的畫布上。"""
from pathlib import Path

PALETTE = {
    "K": "#5A4A5E",  # 外框
    "P": "#FFD6E0",  # 粉
    "V": "#CDB4F0",  # 紫
    "v": "#9B8BD8",  # 深紫
    "M": "#B8E6D2",  # 薄荷
    "Y": "#FFE08A",  # 黃
    "W": "#FFFFFF",  # 白（眼睛反光）
    "B": "#FF9AA2",  # 腮紅
    "R": "#FF8FA3",  # 桃紅
    "S": "#4A5B6E",  # 螢幕
    "G": "#9FFFE0",  # 螢幕光
    "C": "#FFF4E0",  # 紙
    "c": "#D9C6A5",  # 紙上文字
    "H": "#7A5C58",  # 頭髮
    "F": "#FFE6D8",  # 膚色
}
CW, CH, OX, OY = 20, 18, 2, 1  # 畫布大小與格子偏移

DRONE = [
    ".......KK.......",
    ".KKKK.KYYK.KKKK.",
    "KVVVVK.KK.KVVVVK",
    ".KKKK..KK..KKKK.",
    "...K........K...",
    "....KKKKKKKK....",
    "...KPPPPPPPPK...",
    "..KPPPPPPPPPPK..",
    "..KPPKKPPKKPPK..",
    "..KPPKKPPKKPPK..",
    "..KBBPPPPPPBBK..",
    "..KPPPKPPKPPPK..",
    "...KPPPKKPPPK...",
    "....KKKKKKKK....",
    ".....K....K.....",
    "....KKK..KKK....",
]

def variant(base, rows):
    g = list(base)
    for i, r in rows.items():
        g[i] = r
    return g

def plus(r, c, ch="Y"):
    return {(r, c): ch, (r - 1, c): ch, (r + 1, c): ch, (r, c - 1): ch, (r, c + 1): ch}

SPRITES = {
    "drone-chan": (DRONE, {}),
    "drone-chan-happy": (
        variant(DRONE, {
            8: "..KPPKPPPPKPPK..",
            9: "..KPKPKPPKPKPK..",
            11: "..KPPPKRRKPPPK..",
        }),
        {**plus(7, 1), **plus(12, 18), (3, 17): "Y", (16, 2): "Y"},
    ),
    "drone-chan-thinking": (
        variant(DRONE, {
            8: "..KPPPPPPKKPPK..",
            9: "..KPKKPPPKKPPK..",
            11: "..KPPPPKKKPPPK..",
            12: "...KPPPPPPPPK...",
        }),
        {(6, 17): "v", (6, 18): "v", (6, 19): "v", (7, 19): "v", (8, 18): "v", (8, 19): "v", (10, 18): "v"},
    ),
    "llm-bot": ([
        ".......KK.......",
        "......KRRK......",
        ".......KK.......",
        "...KKKKKKKKKK...",
        "..KMMMMMMMMMMK..",
        "..KMKKKKKKKKMK..",
        ".KKMKSSSSSSKMKK.",
        "KYKMKSGSSGSKMKYK",
        "KYKMKSSSSSSKMKYK",
        ".KKBKSSGGSSKBKK.",
        "..KMKKKKKKKKMK..",
        "..KMMMMMMMMMMK..",
        "...KKKKKKKKKK...",
        ".KMMKMMMMMMKMMK.",
        ".KKK.KMKKMK.KKK.",
        ".....KKKKKK.....",
    ], {}),
    "reward-star": ([
        ".......KK.......",
        "......KYYK......",
        "......KYYK......",
        ".....KYYYYK.....",
        "KKKKKKYYYYKKKKKK",
        "KYYYYYYYYYYYYYYK",
        ".KYYYYYYYYYYYYK.",
        "..KYYKKYYKKYYK..",
        "...KYKKYYKKYK...",
        "...KBYYKKYYBK...",
        "..KYYYYYYYYYYK..",
        "..KYYYYKKYYYYK..",
        ".KYYYYK..KYYYYK.",
        ".KYYYK....KYYYK.",
        "KYYKK......KKYYK",
        "KKK..........KKK",
    ], {**plus(2, 2, "R"), **plus(15, 18, "R"), (1, 17): "R"}),
    "paper-kun": ([
        "..KKKKKKKKK.....",
        "..KCCCCCCCKK....",
        "..KCccccCCKcK...",
        "..KCCCCCCCKKKK..",
        "..KCccccccccCK..",
        "..KCCCCCCCCCCK..",
        "K.KCCKKCCKKCCK.K",
        ".KKCCKKCCKKCCKK.",
        "..KCBCCCCCCBCK..",
        "..KCCCCKKCCCCK..",
        "..KCCCCCCCCCCK..",
        "..KCccccccccCK..",
        "..KCccccccCCCK..",
        "..KCCCCCCCCCCK..",
        "..KKKKKKKKKKKK..",
        "....K.....K.....",
    ], {}),
    "researcher": ([
        ".....KKKKKK.....",
        "...KKHHHHHHKKRR.",
        "..KHHHHHHHHHHKR.",
        ".KHHHHHHHHHHHHK.",
        ".KHHFHHFFHHFHHK.",
        ".KHFFFFFFFFFFHK.",
        ".KHFKKFFFFKKFHK.",
        ".KHFKKFFFFKKFHK.",
        ".KHBFFFFFFFFBHK.",
        ".KHFFFFKKFFFFHK.",
        ".KHKFFFFFFFFKHK.",
        ".KHHKKKKKKKKHHK.",
        "..KKVVCCCCVVKK..",
        "..KVFCccccCFVK..",
        "..KVVCCCCCCVVK..",
        "..KKKKKKKKKKKK..",
    ], {}),
}

def render(grid, overlay):
    cells = {}
    for r, row in enumerate(grid):
        assert len(row) == 16, (r, row, len(row))
        for c, ch in enumerate(row):
            if ch != ".":
                cells[(r + OY, c + OX)] = ch
    cells.update(overlay)
    rects = [
        f'<rect x="{c}" y="{r}" width="1" height="1" fill="{PALETTE[ch]}"/>'
        for (r, c), ch in sorted(cells.items())
        if 0 <= r < CH and 0 <= c < CW
    ]
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" '
        f'shape-rendering="crispEdges">\n  ' + "\n  ".join(rects) + "\n</svg>\n"
    )

if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "chibi-pixel"
    out.mkdir(exist_ok=True)
    for name, (grid, overlay) in SPRITES.items():
        (out / f"{name}.svg").write_text(render(grid, overlay), encoding="utf-8")
        print("wrote", name)
