#Q7 implement BernoulliNb and MultinomialNB

class myBernoulliNB:
    def __init__(self):
        self.is_fit=False
        
        pass
    #input: X:td-array, y:classes 
    def fit(self,X,y):
        self.class_count=dict()
        self.prior=dict()
        for c in y:
            if c in self.class_count:
                self.class_count[c]=self.class_count[c]+1
            else:
                self.class_count[c]=1

        self.N=len(X)
        
        for key in self.class_count:
            self.prior[key]=self.class_count[key]/self.N
        #for each vocabulary
        self.condprob=np.zeros([len(X[0]),len(self.class_count)])
        for i in range(len(X[0]):
            for key in self.class_count:
                Nc=self.class_count[key]
                # i is the vocabuler, key is the class number
                Nct=0
                for j range(self.N):
                    if y[j]==key and X[j][i]!=0:
                        Nct+=1
                
                self.condprob[t][key]=(Nct+1)/(Nc+2)
        pass
    #input X: a singe document TD vector
    def predict_prob_log(self,X):
        if not self.is_fit:
            print("fit before predict")
            return None
        score=[]
        
        for key in self.class_count:
            score[c]=np.log(self.prior[key])
            for i in range(len(X)):
                if X[i]==0:
                    score[c]+=np.log(1-self.condprob[i][c])
                else:
                    score[c]+=np.log(self.condprob[i][c])
        return score
        pass
    pass
class myMultinomialNB:
    def __init__(self):
        self.is_fit=False

        pass
    def fit(self,X,y):
        self.class_count=dict()
        self.prior=dict()
        for c in y:
            if c in self.class_count:
                self.class_count[c]=self.class_count[c]+1
            else:
                self.class_count[c]=1

        self.N=len(X)
        
        for key in self.class_count:
            self.prior[key]=self.class_count[key]/self.N
        #for each vocabulary
        self.condprob=np.zeros([len(X[0]),len(self.class_count)])
        
        for key in self.class_count:
            Nc=self.class_count[key]
            
            Nctt=0
            for j in range(self.N):
                if y[j]==key:
                    Nctt+=np.sum(X[j])
            for i in range(len(X[0]):
                # i is the vocabuler, key is the class number
                Nct=0
                for j range(self.N):
                    if y[j]==key and X[j][i]!=0:
                        Nct+=X[j][i]
                
                self.condprob[t][key]=(Nct+1)/(Nctt+len(X[0]))
        pass
    
    def predict_prob_log(self,X):
        if not self.is_fit:
            print("fit before predict")
            return None
        score=[]
        
        for key in self.class_count:
            score[c]=np.log(self.prior[key])
            for i in range(len(X)):
                if X[i]==0:
                    score[c]+=np.log(1-self.condprob[i][c])
                else:
                    score[c]+=np.log(self.condprob[i][c])
        return score
        pass
    pass

docs=["chinese beijing chineses","chinese chinese shanghai","chinese macao","tokyo japan chinese"]
c=[1,1,1,0]
vectorizer = CountVectorizer(input='content')
vectorizer.fit(docs)
print(vectorizer)
