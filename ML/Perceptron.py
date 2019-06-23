import numpy as np
import pandas as pd
#
def getInputData( url ):
    df = pd.read_csv( url, header=None)
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = df.iloc[0:100, [0,1,2,3]].values
    indices = np.random.permutation(X.shape[0])
    training_idx, test_idx = indices[:int(X.shape[0]*.65)], indices[int(X.shape[0]*.65):X.shape[0]]
    X_training, X_test = X[training_idx,:], X[test_idx,:]
    Y_training, Y_test = y[training_idx], y[test_idx]
    Y_training = Y_training.reshape(1,Y_training.shape[0])
    Y_test = Y_test.reshape(1,Y_test.shape[0])
    return X_training, X_test, Y_training, Y_test

def initializeWeight(inputDimension):
    W = np.zeros(inputDimension)
    W = W.reshape(1,inputDimension)
    return W

def train(X_train, Y_train, W, eta):
    print("training...")
    for i in range(X_train.shape[0]):
        k = np.sum(np.dot(W, X_train[i]))#np.dot(X_train, W.T)
        output = -1
        if k > 0:
            output = 1
        tt = -2*X_train[i]*(Y_train[0][i] - output)
        w = (tt)*eta
        #print("0: ", np.sum(np.dot(W.T, X_train[i][0])))
        print("1: Input vector class ", Y_train[0][i], " :: 2: Initial weights " ,W,"3: Input vector: ", X_train[i])
        W = W - w
        print("4: Output predicted   ", output, " :: 5: Dot product of weights and input: ", k, "6: Delta weights ", w, "7: Final weights ",W, "\n")
    return (W)

def predict(W, X_test):
    Y_predict = np.zeros(X_test.shape[0])
    print("Weight vector: ", W)
    for i in range(X_test.shape[0]):
        k = np.sum(np.dot(W, X_test[i]))
        output = -1
        if k > 0:
            output = 1
        Y_predict[i] = output
    return(Y_predict)

X_training, X_test, Y_training, Y_test = getInputData('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

W = initializeWeight(X_training.shape[1])
W = train(X_training, Y_training, W, 0.1 )

predictedvalue = predict(W, X_test)
error = predictedvalue- Y_test[0]
print("Test classes: ", Y_test[0])
print("Predicted values ", predictedvalue)
print("Error values: ", error)