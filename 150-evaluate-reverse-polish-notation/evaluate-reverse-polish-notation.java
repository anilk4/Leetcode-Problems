class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer>st=new Stack<>();
        for(int i=0;i<tokens.length;i++){
            if(tokens[i].equals("+")){
                int x=st.pop()+st.pop();
                st.push(x);
            }
            else if(tokens[i].equals("-")){
                int a=st.pop();
                int b=st.pop();
                int x=b-a;
                st.push(x);
            }
            else if(tokens[i].equals("*")){
                int x=st.pop()*st.pop();
                st.push(x);
            }
            else if(tokens[i].equals("/")){
                int a=st.pop();
                int b=st.pop();
                int x=b/a;
                st.push(x);
            }
            else{
                st.push(Integer.parseInt(tokens[i]));
            }
            
        }
        return st.pop();
    }
}