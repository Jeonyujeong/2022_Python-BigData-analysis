import pandas as pd

def get_gradDf(path):
    raw_df = pd.read_excel( path, sheet_name=0 )

    use_cols = ['지역', '정보공시 \n 학교코드', '학교명', '졸업자.2',
                '(특수목적고)과학고 진학자.2', '(특수목적고)외고ㆍ국제고 진학자.2']

    raw_df2 = raw_df[ use_cols ]
    raw_df2.columns = ['local', 'code', 'sch_name', 'grad_N', 'sci_N', 'fI_N']
    raw_df3 = raw_df2.drop(0)

    raw_df4 = raw_df3.dropna().copy()
    raw_df4['grad_N'] = pd.to_numeric( raw_df4['grad_N'] )
    raw_df4['sci_N'] = pd.to_numeric( raw_df4['sci_N'] )
    raw_df4['fI_N'] = pd.to_numeric( raw_df4['fI_N'] )

    raw_df5 = raw_df4.reset_index(drop=True)
    
    return raw_df5


def get_dustDf( path, local):
    dust_df = pd.read_excel(path)
    dust_df.columns = ['date', 'local', 'NO2', 'O3', 'CO2', 'SO2', 'dust', 'm_dust']
    dust_df2 = dust_df[ dust_df['local']==local ]
    dust_df2.index = pd.to_datetime( dust_df2['date'].apply(str) )
    return dust_df2