import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Giris verilerini manuel olarak tanimliyoruz
data = {
    "Elemanlararasimesafe": [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1],
    "L": [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11],
    "W": [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1],
    "h": [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01],
    "Dielektriksabiti": [2] * 10,
    "GHz": [
        5.303301,
        3.535534,
        2.65165,
        2.12132,
        1.767767,
        1.515228,
        1.325825,
        1.178511,
        1.0606601,
        0.964236,
    ],
}

# Veri cercevesini olusturma
df = pd.DataFrame(data)

# Grisi (X) ve Cikis (y) verilerini ayirma
X = df[["Elemanlararasimesafe", "L", "W", "h"]].values  # Girisler
y = df["GHz"].values  # Cikis (GHz)

# Modeli olusturma
model = Sequential()

# Ilk katman: 4 giris, 64 noron, ReLU aktivasyon fonksiyonu
model.add(Dense(64, input_dim=4, activation="relu"))

# Ikinci katman: 32 noron, ReLU aktivasyon fonksiyonu
model.add(Dense(32, activation="relu"))

# Cikti katmani: 1 noron (GHz tahmini)
model.add(Dense(1))

# Modeli derleme
model.compile(optimizer=Adam(learning_rate=0.001), loss="mean_squared_error")

# Modeli egitme
model.fit(X, y, epochs=500, batch_size=5, verbose=1)

from tensorflow.keras.utils import plot_model

plot_model(model, to_file="model_mimari.png", show_shapes=True, show_layer_names=True)

# Model ile tahmin yapma (eğitim sonrası)
predictions = model.predict(X)

# Tahminleri ve gerçek değerleri karşılaştırma
plt.plot(y, label="Gerçek GHz Değerleri", marker="o")
plt.plot(predictions, label="Tahmin Edilen GHz Değerleri", marker="x")
plt.title("Gerçek ve Tahmin Edilen GHz Değerleri")
plt.legend()
plt.show()

# Yeni verilerle tahmin yapma (örnek veriler)
new_data = np.array(
    [[0.02, 0.03, 0.02, 0.002], [0.05, 0.06, 0.05, 0.005]]  # Yeni veri örneği 1
)  # Yeni veri örneği 2

new_predictions = model.predict(new_data)

print("Yeni Veri Tahminleri (GHz):", new_predictions)
