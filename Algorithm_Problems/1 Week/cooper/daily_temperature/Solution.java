import java.util.Deque;
import java.util.LinkedList;

public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] result = new int[temperatures.length];
        Deque<WeatherInfo> stack = new LinkedList<>();

        int dayIndex = 0;

        for (Integer temperature : temperatures) {
            WeatherInfo currentWeatherInfo = new WeatherInfo(temperature, dayIndex);

            while (!stack.isEmpty() && currentWeatherInfo.isWarmerThan(stack.peek())) {
                WeatherInfo poppedInfo = stack.pop();
                result[poppedInfo.getDay()] = dayIndex - poppedInfo.getDay();
            }

            stack.push(currentWeatherInfo);
            dayIndex++;
        }

        while (!stack.isEmpty()) {
            int restInfoDay = stack.pop().getDay();
            result[restInfoDay] = 0;
        }

        return result;
    }
}

class WeatherInfo {
    private int temperature;
    private int day;

    public WeatherInfo(int temperature, int day) {
        this.temperature = temperature;
        this.day = day;
    }

    public int getDay() {
        return day;
    }

    public boolean isWarmerThan(WeatherInfo other) {
        return this.temperature > other.temperature;
    }
}

