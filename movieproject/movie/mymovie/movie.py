import os
import pandas as pd
from scipy.spatial.distance import euclidean,cosine
from movie.settings import BASE_DIR 
movie=pd.read_csv(os.path.join(BASE_DIR,"finalmovie.csv"),index_col="mid")

class movie_popular():
    #search="Popularity"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_popular.search="Popularity"
        
    
    def distance(self):
        res=min_max(movie_popular.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_popular.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_popular.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]

class movie_rated():
    #search="Rating"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_rated.search="Rating"
        
    
    def distance(self):
        res=min_max(movie_rated.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_rated.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_rated.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]
class movie_action():
    #search="Action"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_action.search="Action"
        
    
    def distance(self):
        res=min_max(movie_action.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_action.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_action.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]
class movie_drama():
    #search="Drama"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_drama.search="Drama"
        
    
    def distance(self):
        res=min_max(movie_drama.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_drama.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_drama.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]
class movie_romance():
    #search="Drama"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_romance.search="Romance"
        
    
    def distance(self):
        res=min_max(movie_romance.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_romance.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_romance.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]
class movie_crime():
    #search="Drama"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_crime.search="Crime"
        
    
    def distance(self):
        res=min_max(movie_crime.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_crime.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_crime.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]
class movie_sport():
    #search="Drama"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_sport.search="Sport"
        
    
    def distance(self):
        res=min_max(movie_sport.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_sport.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_sport.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]
class movie_mystery():
    #search="Drama"
    def __init__(self,k):
        self.k=k
        #self.search=search
        movie_mystery.search="Mystery"
        
    
    def distance(self):
        res=min_max(movie_mystery.search,self.k)
        m1=movie.loc[res[0]]
        m2=movie.loc[res[1]]
        rp_dis=euclidean(m1[1:3],m2[1:3])
        gen_dis=cosine(m1[2:],m2[2:])
        return rp_dis+gen_dis
    def similarmovie(self):
        res=min_max(movie_mystery.search,self.k)
        brother=[]
        #mid=[]
        for new_mid in res[2]:
            if res[0]!=new_mid:
                d=movie_mystery.distance(self)
                mid=new_mid
                rating=movie.loc[new_mid]['Rating']
                name=movie.loc[new_mid]['Moviename']
                brother.append((rating,name,mid))
                #mid.append(new_mid)
        brother.sort(reverse=True)
        return [(rating,name,mid) for rating,name,mid in brother[:self.k]]

def min_max(se,k):
    result=movie.nlargest(k+1,[se]).index
    maxmid=(max(result))
    minmid=(min(result))
    return maxmid,minmid,result

