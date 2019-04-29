import pandas as pd
import sys

class Load_DB_full:
    def __init__(self):
        print("Loading database...")
        self.df = pd.read_csv('df_M30.csv', delimiter=';')
        print("Database loaded")
        #self.new_df = df[~df["ID"].str.contains("NaN", na=False)]
        #self.new_df = new_df[~new_df["oldID"].str.contains("NaN", na=False)]


class Load_DB:

    def __init__(self):
        print("Loading little-database...")
        self.df = pd.read_csv('df_M30_little.csv', delimiter=';')
        print("Little-Database loaded")

    def main(self):
        #km_column = self.df[['oldID']]
        #print("Getting columns")
        #km_column = self.df.iloc[0:1000,2:3]
        #print("exporting dataframe")
        #km_column.to_csv('df_M30_km.csv', sep=';')
        self.df = self.df[self.df['oldID'].str.contains('PM1.*1$')]
        self.df = self.df.loc[self.df['oldID'].str.len() == 7]
        self.df['KM'] = self.df["oldID"].str[3:5].astype(str) + "." + self.df["oldID"].str[5:6].astype(str)
        self.df.describe()


def export_csv(df):
    print("Exporting new Dataframe")
    df.to_csv('df_M30_little.csv', sep=';')
    print("Done.")

if __name__ == '__main__':

    if len(sys.argv) == 2:
        db = Load_DB_full()
        export_csv(db)
    else:
        db = Load_DB()
        db.main()
