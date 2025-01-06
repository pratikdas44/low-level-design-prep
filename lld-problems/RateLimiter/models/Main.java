package models;

import com.sun.jdi.IntegerType;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();

        queue.add("element 1");
        queue.add("element 2");

        String element1 = queue.poll();

        String element2 = queue.remove();
        System.out.println(element1);
        System.out.println(element2);
    }
}
