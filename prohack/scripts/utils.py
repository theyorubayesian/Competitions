def summarize(data, n_unique=True, missing=True, dtype=True, max_value=True, min_alue=True, sort_by=None):
    # create a dictionary of chosen statistics
    columns={"n_unique": n_unique,
               "missing": missing,
               "dtypes": dtype
              }
    # create a dataframe of all statistics
    temp = pd.DataFrame({"n_unique": data.nunique(),
                        "missing": round(100 * data.isnull().sum() / data.shape[0]),
                        "dtypes": data.dtypes})
    temp.loc[:, "missing"] = temp.missing.apply(lambda x: str(x) + "%")
    # drop any statistics set to false
    for col in columns:
        if not columns[col]:
            temp.drop(col, axis=1, inplace=True)
    return temp

def calculate_residuals(ytrue, ypred):
    return ytrue - ypred 

def plot_residuals(ypred, residuals):
    f, axes = plt.subplots(1, 2, figsize=(20, 5))
    sns.scatterplot(x=ypred, y=residuals, ax=axes[0])
    sns.distplot(residuals, ax=axes[1])
    axes[0].set_title("Scatterplot of Residuals")
    axes[1].set_title("Distribution plot of Residuals")
    plt.show()
    
def plot_by_galaxy(data, column):
    galaxy_groups = data.groupby("galaxy")
    
    f, axes = plt.subplots(21, 9, figsize=(20, 50))
    for i, (name, group) in enumerate(galaxy_groups):
        #print(name)
        sns.distplot(group[column], ax=axes[i//9, i%9])
        axes[i//9, i%9].set_title(name)
    f.tight_layout()  # so that subplot titles will not overlap 
    plt.show()