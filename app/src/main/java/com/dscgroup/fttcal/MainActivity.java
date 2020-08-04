// Generated at 2020-08-07T13:34:55Z with the command line:
// --path C:\Installs\Android\FftCal\app\build\generated\python\sources\debug;C:\Installs\Android\FftCal\app\build\pip\debug/common --java C:\Installs\Android\FftCal\app\build\generated\python\proxies\debug arm

package com.dscgroup.fttcal;

import android.view.View;
import android.widget.Button;

import com.chaquo.python.PyCtorMarker;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.StaticProxy;
import com.dscgroup.fftcal.R;

import static com.chaquo.python.PyObject._chaquopyCall;

@SuppressWarnings("deprecation")
public class MainActivity extends androidx.appcompat.app.AppCompatActivity implements StaticProxy {
    static {
        Python.getInstance().getModule("arm").get("MainActivity");
    }
    
    public MainActivity() {
        PyObject result;
        result = _chaquopyCall(this, "__init__");
        if (result != null) result.toJava(void.class);


    }
    
    @Override public void onCreate(android.os.Bundle arg0) {
        PyObject result;
        result = _chaquopyCall(this, "onCreate", arg0);
        if (result != null) result.toJava(void.class);


        Button btn = findViewById(R.id.btnCal);
        btn.setOnClickListener(v -> {

        });
    }
    
    public MainActivity(PyCtorMarker pcm) {}
    private PyObject _chaquopyDict;
    public PyObject _chaquopyGetDict() { return _chaquopyDict; }
    public void _chaquopySetDict(PyObject dict) { _chaquopyDict = dict; }

    public void btnCalc(View view) {
    }
}
