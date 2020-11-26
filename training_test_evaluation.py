#Evaluation of the training process
#Creating visual representation of training accuracy and loss
#Summarize history for accuracy
plt.plot(history.history['accuracy'], color = '#a3281f')
plt.plot(history.history['val_accuracy'], color = '#1613a1')
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'], color = '#a3281f')
plt.plot(history.history['val_loss'], color = '#1613a1')
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

#Predictions
yhat_probs = model2.predict(test_img, verbose=0)
# predict crisp classes for test set
yhat_classes = model2.predict_classes(test_img, verbose=0)
# reduce to 1d array
yhat_probs = yhat_probs[:, 0]
yhat_classes = yhat_classes[:, 0]

#Printing metrices
# accuracy: (tp + tn) / (p + n)
accuracy = accuracy_score(test_lab, yhat_classes)
print('Accuracy: %f' % accuracy)
# precision tp / (tp + fp)
precision = precision_score(test_lab, yhat_classes)
print('Precision: %f' % precision)
# recall: tp / (tp + fn)
recall = recall_score(test_lab, yhat_classes)
print('Recall: %f' % recall)
# f1: 2 tp / (2 tp + fp + fn)
f1 = f1_score(test_lab, yhat_classes)
print('F1 score: %f' % f1)
 
# confusion matrix
matrix = confusion_matrix(test_lab, yhat_classes)
print(matrix)

average_precision = average_precision_score(test_lab, yhat_classes)
print('Average precision: %f' % average_precision)
