import java.util.*;

class Solution02 {
    public String removeDuplicateLetters(String s) {
        Set<Character> hashSet = new HashSet<>();
        Map<Character, Integer> counter = new HashMap<>();
        Deque<Character> stack = new LinkedList<>();

        for (char c : s.toCharArray()) {
            counter.putIfAbsent(c, 0);
            counter.computeIfPresent(c, (key, value) -> value + 1);
        }


        for (char c : s.toCharArray()) {
            counter.put(c, counter.get(c) - 1);

            if(hashSet.contains(c)) {
                continue;
            }

            while (!stack.isEmpty() && c < stack.peek() && counter.get(stack.peek()) > 0) {
                hashSet.remove(stack.pop());
            }

            stack.push(c);
            hashSet.add(c);
        }

        String result = "";

        while (!stack.isEmpty()) {
            result =  stack.pop() + result;
        }

        return result;
    }
}

