# Importing libraries
import numpy as np

# Creating ErrorCalculator class
class ErrorCalculator:

    # Assigning values to object properties
    def __init__(self, residuals, standard_res, mse, rmse, y, y_pred):
        self.residuals = residuals
        self.standard_res = standard_res
        self.mse = mse
        self.rmse = rmse
        self.y = np.array(y)
        self.y_pred = np.array(y_pred)

    # Method to compute the residuals
    def get_residuals(self):
        self.residuals = self.y - self.y_pred
        return self.residuals

    # Method to compute the standard residuals
    def get_standardised_residuals(self):
        self.standard_res = (self.y - self.y_pred) / (self.y_pred)**0.5
        return self.standard_res

    # Method to compute the Mean Squared Error
    def get_mse(self):
        self.mse = mse(self.y, self.y_pred)
        return self.mse

    # Method to compute the Root Mean Squared Error
    def get_rmse(self):
        self.rmse = mse(self.y, self.y_pred, squared=False)
        return self.rmse

    # Method that prints the average, minimum and maximum of the
    # standardised residuals, as well as the MSE and RMSE.
    def error_summary(self):

        print(f'the average standard residual: {standard_res.mean()}')
        print(f'the minimum standard residual: {min(standard_res)}')
        print(f'the maximum standard residual: {max(standard_res)}')
        print(f'The Root Mean Squared Error: {rmse}')
        print(f'The Root Mean Squared Error: {mse}')

# Creating Plotter class
class Plotter(ErrorCalculator):

    def plot(self):
        plt.hist(self.residuals)
        plt.title('Distribution of residuals')
        plt.xlabel('Residuals')
        plt.ylabel('Distribution')
        plt.show()
        return plt.show()

# Creating HistogramPlotter class
class HistogramPlotter(Plotter):

    Plotter.plot()
    super()

# Creating ScatterPlotter class
class ScatterPlotter(Plotter):
    def scatter(self):
        plt.scatter(self.y_pred, self.residuals)
        plt.xlabel('Observed values')
        plt.ylabel('predicted values')
        plt.title('Observed values vs predicted values')
    super()