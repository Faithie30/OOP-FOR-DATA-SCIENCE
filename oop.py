# Importing libraries
import numpy as np

# Creating ErrorCalculator class
class ErrorCalculator:

    # Assigning values to object properties
    def __init__(self, resid, stand_res, mse, rmse, y, y_pred):
        self.resid = resid
        self.stand_res = stand_res
        self.mse = mse
        self.rmse = rmse
        self.y = np.array(y)
        self.y_pred = np.array(y_pred)

    # Method to compute the residuals
    def get_residuals(self):
        self.resid = self.y - self.y_pred
        return self.resid

    # Method to compute the standard residuals
    def get_standardised_residuals(self):
        self.stand_res = (self.y - self.y_pred) / (self.y_pred)**0.5
        return self.stand_res

    # Method to compute the Mean Squared Error
    def get_mse(self):
        self.mse = mse(self.y, self.y_pred)
        return self.mse

    # Method to compute the Root Mean Squared Error
    def get_rmse(self):
        self.rmse = mse(self.y, self.y_pred, squared=False)
        return self.rmse

    def error_summary(self):
        stand_resid_min = min(self.stand_res)
        stand_resid_max = max(self.stand_res)
        rmse_min = min(self.rmse)
        rmse_max = max(self.rmse)
        mse_min = min(self.mse)
        mse_max = max(self.mse)
        print(f'standard residual: {stand_resid_min}')
        print(f'standard residual: {stand_resid_max}')
        print(f'min rmse: {rmse_min}')
        print(f'max rmse: {rmse_max}')
        print(f'min mse: {mse_min}')
        print(f'max mse: {mse_max}')


class Plotter(ErrorCalculator):

    def plot(self):
        plt.hist(self.resid)
        plt.title('The distribution of residuals')
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        plt.show()
        return plt.show()


class HistogramPlotter(Plotter):

    Plotter.plot()
    super()


class ScatterPlotter(Plotter):
    def scatter(self):
        plt.scatter(self.y_pred, self.resid)
        plt.xlabel('Observed values')
        plt.ylabel('predicted values')
        plt.title('Observed values vs predicted values')
    super()
