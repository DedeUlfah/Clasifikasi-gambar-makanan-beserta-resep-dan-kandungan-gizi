# Create the model
base_model = ResNet50(weights=None, include_top=False, input_shape=(227, 227, 3))

model = Sequential()
model.add(base_model)
model.add(GlobalAveragePooling2D())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50)

# Save the model
model.save(model_save_path)
print(f"Model saved at: {model_save_path}")

# Evaluate the model on the test set
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)

# Calculate overall accuracy
accuracy = metrics.accuracy_score(np.argmax(y_test, axis=1), y_pred)
print("Accuracy:", accuracy)
