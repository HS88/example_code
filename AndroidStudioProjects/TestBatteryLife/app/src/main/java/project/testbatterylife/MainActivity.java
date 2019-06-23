package project.testbatterylife;

import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.BatteryManager;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.text.SimpleDateFormat;
import java.util.Date;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        IntentFilter iFilter = new IntentFilter(Intent.ACTION_BATTERY_CHANGED);
        final Intent batteryStatus = this.registerReceiver(null, iFilter);
        float battery_percentage = getBatteryPercentage( batteryStatus );
        Log.v("TAG"," Battery level at beginning " + battery_percentage);

        final Handler runDiscovery = new Handler();
        Log.v("TAG"," _+_+_+_+_=-=-=-= POSTING HANDLER =-=-=-=-=-=-=-=-=- ");
        runDiscovery.post(
                new Runnable() {
                    @Override
                    public void run() {
                        float battery_percentage = getBatteryPercentage( batteryStatus );
                        Log.v("TAG"," Battery level at beginning " + battery_percentage);
                        writeToLogFile(getDateCurrentTimeZone() + ", battery_percentage");
                        runDiscovery.postDelayed(this, 5000);
                    }
                }
        );
    }
    private void writeToLogFile(String data, String...filenames) {
        String filename = "";
        if (filenames.length == 0)
            filename = "logfile.txt";
        else
            filename = filenames[0];

        try {
            OutputStreamWriter outputStreamWriter = new OutputStreamWriter(this.openFileOutput( filename, MODE_APPEND ));
            outputStreamWriter.write(data);
            outputStreamWriter.write(Long.toString(System.currentTimeMillis()));
            outputStreamWriter.write("\n");
            outputStreamWriter.close();
        }
        catch (IOException e) {
            Log.v("Exception", "File write failed: " + e.toString());
        }
    }

    public  String getDateCurrentTimeZone(){
        try {
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
            return dateFormat.format(new Date());
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
    }

    public static int getBatteryPercentage( Intent batteryStatus ) {
        int level = batteryStatus != null ? batteryStatus.getIntExtra(BatteryManager.EXTRA_LEVEL, -1) : -1;
        int scale = batteryStatus != null ? batteryStatus.getIntExtra(BatteryManager.EXTRA_SCALE, -1) : -1;

        float batteryPct = level / (float) scale;

        return (int) (batteryPct * 100);
    }
}
