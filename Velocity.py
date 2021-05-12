from transformers import BertTokenizer, BertForSequenceClassification, PretrainedConfig
import torch

#Import tokenizer from transformers
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case = True)

#Take user input for VELOCITY!!!!
sentence = input("Enter sentence to be labelled: ")

#Encode the user input with the tokenizer
encoded_sentence = tokenizer(
                        sentence,                      # Sentence to encode.
                        add_special_tokens = True, # Add '[CLS]' and '[SEP]'
                        return_tensors = "pt",

                        # This function also supports truncation and conversion
                        # to pytorch tensors, but we need to do padding, so we
                        # can't use these features :( .
                        #max_length = 128,          # Truncate all sentences.
                        #return_tensors = 'pt',     # Return pytorch tensors.
                   )

#Load the pretrained model
model = BertForSequenceClassification.from_pretrained('BERTV3/')

#Set the model to evaluation mode
model.eval()

#Initialize labels
labels = torch.tensor([1]).unsqueeze(0)

#Create the prediction
prediction = model(**encoded_sentence, labels=labels)

#Convert the prediction logits into its sigmoid representation, then convert to python list
results = (torch.sigmoid(prediction.logits)).tolist()[0]

#Create a dictionary that maps labels to high level meanings
dictionary = dict()
dictionary[0] = "Hate Speech"
dictionary[1] = "Offensive Language"
dictionary[2] = "Neither"

#Print the dictionary output of the index of the highest probability from the sigmoid logits 
print(dictionary[results.index(max(results))])