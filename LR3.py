# -*- coding: utf-8 -*-
# 多项式回归

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np


def make_data():
    np.random.seed(10)
    x1 = np.random.randint(5, 10, 50).reshape(50, 1)
    x2 = np.random.randint(10, 16, 50).reshape(50, 1)
    x = np.hstack((x1, x2))
    y = 0.5 * (x1 + x2) * x1
    return x, y


def train(x, y):
    poly = PolynomialFeatures(include_bias=False)
    x_mul = poly.fit_transform(x)
    model = LinearRegression()
    model.fit(x_mul, y)
    print("权重为：", model.coef_)
    print("偏置为：", model.intercept_)
    print("上底 {}，下底 {}梯形真实面积：{}".
          format(5, 8, 0.5 * (5 + 8) * 5))
    x_mul = poly.transform([[5, 8]])
    print(x_mul)
    print("上底 {}，下底为 {}梯形预测面积：{}".
          format(5, 8, model.predict(x_mul)))


if __name__ == '__main__':
    x, y = make_data()
    train(x, y)



