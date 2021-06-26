import java.util.Deque;
import java.util.LinkedList;

public class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new LinkedList<>();
        char[] parentheses = s.toCharArray();

        for (char parenthesis : parentheses) {
            if (parenthesis == '(' || parenthesis == '{' || parenthesis == '[') {
                stack.push(parenthesis);
            }

            if(parenthesis == ')' || parenthesis == '}' || parenthesis == ']') {
                if (stack.isEmpty()) {
                    return false;
                }

                char peekParenthesis = stack.peek();

                if(parenthesis == ')' && peekParenthesis == '(') {
                    stack.pop();
                    continue;
                }

                if (parenthesis == '}' && peekParenthesis == '{') {
                    stack.pop();
                    continue;
                }

                if(parenthesis == ']' && peekParenthesis == '[') {
                    stack.pop();
                    continue;
                }

                return false;
            }
        }

        if(stack.isEmpty()) {
            return true;
        }

        return false;
    }
}
