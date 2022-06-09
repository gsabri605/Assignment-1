#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
* 
'hello'
-87.8
- 
()
+	
6 


Ans: *,-,+,/ this are expressions
     'hello', this is a string
      -87.8,6 this is  a integer


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')


Ans: String is a sequence of character and variable is single character which stores memory location for storing values.


# In[ ]:


3. Describe three different data types.

Ans:   Integer

       Float
       
       String
       
       Integer:  This value is repesented by "int" it contain positive or negative whole number. In python their is no limit to how long an integer can be.
       
       Float:    This value is represented by "folat" it is specified by a decimal point.
       
       String:   This value is represented by "str" A string is a sequence of character put in single or double quote


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Ans:  An expression is made up of operators and operands.
      
      All expression perform some operation depends on operators.
    


# In[ ]:


get_ipython().set_next_input('5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Ans:  Statement respresent an action or command 
      
      eg spam=10
      
      Expression is a combination of variables , operations and value that gives a result.
      
      


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1

Ans:   After running the following code

       The variable bacon contain    23


# In[3]:


bacon=22
bacon+1


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' * 3


Ans:  'spamspamspam' 


# In[4]:


'spam'+'spamspam'
'spam'*3


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Ans:  because variable cannot start with number thats why 100 is invalid and eggs is valid varible.


# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')

Ans : 
       
       int is used to get integer value
       
       float is used to get floatin-point number
       
       str is used to get string value 


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'

Ans :  
       This expression cause an error because 99 is integer so string and integer cannot concatenate.
         
         
       We need to convert integer value in to string then it will fix an error.
      


# In[5]:


'I have eaten '+99+'burritos'


# In[6]:


'I have eaten'+str(99)+'burritos'


# In[ ]:




