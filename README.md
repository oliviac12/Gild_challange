## Gild_challenge

I was able to pass all the test in the test set. I was using this moudule called [probablepeople](https://github.com/datamade/probablepeople) becasue it uses uses [parserator](https://github.com/datamade/parserator), a library for making and improving probabilistic parsers - specifically, parsers that use python-crfsuite's implementation of conditional random fields.Therefore, I was able to customize and added more example and train the moudule. 

## Following are steps to set up probablepeople and test if my script pass all the tests

1. clone Gild_challenge and submodule probablepeople to your local machine

   ```
   $ git clone --recursive https://github.com/oliviac12/Gild_challenge.git 
   $ cd Gild_challenge/probablepeople
   $ pip install -r requirements.txt  
   $ python setup.py develop
   ```
2. Another thing need to be fixed: downgrade the parserator to version 0.4.1 because the parserator installed with probablepepople is  5.0+ , it doesn't work with the train command we are using next step (ugh I know!) 
    ```
   $ pip uninstall parserator
   $ pip install parserator==0.4.1
    ```  
3. Do a test train with existing data
   ```
   $ parserator train name_data/labeled/labeled.xml,name_data/labeled/company_labeled.xml probablepeople
    ```  
if no error pops up and you see something like this 
"training model on 2078 training examples from ['name_data/labeled/labeled.xml']"
"done training! model file created: probablepeople/learned_settings.crfsuite"
then we are almost there. 
 
 4. After train sussusfully, cd back to the Gild_challange folder, make sure you have pytest installed and run. Dependencies for this script also including nltk, after install nltk, go to python shell and do ```import nltk, nltk.download()```
 
  ```
  $ cd .. 
  $ py.test -v test_name_parsing.py
  ``` 
 
 Hope everything works and my script passes all the test as on my machine! 

## How to train the module with new examples in the future (how did I do it as an example here)

 1-3 steps are same as the previous part
 
 
 4. After the test training ran successfully, label new data. In this probablepeople folder, there's raw csv called newpeople.csv. That's the new data I wanted to add. Based on the note in [probablepeople](https://github.com/datamade/probablepeople)'s page, parserator doesn't need a lot of new example to learn about the new label. This is what the data looks like in the newpeople.csv
  ```
  Molly Scott
  Steven St.Claire
  Naini Mistry
  mistry naini
  St.Claire steven
  scott molly
  stephanie scott
  scott stephsnie
  aaron david von mangum
  serena van der woodsen
  ```
To Label:
   ```
   $ parserator label newpeople.csv name_data/labeled/labeled.xml probablepeople
    ```  
Labeling example: (there's a list for tag with numbers to choose from, i.e. GivenName -2, SurName -6, please refer to labeling.txt for more details how I lable them)
   ```
   STRING: serena van der woodsen
  | serena  | GivenName |
  | van     | Surname   |
  | der     | Surname   |
  | woodsen | Surname   |
  Is this correct? (y)es / (n)o / (s)kip / (f)inish tagging / (h)elp
  n
  What is 'serena' ? If GivenName hit return
  
  What is 'van' ? If Surname hit return
  4
  What is 'der' ? If Surname hit return
  4
  What is 'woodsen' ? If Surname hit return
  6
  ```
 5. Re-train and test the performance! 
```
parserator train name_data/labeled/labeled.xml probablepeople
```

Thoughts:

 But... does this a bit arbitrary? What I did is basically telling the moudule that I want molly to be labeled as first name and scott as last name. So I mocked up a dataset with random people name and job title and test my method again. It's the test.py and test_data.csv. The AUC is about 93% 
 
  I know that my method is pretty naive and straighforward, but I tried some other NLP tools like standford NER and NLTK stuff, doesn't seem working that well and I think it has something to do with the fact that I am dealing with short content here instead of artilces/paragraphs
   
 
