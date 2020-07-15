from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def train(x_normal):
    x_normal_train, x_normal_test = train_test_split(x_normal, test_size=0.25, random_state=42)

    print(f"Normal train count: {len(x_normal_train)}")
    print(f"Normal test count: {len(x_normal_test)}")

    model = Sequential()
    model.add(Dense(25, input_dim=x_normal.shape[1], activation='relu'))
    model.add(Dense(3, activation='relu'))  # size to compress to
    model.add(Dense(25, activation='relu'))
    model.add(Dense(x_normal.shape[1]))  # Multiple output neurons
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x_normal_train, x_normal_train, verbose=1, epochs=100)

    return model, x_normal_test
