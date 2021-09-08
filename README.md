# Team 3 Project Repository for CMPE 188: Machine Learning For Big Data
## Contributers
* David Danialy
* Aidan Jones
* Christian Oh
* Uyen Nguyen
* Lawrence Nguyen
## Introduction
This project is a hate speech/offensive language classifier that was trained using a dataset found on Kaggle. 
## Implementation 
### Data Preprocessing
The data had already been prelabeled, so all that needed to be done was cleaning the text from mentions, urls, and any other unwanted characters that come from looking at the text. The architecture we decided to use (BERT) is resistant to skewed data, so the distribution of the data was not concerning to us. 
### Machine Learning Model
For the model, we decided to finetune one of Hugging Face's pretrained BERT models with our data. We ended up training three different variations of the model, changing only the hyparameters within the model. You can find the adjustments of the hyper parameters as well as the performance of each model inside of our report.
### Testing
Testing the model was done by exporting the model and using it inside a python program that prompts the user for text. The model then classifies the text as hate speech, offensive language, or neither.
## Conclusion
### Future Work
Providing a nicer interface for users would be ideal for this project. A single page web application or even a browser extension would help users access the model much easier.
### Acknowledgements
The kaggle dataset we used can be found [here](https://www.kaggle.com/mrmorj/hate-speech-and-offensive-language-dataset/).
Where we learned how to finetune a BERT model can be found [here](https://www.youtube.com/watch?v=x66kkDnbzi4).
Thank you Dr.Vishnu Pendyala for facilitating this project
