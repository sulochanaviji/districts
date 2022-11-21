#import sys
import pandas

class districts:
    def __init__(self,State='',District='',Area='',Pincode=''):
        self.State = State
        self.District = District
        self.Area = Area
        self.Pincode = Pincode
        print(self.get_districts())
    def get_districts(self):
        val= pandas.read_csv('Tamilnadu.csv')
        dis_val=pandas.DataFrame(val)
        search_val = self.State+self.District+self.Area+self.Pincode
        dis_val.groupby(['State','District']).apply(','.join)
        dis_val['con_cols'] = dis_val['State'].map(str) + dis_val['District'].map(str) + dis_val['Area'].map(str) + dis_val['Pincode'].map(str)
        #print(dis_val)
        #print(search_val)
        search_val= search_val.upper()
        dis_val['con_cols'] = dis_val['con_cols'].str.upper()
        dis_contains_val = dis_val.loc[dis_val['con_cols'].str.contains(search_val)==True]
        if len(dis_contains_val)>0:
            dis_contains_val=dis_contains_val.drop(['con_cols'],axis=1)
        
        return dis_contains_val

if __name__ == '__main__':
    d = districts('Tamilnadu','villupuram','Gingee')
    #print(d.get_districts())

