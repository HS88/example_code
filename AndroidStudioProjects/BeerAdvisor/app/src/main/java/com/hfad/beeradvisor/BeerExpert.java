package com.hfad.beeradvisor;

/**
 * Created by harmeet-US on 1/30/2018.
 */
import java.util.ArrayList;
import java.util.List;

public class BeerExpert {
    List<String> getBrands(String color)
    {
        List<String> brands = new ArrayList<>();
        if( color.equals("amber")){brands.add("Amber 1");brands.add("Amber 2");}
        else
            {
                brands.add("Extra 1");
                brands.add("Extra 2");
            }
        return brands;
    }
}
