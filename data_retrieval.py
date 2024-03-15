from ucimlrepo import fetch_ucirepo
import pandas as pd

def fetch_uci_data(id: int):
    """
    Function to return features (X) and response variable (y) from datasets 
    from the UCI ML Repository.

    Parameters
    ----------
    id: int
        Identifying number for the dataset

    Returns
    ----------
    X: df
        Dataframe with features 
    y: array-like (n_observations,)
        Array-like object with length equal to the number of observations  
    """
    dataset = fetch_ucirepo(id=id) 

    features = pd.DataFrame(dataset.data.features)
    response = pd.DataFrame(dataset.data.targets)
    df = pd.concat([features, response], axis=1)

    # Print variable information
    print('Variable Information')
    print('--------------------')
    print(dataset.variables)

    return(df)