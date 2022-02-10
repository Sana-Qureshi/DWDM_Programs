#regression of line
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def estimate_coef(x, y):
    n = np.size(x)

    m_x = np.mean(x)
    m_y = np.mean(y)

    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)

def plot_regression_line(x, y, b):

    plt.scatter(x, y, color = "g",marker = "o", s = 30)

    y_pred = b[0] + b[1]*x
    print('Mean squared error: %.2f' % mean_squared_error(x, y_pred))

    plt.plot(x, y_pred, color = "m")
    plt.title('Linnear Regression')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
def main():
    x = np.array(sorted(list(map(int,input("\nEnter X values : ").strip().split())))[:5])
    y = np.array(sorted(list(map(int,input("\nEnter Y frequency : ").strip().split())))[:5])
    # x = np.array([1, 2, 3, 4, 5])
    # y = np.array([7, 14, 15, 18, 19])

    b = estimate_coef(x, y)
    print("\nEstimated coefficients:\nb_Y-intercept = {} \nb_Slope= {}".format(b[0], b[1]))

    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()
