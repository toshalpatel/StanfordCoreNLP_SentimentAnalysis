# Sentiment Analysis using Stanford CoreNLP

This project involves training the Stanford NLP's Sentiment Model, on our dataset of News Articles.

## SentimentTrainingInitModel
This class allows to load a pre-trained model giving a path. This is compiled in the stanford-corenlp-2020-05-21.jar file

<code> --initModelPath path/to/sentiment/model </code>

Hence the command for training will be:

<code> java -cp "classpath/here" -mx8g edu.stanford.nlp.sentiment.SentimentTrainingInitModel -initModelPath edu/stanford/nlp/models/sentiment/sentiment.ser.gz -numHid 25 -epochs 200 -trainPath path/training/file -devPath path/validation/file -train -model path/to/save/new/trained/model/ </code>


And the evaluation command, to test the test data will be:

<code> java -cp "classpath/here" edu.stanford.nlp.sentiment.Evaluate -model path/to/saved/model -treebank path/test/file </code>


## References

https://nlp.stanford.edu/sentiment/

https://github.com/stanfordnlp/CoreNLP/
