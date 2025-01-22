class Central_tendencies:
    def __int__(self,data:list):
        self.data=data
    def  mean(self):
        """ Calculates the average of the data
            formula:
            mean=(sum of observation)/(no of observations)
        """
        mean=(sum(self.data))/len(self.data)
        return mean

    def Median(self):
        """
        Find the median of the given data
        process:
        - Arrange the data in ascending order
        - if total observations are even:
                - median =(((n/2)+((n/2)+1))the values)/2
        - if total observations are odd:
                - median =(n+1)/2 th value
        """
        ordered_data=sorted(self.data)
        n=len(ordered_data)
        if n%2==0:
            mid=(ordered_data[n//2]+ordered_data[(n//2)+1])/2
        else:
            mid=ordered_data[(n+1)//2]
        return mid
    def mode(self):
        """
        the frequently repeated data is called.
        It can by finding the frequencies of each element in the data and then giving out high frequency data
        :return:
        """
        frequencies={}
        for i in self.data:
            if i in frequencies:
                frequencies[i]+=1
            else:
                frequencies[i]=1
        mode=[]
        high_freq=max(frequencies)





