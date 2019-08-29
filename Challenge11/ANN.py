import tensorflow as tf
with tf.device('/gpu:0'):
    import numpy as np
    from tensorflow import keras

    model = keras.Sequential([
        keras.layers.Dense(units=1, input_shape=[1])
    ])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    a = [1, 11, 21, 1211, 111221]
    xs = np.array(range(1, len(a)+1), dtype=float)
    ys = np.array(a, dtype=float)
    print(xs)
    print(ys)

    model.fit(xs, ys, epochs=500)
    print(model.predict([len(a)+2]))


