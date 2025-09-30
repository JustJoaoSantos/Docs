# Importar Bibliotecas
#import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#from sklearn.preprocessing import StandardScaler

# Carrega conjunto de dados iris
iris = load_iris()
x = iris.data
y = iris.target

# separar os dados em conjuntos de treinamento e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# construcao de modelo K-Nearest Neighbor
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)

# previsao no conjunto de teste
predictions = model.predict(x_test)

# Teste de acuracia
accuracy = accuracy_score(y_test, predictions)
print(f"Acuracia do teste de previcao com Iris: {accuracy:.2f}")