
import numpy as np
import matplotlib.pyplot as plt 

import math
pi=math.pi

from typing import Tuple


class demo:
    """Demonstration of the central limit theorem."""

    def __init__(
        self,
        n_sample: int,
        n_shot: int,
    ):
        self.n_sample = n_sample
        self.n_shot = n_shot

    def roll_dice(self,)->np.ndarray:

        """Return a n_sample*n_shot matrix .
        
        Return:
            __ : n_sample*n_shot ndarray.
        """

        return 1+np.random.randint(6, size=(self.n_sample, self.n_shot)) 

    def show_histogram(
        self,
    ) ->plt.plot:

        mat=self.roll_dice()
        vec=mat.sum(axis=0)/self.n_sample
        
        n_bins=20*self.n_sample
        f=15
        r=10

        fig= plt.plot(figsize=(r,r))
        counts, bins = np.histogram(vec,bins=n_bins)
        dx=bins[1]-bins[0]
        plt.hist(bins[:-1], bins, weights=counts/(self.n_shot))
        
        p=np.arange(1,7)
        value=p.sum()/6
        std=np.sum((p-value)**2)/6
     
        x=0.1*np.arange(1000)
        plt.plot(x,np.max(counts/(self.n_shot))*np.exp(-(x-value)**2/(2*std/self.n_sample)),'b-',linewidth=1)
        #plt.plot(x,(dx/np.sqrt(2*pi*std/self.n_sample))*np.exp(-(x-value)**2/(2*std/self.n_sample)),'b-',linewidth=1)
        
        plt.xlim(bins[0]-.5,bins[-1]+.5)
        plt.xlabel(r"mean value", fontsize=f)
        plt.ylabel(r"frequency", fontsize=f)
        plt.tick_params(labelsize=f)
        plt.title(rf"number of dice$={self.n_sample}$, number of shots$={self.n_shot}$")
        plt.tight_layout()
        plt.show()

        return None


# サイコロ$n$回ふって平均を取ることを繰り返した時の頻度の分布（＝確率）を描いてみる
# 
# $n$が大きいと分布は平均が$\mu=\sum_i\frac{i}{6}=\frac{7}{2}$, 分散が$\sigma=\sqrt{\sum_i\frac{(i-\mu)^2}{6}\frac{1}{n}}=\sqrt{\frac{35}{12}\frac{1}{n}}$の正規分布に一致する
# 
# サンプル数$n$の√で分散(=誤差)が小さくなることを覚えておきましょう

# サイコロを1回振ることを1000回繰り返した時

demo(1,1000).show_histogram()



# サイコロを２回振ることを1000回繰り返した時

demo(2,1000).show_histogram()


# サイコロを４回振ることを1000回繰り返した時


demo(4,1000).show_histogram()


# サイコロを１０回振ることを1000回繰り返した時

demo(10,10000).show_histogram()


