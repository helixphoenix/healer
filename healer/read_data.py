from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String,create_engine
import re
from top_ten import top_ten_check



Base = declarative_base()
class Practices(Base):
     __tablename__ = 'pdpic'
     id = Column(Integer, primary_key=True)
     bnf_code = Column(String)
     practice = Column(String)
     quantity=Column(String)
     def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.bnf_code, self.practice)

class Chemicals(Base):
     __tablename__ = 'chemc'
     chem_sub = Column(Integer, primary_key=True)
     name = Column(String)
     def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.chem_sub, self.name)      
class Addresses(Base):
     __tablename__ = 'addrc'
     id = Column(Integer, primary_key=True)
     practice_code = Column(String)
     practice_name = Column(String)
     def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.practice_code, self.practice_name)      



def chemical_query(chemical_names):
   results={'paracetamol':[],'melatonin':[], 'prednisolone':[]}
   engine = create_engine('postgresql://developer:secret@localhost:5432/postgres')
   Session = sessionmaker(bind=engine)
   session=Session() 
   for chemical in chemical_names:
      if chemical == 'paracetamol':
         para_res=session.query(Chemicals.chem_sub).filter(Chemicals.name.like('%Paracetamol%'))
         for row in para_res:    
            # print("reading paracetomol's bnf codes:",row)
            results[chemical].append(row)
      else:
            if chemical=='melatonin':
               chem_res=session.query(Chemicals.chem_sub).filter(Chemicals.name=='Melatonin')
               for row in chem_res:    
                  # print("reading melatonin' bnf codes:",row)
                  results[chemical].append(row)
            if chemical=='prednisolone':
               chem_res=session.query(Chemicals.chem_sub).filter(Chemicals.name=='Prednisolone')
               for row in chem_res:    
                  # print("reading prednisolone' bnf codes:",row)
                  results[chemical].append(row)
   return results         



def quantity_query(bnf_codes):
   engine = create_engine('postgresql://developer:secret@localhost:5432/postgres')
   Session = sessionmaker(bind=engine)
   session=Session()     
   for chemical,bnf_code in bnf_codes.items():
         for code in bnf_code:
               code_str=str(code) 
               codi=code_str.replace("(","").replace(")","").replace("'","").replace(",","")
               code_like='%'+codi+'%'
               result=session.query(Practices.practice,Practices.quantity).filter(Practices.bnf_code.like(code_like))  
               for row in result:    
                  # print("reading practice codes and quantity:",row)
                  
                  bnf_codes[chemical].append(row)  
   return bnf_codes         
 
 
    
def read_quantity_data(chemical_names):
    chem_codes=chemical_query(chemical_names)
    quantity_info=quantity_query(chem_codes)
    return quantity_info   
 
 
 
       
def query_top_ten_names(quantity_info):
   practices={'paracetamol':[],'melatonin':[], 'prednisolone':[]}    
   engine = create_engine('postgresql://developer:secret@localhost:5432/postgres')
   Session = sessionmaker(bind=engine)
   session=Session()   
   for chemical, value in quantity_info.items():
      for val in value: 
         if len(val)>1:  
            for top_ten in val: 
               code_str=str(top_ten[0]) 
               codi=code_str.replace("(","").replace(")","").replace("'","").replace(",","")  
               code_like='%'+codi+'%'
               result=session.query(Addresses.practice_name).filter(Addresses.practice_code.like(code_like))
               for row in result:
                  practices[chemical].append([row,codi,value[0],top_ten[1]])
                  
   # print(practices)   
   return practices   

          
def read_data(chemical_names):
   top_ten_practices={'paracetamol':[],'melatonin':[], 'prednisolone':[]}    
   quantity_info=read_quantity_data(chemical_names) 
   top_ten=top_ten_check(quantity_info)
   top_ten_names=query_top_ten_names(top_ten) 
   for chemical,values in top_ten_names.items():
      for practice in values:
         message=f"{practice[0]}({practice[1]}) prescribed {chemical}({practice[2]}) a total of {practice[3]} times"     
         print(message)
         top_ten_practices[chemical].append(message) 
   return top_ten_practices             
      
 
