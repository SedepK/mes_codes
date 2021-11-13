def int_prices(country, year):
    import pandas as pd
    import numpy as np
    from sklearn import linear_model as lm
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    df = pd.read_csv("C:/Users/Sedep/Desktop/internet_prices.csv")
    df_countr = df[(df['Country'] == country)]
    df_drop = df_countr.drop(['City', 'Region', 'Country'], axis=1)
    df_list = df_drop.columns.tolist()
    for j in range(0, 10):  # убрали нули из дф, чтоб не влияло на подсчет сред ариф
        count = 0
        for i in df_drop.values:
            count += i[j]
        if count == 0:
            df_drop = df_drop.drop(df_drop.columns[j], 1)
    df2 = []
    for i in df_drop:
        mass = []
        for j in i:
            if j.isdigit():
                mass.append(j)
        df2.append(int(''.join(mass)))
    df_aver = df_drop.sum() / df_drop.where(df_drop > 0).count()  # сред ариф без учета нулей, это наш У
    reg = lm.LinearRegression()
    reg.fit(np.array(df2).reshape(-1, 1), df_aver)
    print(reg.coef_)
    print(reg.predict([[year]])[0])
int_prices('Brazil', 2045)

