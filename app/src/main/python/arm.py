from android.os import Bundle
from androidx.appcompat.app import AppCompatActivity  
from android.view import View
from com.dscgroup.fftcal import R
from java import jvoid, Override, static_proxy
import numpy as np
import os, json
# import sys
from numpy import cos, pi, random, floor, angle 
# import android
from android.widget import Toast
from androidx.core.app import NotificationCompat

from android.content import Context



class MainActivity(static_proxy(AppCompatActivity, View.OnClickListener)):

    @Override(jvoid, [Bundle])
    def onCreate(self, state):
        self.getSystemService(Context.NOTIFICATION_SERVICE).cancelAll()
    
        AppCompatActivity.onCreate(self, state)
        self.setContentView(R.layout.activity_main)

        ab = np.zeros((3,4))

        self.findViewById(R.id.btnCal).setOnClickListener(self)

        self.working = False
        self.findViewById(R.id.txtRes).setText("Res2"+str(ab))


    @Override(jvoid, [View])
    def onClick(self, v):
    
        if self.working:
            Toast.makeText(self, 'Plz Wait...',  Toast.LENGTH_SHORT).show()
            return None
            
        self.working = True
        
        Toast.makeText(self, 'FftCal will save outputs in your storage',  Toast.LENGTH_LONG).show()


        mdir = os.environ['EXTERNAL_STORAGE']+ '/FftCal/'
        
        if not os.path.exists(mdir):
            os.makedirs(mdir)
        
        t = np.arange(0.0, 105.0001, 0.01)
        Fs = 1/(t[1] - t[0]);
        
        
        
        if os.path.isfile(mdir + 'input.csv'):
            S = np.loadtxt(mdir + 'input.csv') 
        else:
            S = 10*cos(2*pi*25*t+pi/6)+5*cos(2*pi*50*t+pi/8)+2*cos(2*pi*75*t+pi/3)+1*cos(2*pi*8*t+pi/7)+1.5*cos(2*pi*35*t+pi/5);
            
        print('S.shape', S.shape)
        
        
        
        [freq, xdft, psdx, phase, complexx] = Mide_FFT_PSD(S, Fs)
        
        np.savetxt(mdir + 'freq_xdft_psdx_phase.csv', np.column_stack((freq, xdft, psdx, phase )), delimiter=',')
        np.savetxt(mdir + 'input_fft.csv', np.column_stack((S, complexx)), delimiter=',')
        
        self.working = False

        
        
 
def Mide_FFT_PSD(S, Fs): 

    N = len(S); 

    freq = np.arange(0, Fs/2, Fs/(len(S)))
    
    xdft = np.fft.fft(S);
    complexx = xdft;
    xdft = xdft[:int(floor(N/2))]
    
    psdx = (1/(Fs*N)) * abs(xdft) ** 2
    psdx[:-1] = 2*psdx[:-1]
   
   
    phase = (angle(xdft));
    phase= (pi/2)-phase;

    xdft = abs(xdft);
    
    
    if len(freq) != len(xdft):
        freq = freq[:len(xdft)]
    
    return [freq, xdft, psdx, phase,complexx]