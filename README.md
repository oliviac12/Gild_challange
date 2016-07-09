## Gild_challange

I was able to pass all the test in the test set. I was using this moudule called [probablepeople](https://github.com/datamade/probablepeople) becasue it uses uses [parserator](https://github.com/datamade/parserator), a library for making and improving probabilistic parsers - specifically, parsers that use python-crfsuite's implementation of conditional random fields.Therefore, I was able to customize and added more example and train the moudule. 
**However, the train function in the most updated version of probablepeople is broken, so in order to get what I got, please bare with me and do the following step set up the moudule.**

## How to set up probablepeople and train the new examples

 1. In the terminal, git clone, and set it to this specific commit number 6cb9f7ecc6d77496c580359cb63dd38ddfab3ae9
   
    ```
   git clone https://github.com/datamade/probablepeople.git
   cd probablepeople
   git reset --hard 6cb9f7ecc6d77496c580359cb63dd38ddfab3ae9
   pip install -r requirements.txt  
   python setup.py develop
    ```  
 
 2. Another thing need to be fixed: downgrade the parserator to version 0.4.1 because the parserator installed with probablepepople is  5.0+  only that specific commit number probablepeople and 0.4.1 parserator together works (ugh I know!) 
    ```
   pip unintall parserator
   pip intall parserator==0.4.1
    ```  

 3. Do a test train
   ```
   parserator train name_data/labeled/labeled.xml,name_data/labeled/company_labeled.xml probablepeople
    ```  
if no error pops up and you see something like this 
"training model on 2078 training examples from ['name_data/labeled/labeled.xml']"
"done training! model file created: probablepeople/learned_settings.crfsuite"
then we are half way there!

 4. Label new data. In this Gild_challengage folder, there's raw csv called newpeople.csv. Copy paste it to the probablepeople folder. That's the new data we want to add. Based on the note in [probablepeople](https://github.com/datamade/probablepeople)'s page, parserator doesn't need a lot of new example to learn about the new label. This is what the data looks like in the newpeople.csv
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
   parserator label newpeople.csv name_data/labeled/labeled.xml probablepeople
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
 5. Re-train and use it! 
```
train name_data/labeled/labeled.xml probablepeople
```
After train sussusfully, cd back to the Gild_challange folder, make sure you have pytest installed and run 
```
py.test -v test_name_parsing.py
```


 6. But... does this a bit arbitrary? What I did is basically telling the moudule that I want molly to be labeled as first name and scott as last name. I mock up a dataset with random people name and job title and test my method again. 
