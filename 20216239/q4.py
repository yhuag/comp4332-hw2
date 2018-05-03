import numpy as np
from keras.models import Sequential
from keras.layers import Dense

def trainData():
    # (a)
    X = np.loadtxt("training.csv", delimiter=",", usecols=(0,1), dtype="int")
    Y_raw = np.loadtxt("training.csv", delimiter=",", usecols=(2), dtype="str")

    # (b)
    Y = np.asarray([1 if (d == "b'Yes'") else 0 for d in Y_raw])

    # (c)(i)
    np.random.seed(4332)

    # (c)(ii)
    model = Sequential()
    model.add(Dense(4, input_dim=2, activation='relu')) 
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(X, Y, epochs=1500, batch_size=4, validation_split=0.2)

    scores = model.evaluate(X, Y)
    print("{}: {}".format(model.metrics_names[1], scores[1]*100))

    return model

def predictData(_model):
    # (a)
    newX = np.loadtxt("new.csv", delimiter=",", dtype="int")

    # (b)
    newY = _model.predict(newX, batch_size=1)

    # (c)
    ans = ["Yes" if (d >= 0.5) else "No" for d in newY]
    with open("output-NN.csv", "w") as f:
        for y,a in zip(newY,ans):
            f.write(str(y[0])+","+str(a))
            f.write("\n")


if __name__ == "__main__":
    model = trainData()
    predictData(model)