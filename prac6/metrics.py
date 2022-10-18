def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0
    
    accuracy_i = 0

    tp = 0
    tn = 0
    fp = 0
    fn = 0
    
    for i in range(len(prediction)) :
        if prediction[i] == ground_truth[i] and prediction[i] == True:
            tp+=1
        elif prediction[i] == ground_truth[i] and prediction[i] == False:
            tn+=1
        elif prediction[i] != ground_truth[i] and prediction[i] == True:
            fp+=1
        elif prediction[i] != ground_truth[i] and prediction[i] == False:
            fn+=1

    accuracy = (tp+tn)/(tp+tn+fp+fn)
   
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    
    f1 = (2*(precision*recall))/(precision+recall)

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy

    accuracy = 0
    for i in range(len(prediction)):
        if prediction[i] == ground_truth[i]:
            accuracy+=1
 
    return accuracy/len(prediction)
