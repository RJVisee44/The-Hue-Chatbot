# The-Hue-Chatbot
Hue is a simple chatbot that was created for fun. He currently isn't very smart, but together we will get smarter. More data = more knowledge. Currently, Hue uses a natural language processing approach to understand your input and generate an approach response from a database of tags. From those tags, he sleects the best reponse based on similarity between the user input and databse of patterns. Future upgrades will have Hue have memory, for questions such as Why? or How? Furthermore, Hue will continue to get smarter by improving the similarity response. To learn more about chatbot's and this approach, please refer to Tech with Tim's awesome [tutorial](https://www.youtube.com/watch?v=wypVcNIH6D4) 

## Future Upgrades
- [ ] More data! -> Will use LSTM with more data. 
- [X] Add a similarity score to generate the correct response, instead of a random one.
- [ ] Improve similarity score
- [ ] Memory

## Chat with Hue
Download GloVe pretrained word vectors from here: https://github.com/stanfordnlp/GloVe. I used the Wikipedia 2014 + Gigaword 5 pretrained model. 

Run:

`chat.py`

## Data
Data was collected from Kaggle: https://www.kaggle.com/kausr25/chatterbotenglish. This data was taken and manually put into tags to generate the my_intents.json file. This was accomplished using create_dataset.py

## Train
If you would like to train Hue on your own data: 
1) Generate a `my_intents.json` file with the same format
2) Run `train.py` and specify the absolute path to the my_intents.json file, the emb_dim (embedding dimension) for word embedding and the number of epochs (num_epochs) you'd like to train. If you would like to view training accuracy and loss after, set `show_training_results=True`. 

e.g. `train('my_intents.json',emb_dim=256,num_epochs=50,show_training_results=True)`
