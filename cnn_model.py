#Building our CNN model
model = Sequential()

#Layer 1
model.add(Conv2D(128,(3,3), activation="relu", input_shape=(128, 128, 1))) 
model.add(MaxPooling2D(pool_size=(2,2)))

#Layer 2
model.add(Conv2D(64,(3,3), activation="relu")) 
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.6))

#Layer 3
model.add(Conv2D(64,(3,3), activation="relu")) 
model.add(MaxPooling2D(pool_size=(2,2)))

#Layer 4
model.add(Conv2D(64,(3,3), activation="relu")) 
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.6))

#Fully Connected Layer
model.add(Flatten()) 
model.add(Dense(128))

#Output Sigmoid Layer
model.add(Dense(1, activation ="sigmoid"))

opt = keras.optimizers.Adam(learning_rate=0.0002)
model.compile(loss = "binary_crossentropy", optimizer = opt, metrics = ['accuracy'])

#Training the model
history = model.fit(train_img, train_lab, batch_size = 16, epochs = 70, verbose = 1, validation_split = 0.2)
