# old scatter

labels = data.index

x = [_[0] for _ in Y_pca]
y = [_[1] for _ in Y_pca]

x2 = [_[0] for _ in Y_pca if _[1] < 1 and _[1] > -2]
y2 = [_[1] for _ in Y_pca if _[1] < 1 and _[1] > -2]

fig = plt.figure(figsize=(10, 10))
ax = plt.gca()
ax.scatter(x, y)

for i, txt in enumerate(labels):
    ax.annotate(txt, (x[i],y[i]), fontsize = 'medium')