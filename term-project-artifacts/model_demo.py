from transformers import BertTokenizer, BertForSequenceClassification, PretrainedConfig
import torch

#Import tokenizer from transformers
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case = True)

#Load the pretrained model
model = BertForSequenceClassification.from_pretrained('C:\\Users\\david\\OneDrive\\Documents\\GitHub\\CMPE188-Project\\term-project-artifacts\\BERTV3')

#Set the model to evaluation mode
model.eval()
 
#Initialize labels
labels = torch.tensor([1]).unsqueeze(0)

#Create a dictionary that maps labels to high level meanings
dictionary = dict()
dictionary[0] = "Hate Speech"
dictionary[1] = "Offensive Language"
dictionary[2] = "Neither"

#State for the while loop
state = True
while (state):
    #Take user input for VELOCITY!!!! exit if user enters exit
    sentence = input("Enter sentence to be labelled or type exit to quit: ")
    if (sentence == "exit"):
        state = False
    else:
        #Encode the user input with the tokenizer
        encoded_sentence = tokenizer(
                                sentence,                      # Sentence to encode.
                                add_special_tokens = True, # Add '[CLS]' and '[SEP]'
                                return_tensors = "pt", # Return the results as tensors
                        )

        #Create the prediction
        prediction = model(**encoded_sentence, labels=labels)

        #Convert the prediction logits into its sigmoid representation, then convert to python list, and print each percentage
        results = (torch.sigmoid(prediction.logits)).tolist()[0]
        print("\nProbability of each category:\nHate Speech: " + str(int(results[0] * 100)) + "%\nOffensive Language: " + str(int(results[1] * 100)) + "%\nNeither: " + str(int(results[2] * 100)) + "%")

        #Print the dictionary output of the index of the highest probability from the sigmoid logits 
        print("This input is classified as: " + dictionary[results.index(max(results))] + "\n")