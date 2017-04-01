from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import make_hastie_10_2
X, y = make_hastie_10_2(n_samples=10000)
est = GradientBoostingClassifier(n_estimators=200, max_depth=3)
print(est.fit(X, y))

pred=est.predict(X)
est.predict_proba(X)[0]
print(pred)
print("something happened")