package com.hfad.beeradvisor;

import android.app.Activity;
import android.os.Bundle;
import java.util.List;
import android.view.View;
import android.widget.Spinner;
import android.widget.TextView;

public class FindBeerActivity extends Activity {
    private BeerExpert beerExpert = new BeerExpert();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_find_beer);
    }

    //If you want a method to respond to a button click, it must be public, have a void return type, and take a single View parameter.
    public void onClickFindBeer( View view ){
        TextView brands = (TextView) findViewById(R.id.brands);
        //R is a special Java class that enables you to retrieve references to resources in your app.

        Spinner color = (Spinner) findViewById(R.id.color);
        String beerType = String.valueOf(color.getSelectedItem());
        List<String> brandsList = beerExpert.getBrands(beerType);
        StringBuilder brandsFormatted = new StringBuilder();
        for(String brand : brandsList){
            brandsFormatted.append(brand).append("\n");
        }
        brands.setText(brandsFormatted);
/*
    R.java is a special Java file that gets generated by Android Studio whenever you create or build your app.
    It lives within the app/build/generated/source/r/debug folder in your project in a package with the same name
    as the package of your app.
    Android uses R.java to keep track of the resources used within the app, and among other things
    it enables you to get references to GUI components from within your activity code.
*/
    }
}
