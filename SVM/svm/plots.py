import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures

def plotC(fracts, nDims, trials):
    plt.figure()
    domain = np.round(np.linspace(2,200,25)).astype(int)/nDims
    plt.plot(domain,fracts)
    plt.xlabel("p/N")
    plt.ylabel("C(p,N)")
    plt.title("Fraction of convergences per {} trials as a function of p".format(trials))

def plot3Dscatter(X):
    prefix = "original" if X.shape[1]<3 else "transformed"
    if X.shape[1]<3:
        Z = np.zeros((X.shape[0],1))
        X = np.hstack([X, Z])
        
    fig = plt.figure()
    ax  = Axes3D(fig)
    point_size = 1000
    colors_vec = ["red","blue","blue","red"]
    ax.scatter(list(X[:,0]), list(X[:,1]), list(X[:,2]), s=point_size, c=colors_vec)
    ax.set_zlim3d(0,2)

    plt.xlabel("x")
    plt.ylabel("y")
    ax.set_zlabel("z")
    plt.title("XOR problem {} data points".format(prefix))
    
def expand_X(X, degree_of_expansion):
    """  Perform degree-d polynomial feature expansion of X, 
        with bias but omitting interaction terms
    
    Args:
        X (np.array): data, shape (N, D).
        degree_of_expansion (int): The degree of the polynomial feature expansion.
    
    Returns:
        (np.array): Expanded data with shape (N, new_D), 
                    where new_D is D*degree_of_expansion+1
    
    """
   
    expanded_X = np.ones((X.shape[0],1))
    for idx in range(1,degree_of_expansion+1): 
        expanded_X = np.hstack((expanded_X, X**idx))
    return expanded_X

def expand_X_poly(X, degree_of_expansion):
    """  Perform degree-d polynomial feature expansion of X, 
         with bias but omitting interaction terms
    
    Args:
        X (np.array): data, shape (N, D).
        degree_of_expansion (int): The degree of the polynomial feature expansion.
    
    Returns:
        (np.array): Expanded data with shape (N, new_D), 
                    where new_D is D*degree_of_expansion+1
    
    """
    expanded_X = np.ones((X.shape[0],1))
    ### CODE HERE ###
#     for idx in range(1,degree_of_expansion+1): 
#         expanded_X = np.hstack((expanded_X, X**idx))
    poly = PolynomialFeatures(degree_of_expansion)
    expanded_X = poly.fit_transform(X)
    
    return expanded_X


'''Plotting helper for SVM exercise'''
def plot(X,Y,clf,show=True,dataOnly=False):
    
    plt.figure()
    # plot data points
    Y = Y.copy()
    Y[Y==-1] = 0
    X1 = X[Y==0]
    X2 = X[Y==1]
    Y1 = Y[Y==0]
    Y2 = Y[Y==1]
    class1 = plt.scatter(X1[:, 0], X1[:, 1], zorder=10, color="C0",
                edgecolor='k', s=20)
    class2 = plt.scatter(X2[:, 0], X2[:, 1], zorder=10, color="C1",
                edgecolor='k', s=20)
    if not dataOnly:
        # get the range of data
        x_min = X[:, 0].min()
        x_max = X[:, 0].max()
        y_min = X[:, 1].min()
        y_max = X[:, 1].max()

        # sample the data space
        XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]

        # apply the model for each point
        Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
        Z = Z.reshape(XX.shape)

        # plot the partitioned space
        plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired, shading='auto')
        
        # plot hyperplanes
        plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                    linestyles=['--', '-', '--'], levels=[-1, 0, 1], alpha=0.5)
        
        # plot support vectors
        plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
                edgecolors='g', facecolors='g', s=100, linewidth=1)
    if dataOnly:
        plt.title('Data Set')
    else:
        if clf.kernel == 'rbf':
            plt.title('Decision Boundary and Margins, C={}, gamma={} with {} kernel'.format(clf.C,clf.gamma, clf.kernel)) 
        elif clf.kernel == 'poly':
            plt.title('Decision Boundary and Margins, C={}, degree={} with {} kernel'.format(clf.C,clf.degree, clf.kernel)) 
        else:
            plt.title('Decision Boundary and Margins, C={} with {} kernel'.format(clf.C, clf.kernel)) 
        
    plt.legend((class1,class2),('Class A','Class B'),scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
    if show:
        plt.show()
        
'''Plotting helper for SVM exercise'''
def plot_expand_poly(X,Y,clf, degree=2, show=True,dataOnly=False):
    
    plt.figure()
    # plot data points
    X1 = X[Y==0]
    X2 = X[Y==1]
    Y1 = Y[Y==0]
    Y2 = Y[Y==1]
    class1 = plt.scatter(X1[:, 0], X1[:, 1], zorder=10, color="C0",
                edgecolor='k', s=20)
    class2 = plt.scatter(X2[:, 0], X2[:, 1], zorder=10, color="C1",
                edgecolor='k', s=20)
    if not dataOnly:
        # get the range of data
        x_min = X[:, 0].min() 
        x_max = X[:, 0].max() 
        y_min = X[:, 1].min() 
        y_max = X[:, 1].max() 

        # sample the data space
        XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
        
        # apply the model for each point
        Z = clf.decision_function(expand_X_poly(np.c_[XX.ravel(), YY.ravel()], degree))
        Z = Z.reshape(XX.shape)

        # plot the partitioned space
        plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired, shading='auto')
        
        # plot hyperplanes
        plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                    linestyles=['--', '-', '--'], levels=[-1, 0, 1], alpha=0.5)
        
        # plot support vectors
        plt.scatter(clf.support_vectors_[:, 1], clf.support_vectors_[:, 2],
                edgecolors='g', facecolors='g', s=100, linewidth=1)
    if dataOnly:
        plt.title('Data Set')
    else:
        if clf.kernel == 'rbf':
            plt.title('Decision Boundary and Margins, C={}, gamma={} with {} kernel'.format(clf.C,clf.gamma, clf.kernel)) 
        elif clf.kernel == 'poly':
            plt.title('Decision Boundary and Margins, C={}, degree={} with {} kernel'.format(clf.C,clf.degree, clf.kernel)) 
        elif clf.kernel == 'linear':
            plt.title('Decision Boundary and Margins, C={}, degree={} on expanded data'.format(clf.C, degree))
        else:
            plt.title('Decision Boundary and Margins, C={} with {} kernel'.format(clf.C, clf.kernel)) 
        
    plt.legend((class1,class2),('Class A','Class B'),scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
    if show:
        plt.show()
        
def plot_expand(X,Y,clf, degree=2, show=True,dataOnly=False):
    
    plt.figure()
    # plot data points
    X1 = X[Y==0]
    X2 = X[Y==1]
    Y1 = Y[Y==0]
    Y2 = Y[Y==1]
    class1 = plt.scatter(X1[:, 0], X1[:, 1], zorder=10, color="C0",
                edgecolor='k', s=20)
    class2 = plt.scatter(X2[:, 0], X2[:, 1], zorder=10, color="C1",
                edgecolor='k', s=20)
    if not dataOnly:
        # get the range of data
        x_min = X[:, 0].min() 
        x_max = X[:, 0].max() 
        y_min = X[:, 1].min() 
        y_max = X[:, 1].max() 

        # sample the data space
        XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
        
        # apply the model for each point
        Z = clf.decision_function(expand_X(np.c_[XX.ravel(), YY.ravel()], degree))
        Z = Z.reshape(XX.shape)

        # plot the partitioned space
        plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired, shading='auto')
        
        # plot hyperplanes
        plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                    linestyles=['--', '-', '--'], levels=[-1, 0, 1], alpha=0.5)
        
        # plot support vectors
        plt.scatter(clf.support_vectors_[:, 1], clf.support_vectors_[:, 2],
                edgecolors='g', facecolors='g', s=100, linewidth=1)
    if dataOnly:
        plt.title('Data Set')
    else:
        if clf.kernel == 'rbf':
            plt.title('Decision Boundary and Margins, C={}, gamma={} with {} kernel'.format(clf.C,clf.gamma, clf.kernel)) 
        elif clf.kernel == 'poly':
            plt.title('Decision Boundary and Margins, C={}, degree={} with {} kernel'.format(clf.C,clf.degree, clf.kernel))
        elif clf.kernel == 'linear':
            plt.title('Decision Boundary and Margins, C={}, degree={} on expanded data'.format(clf.C, degree))
        else:
            plt.title('Decision Boundary and Margins, C={} with {} kernel'.format(clf.C, clf.kernel)) 
        
    plt.legend((class1,class2),('Class A','Class B'),scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
    if show:
        plt.show()
        
def plot_mykernel(X,Y,clf,show=True,dataOnly=False):
    
    plt.figure()
    # plot data points
    X1 = X[Y==0]
    X2 = X[Y==1]
    Y1 = Y[Y==0]
    Y2 = Y[Y==1]
    class1 = plt.scatter(X1[:, 0], X1[:, 1], zorder=10, color="C0",
                edgecolor='k', s=20)
    class2 = plt.scatter(X2[:, 0], X2[:, 1], zorder=10, color="C1",
                edgecolor='k', s=20)
    if not dataOnly:
        # get the range of data
        x_min = X[:, 0].min() 
        x_max = X[:, 0].max() 
        y_min = X[:, 1].min() 
        y_max = X[:, 1].max() 

        # sample the data space
        XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]

        # apply the model for each point
        Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
        Z = Z.reshape(XX.shape)

        # plot the partitioned space
        plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired, shading='auto')
        
        # plot hyperplanes
        plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                    linestyles=['--', '-', '--'], levels=[-1, 0, 1], alpha=0.5)
        
        # plot support vectors
        plt.scatter(X[clf.support_][:, 0], X[clf.support_][:, 1],
                edgecolors='g', facecolors='g', s=100, linewidth=1)
    if dataOnly:
        plt.title('Data Set')
    else:
        if clf.kernel == 'rbf':
            plt.title('Decision Boundary and Margins, C={}, gamma={} with {} kernel'.format(clf.C,clf.gamma, clf.kernel)) 
        elif clf.kernel == 'poly':
            plt.title('Decision Boundary and Margins, C={}, degree={} with {} kernel'.format(clf.C,clf.degree, clf.kernel)) 
        else:
            plt.title('Decision Boundary and Margins, C={} with {} kernel'.format(clf.C, 'my_poly')) 
        
    plt.legend((class1,class2),('Class A','Class B'),scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)
    if show:
        plt.show()
   
'''Plotting Heatmap for CV results'''
def plot_cv_result_rbf(grid_val,grid_search_c,grid_search_gamma):
    plt.figure(figsize=(8,10))
    plt.imshow(grid_val)
    plt.colorbar()
    plt.xticks(np.arange(len(grid_search_gamma)), grid_search_gamma, rotation=20)
    plt.yticks(np.arange(len(grid_search_c)), grid_search_c, rotation=20)
    plt.xlabel('Gamma')
    plt.ylabel('C')
    plt.title('Val Accuracy for different Gammas and Cs')
    plt.show()

def plot_cv_result_poly(grid_val,grid_search_c,grid_search_degree):
    plt.figure(figsize=(8,10))
    plt.imshow(grid_val)
    plt.colorbar()
    plt.xticks(np.arange(len(grid_search_degree)), grid_search_degree, rotation=20)
    plt.yticks(np.arange(len(grid_search_c)), grid_search_c, rotation=20)
    plt.xlabel('Degree')
    plt.ylabel('C')
    plt.title('Val Accuracy for different Degrees and Cs')
    plt.show()


def plot_simple_data():
    #Data set
    x_neg = np.array([[2,4],[1,4],[2,3]])
    y_neg = np.array([-1,-1,-1])
    x_pos = np.array([[6,-1],[7,-1],[5,-3]])
    y_pos = np.array([1,1,1])
    x1 = np.linspace(-10,10)
    x = np.vstack((np.linspace(-10,10),np.linspace(-10,10)))

    #Parameters guessed by inspection
    w = np.array([1,-1]).reshape(-1,1)
    b = -3

    #Plot
    fig = plt.figure(figsize = (6,6))
    plt.scatter(x_neg[:,0], x_neg[:,1], marker = 'x', color = 'r', label = 'Negative -1')
    plt.scatter(x_pos[:,0], x_pos[:,1], marker = 'o', color = 'b',label = 'Positive +1')
    plt.plot(x1, x1  - 3, color = 'darkblue')
    plt.plot(x1, x1  - 7, linestyle = '--', alpha = .3, color = 'b')
    plt.plot(x1, x1  + 1, linestyle = '--', alpha = .3, color = 'r')
    plt.xlim(0,10)
    plt.ylim(-5,5)
    plt.xticks(np.arange(0, 10, step=1))
    plt.yticks(np.arange(-5, 5, step=1))

    #Lines
    plt.axvline(0, color = 'black', alpha = .5)
    plt.axhline(0,color = 'black', alpha = .5)
    plt.plot([2,6],[3,-1], linestyle = '-', color = 'darkblue', alpha = .5 )
    plt.plot([4,6],[1,1],[6,6],[1,-1], linestyle = ':', color = 'darkblue', alpha = .5 )
    plt.plot([0,1.5],[0,-1.5],[6,6],[1,-1], linestyle = ':', color = 'darkblue', alpha = .5 )

    #Annotations
    plt.annotate('$A \ (6,-1)$', xy = (5,-1), xytext = (6,-1.5))
    plt.annotate('$B \ (2,3)$', xy = (2,3), xytext = (2,3.5))#, arrowprops = {'width':.2, 'headwidth':8})
    plt.annotate('$2$', xy = (5,1.2), xytext = (5,1.2) )
    plt.annotate('$2$', xy = (6.2,.5), xytext = (6.2,.5))
    plt.annotate('$2\sqrt{2}$', xy = (4.5,-.5), xytext = (4.5,-.5))
    plt.annotate('$2\sqrt{2}$', xy = (2.5,1.5), xytext = (2.5,1.5))
    plt.annotate('$w^Tx + b = 0$', xy = (8,4.5), xytext = (8,4.5))
    plt.annotate('$(\\frac{1}{4},-\\frac{1}{4}) \\binom{x_1}{x_2}- \\frac{3}{4} = 0$', xy = (7.5,4), xytext = (7.5,4))
    plt.annotate('$\\frac{3}{\sqrt{2}}$', xy = (.5,-1), xytext = (.5,-1))

    #Labels and show
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.legend(loc = 'lower right')
    plt.show()