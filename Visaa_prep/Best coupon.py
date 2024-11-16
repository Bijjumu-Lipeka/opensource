Z=float(input())
amou_after_10_percent=0.90*Z
amou_after_flat_100=Z-100
final_amou=min(amou_after_10_percent,amou_after_flat_100)
print(int(final_amou))
