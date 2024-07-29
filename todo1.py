import pickle
import argparse

def main():
     
    oku=open('list.pkl','rb')
    liste1=[' ']
    liste1=pickle.load(oku)
    
    

    parser=argparse.ArgumentParser()
    
    parser.add_argument("--cumle", nargs="+", action="append",help='cumleyi yaz')
    
    parser.add_argument('-s','--silincek', default=0, type=int,help='tamamlanan elemani yaz')
    
    parser.add_argument('-l','--listall',dest='listall',help='listall')

    
    subparsers = parser.add_subparsers(help='commands')

    list_parser = subparsers.add_parser('list', help='List contents')
    list_parser.add_argument('dirname', action='store',help='Directory to list')
    
    args=parser.parse_args()
    if args.cumle!= None:
      liste= [item for sublist in args.cumle for item in sublist]
      cumle=''
      for i in liste:
        cumle =cumle+' '+ i
      
    
      if type(liste1) == str:
       liste1=liste1+cumle
       yazi=open('list.pkl','wb')
       liste2=[liste1]
       pickle.dump(liste2,yazi)

       yazi.close()
 
    
        
    
      else:
      
    
       liste1.append(cumle)
       yazi=open('list.pkl','wb')
    
       pickle.dump(liste1,yazi)

       yazi.close()
    else:  
      sül=args.silincek
      
      if sül >0:
        print(silen(sül,liste1))   
    
      
    
    
    
    
    
    

def silen(args,liste):
    liste.pop(args)
    return liste

  

     



main()






