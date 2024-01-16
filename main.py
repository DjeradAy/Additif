from data_preparation import DataPreparation
from Additif import AdditifModel


csv_path = "./number of travelers.csv"
data_preparation_object = DataPreparation(csv_path)
regression_object = Regression(data_preparation_object)

# data_preparation_object.show_graph()