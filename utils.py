def countPlots(col , plt , dataframe, sns):
    dataframe[col].value_counts()
    plt.figure(figsize=(5,6))
    sns.countplot(x=col, hue='Accident_severity', data=dataframe)
    plt.xlabel(f'{col}')
    plt.xticks(rotation=60)
    print("Plotting with :",  f'{col}')
    plt.show

