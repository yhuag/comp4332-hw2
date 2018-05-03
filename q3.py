import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def forward(_x1, _x2, _w1, _w2, _b):
    return _x1 * w1 + _x2 * w2 + _b;

def backward(_x, _wb, _alpha, _d, _y):
    return _wb + _alpha * (_d - _y) * _x

def backprop(_x1, _x2, _w1, _w2, _b, _alpha, _d, _y):
    _w1 = backward(_x1, _w1, _alpha, _d, _y)
    _w2 = backward(_x2, _w2, _alpha, _d, _y)
    _b = backward(1, _b, _alpha, _d, _y)
    return (_w1, _w2, _b)


if __name__ == "__main__":
    X1 = [2,0,4,2,2]
    X2 = [0,2,2,4,0]
    D = [0,0,1,1,0]
    alpha = 0.6
    w1, w2, b = 0.3, 0.3, 0.3

    for x1,x2,d in zip(X1,X2,D):
        # forward
        y = sigmoid(forward(x1,x2,w1,w2,b))

        # backprop
        (w1,w2,b) = backprop(x1,x2,w1,w2,b,alpha,d,y)

        # Logging
        print("----------")
        print("w1: {}, w2: {}, b: {}".format(w1,w2,b))
        print("D: {}, Y: {}, MAE Loss: {}".format(d,y,abs(d-y)))