import tensorflow as tf

# carrega o conjunto de dados MNIST, que consiste em imagens de digitos escritos a mao (0 a 9).
mnist = tf.keras.datasets.mnist 

# normaliza os valores dos pixels das imagens para intervalo [0, 1]. ajuda no treinamento da rede neural
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Modelo sequencia, consiste de tres camadas:
# flatten: transforma a matriz 2D das imagens (28x28 pixels) em um vetor unidimensional
# Dense: camada totalmente conectada com 128 neuronios e ativacao ReLU.
# Dropout: reduz o overfitting, desativando aleatoriamente 20% dos neuronios.
# Dense: camada de saida com 10 neuronios(um para cada digito) e ativacao softmax.
model = tf.keras.models.Sequential([
    tf.keras.layers.flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compila o modelo com o otimizador Adam,
# funcao de perda entropia cruzada categorica esparca (apropriada para rotulos categoricos) e a metrica de acuracia.
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)