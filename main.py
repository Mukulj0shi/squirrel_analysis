import pandas

with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as sqrl_data:
    data = pandas.read_csv(sqrl_data)  # DataFrame
    fur_color = data["Primary Fur Color"]  # DataSeries
    # print(fur_color_list)
    fur_gray = data[fur_color == "Gray"]
    print(len(fur_gray))
    fur_cinnamon = data[fur_color == "Cinnamon"]
    fur_black = data[fur_color == "Black"]
    fur_color_dict = dict(color=["Gray", "Cinnamon", "Black"],
                          total_squ=[len(fur_gray), len(fur_cinnamon), len(fur_black)])
    # Creating a data frame
    my_dataframe = pandas.DataFrame(fur_color_dict)
    my_dataframe.to_csv("Squirrel_count_analysis.csv")
