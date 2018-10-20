import numpy as np 
import scipy.io
from sklearn.preprocessing import normalize
from sklearn.datasets import fetch_lfw_people

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

image_data = lfw_people.images #3D matrix
no_of_sample, height, width = lfw_people.images.shape

data = lfw_people.data
labels = lfw_people.target


'''
Normalising the following matrix
'''
sk_norm = normalize(data, axis=0)
norm_matrix = (data-np.mean(data, axis=0))/np.var(data, axis=0)

matrix = sk_norm


'''
PCA
'''
cov_matrix = matrix.T.dot(matrix)/(matrix.shape[0])
values, vectors = np.linalg.eig(cov_matrix)

red_dim = 1000
pca_vectors = vectors[:, :red_dim]

eigen_faces = matrix.dot(pca_vectors) #obtain our eigen faces






# cv2.imshow('original image', img)
# cv2.imshow('grey', grey_img)

