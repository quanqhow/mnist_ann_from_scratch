#!/usr/bin/env python3
import numpy as np

sd=np.random.randint(500)
print(sd)
np.random.seed(sd)

class neural_net:
	def __init__(self, nrons):
		self.nrons = nrons
		self.weights=[]
		self.bias=[]
		for i in range(len(self.nrons)-1):
			self.weights.append(2*np.random.rand(self.nrons[i],self.nrons[i+1])-1)
			self.bias.append(2*np.random.rand(1,self.nrons[i+1])-1)

	def __str__(self):
		return str(self.__dict__)

	def sigmoid(self,x):
		return 1.0/(1+np.exp(-x))

	def sigmoid_der(self,x):
		return x * (1 - x)

	def feed_forward(self, X):
		self.X = X.reshape(1,self.nrons[0])
		self.a = [self.X]						# (1,784)
		for i in range(len(self.nrons)-1):
			z = (np.dot(self.a[i] ,self.weights[i])+self.bias[i])	# w0(784,20) w1(20,20) w2(20,10)
			self.a.append(self.sigmoid(z))		# a0(1,784) a1(1,20) a2(1,20) b
		return self.a[-1]					# a3(1,10)

	def backprop(self, y):
		self.y = y 								# (1,10)
		d_c_out= 2*(self.y-self.a[3])

		d_c_z2 = d_c_out*self.sigmoid_der(self.a[3])# (1,10)
		d_c_b2 = d_c_z2								# (1,10)
		d_c_w2 = np.dot(self.a[2].T, d_c_z2)		# (20,10)
		d_c_a2 = np.dot(d_c_z2, self.weights[2].T)			# (1,20)
		
		d_c_z1 = d_c_a2*self.sigmoid_der(self.a[2])	# (1,20)
		d_c_b1 = d_c_z1								# (1,20)
		d_c_w1 = np.dot(self.a[1].T, d_c_z1)		# (20,20)
		d_c_a1 = np.dot(d_c_z1, self.weights[1].T)			# (1,20)
		
		d_c_z0 = d_c_a1*self.sigmoid_der(self.a[1])	# (1,20)
		d_c_b0 = d_c_z0								# (1,20)
		d_c_w0 = np.dot(self.a[0].T, d_c_z0)		# (784,20)

		self.weights[0]+=d_c_w0
		self.bias[0]+=d_c_b0
		self.weights[1]+=d_c_w1
		self.bias[1]+=d_c_b1
		self.weights[2]+=d_c_w2
		self.bias[2]+=d_c_b2