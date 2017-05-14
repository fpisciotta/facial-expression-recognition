import base64
import numpy as np
from PIL import Image
from log import load_model
from keras.models import model_from_json

batch_size = 128
img = Image.open('test.jpg').convert('L')
img.thumbnail((48,48), Image.ANTIALIAS)
data = np.asarray(img.getdata()).reshape(img.size)
print(data.shape)
data = data.reshape(-1, 1, data.shape[0], data.shape[1])
print(data.shape)
model = load_model('model.json');
#print(model);
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
y = model.predict(data, batch_size=batch_size, verbose=1)
print(y);

