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
