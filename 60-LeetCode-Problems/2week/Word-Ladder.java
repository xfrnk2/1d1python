class Solution {
    
    private Map<String, List<String>> initCases (List<String> wordList, int maxWordLength) 
    {
        Map<String, List<String>> cases = new HashMap<>();
       
        
        for (int i = 0; i < wordList.size(); i++) {
            String cur = wordList.get(i);
            for( int j =0;j<maxWordLength;j++)
        {
           String key= cur.substring(0,j)+"_"+cur.substring(j+1,maxWordLength);
            if(cases.containsKey(key))
                {
                cases.get(key).add(cur);
                }
            else
                {
                cases.put(key, new ArrayList<String>());
                 cases.get(key).add(cur);
                }
            }
        }
        System.out.println(cases);
        return cases;
    }
    
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) {
             return 0;
            }
        
        int cnt = 0;
        int maxWordLength = wordList.get(0).length();
        Map<String, List<String>> availableCases = initCases(wordList, maxWordLength);
        Queue<String> wordQueue = new LinkedList<>(); 
        HashSet<String> visited = new HashSet<>();
        wordQueue.add(beginWord);
         
        while( wordQueue.size()>0)
    {   
        int queueSize =wordQueue.size();
        cnt++;
        
        while (queueSize --> 0)
        {
          String currWord= wordQueue.poll();
          for(int i =0; i<currWord.length();i++)
          {
            List<String> nextChars= availableCases.get(currWord.substring(0,i)+"_"+currWord.substring(i+1,currWord.length()));
             System.out.println(nextChars);
            if(nextChars!=null && !nextChars.isEmpty() )
            {
                for(String s: nextChars)
                {
                    if(s.equals(endWord))
                        return cnt+1;
                    
                   if( !visited.contains(s))
                    {    
                         visited.add(s);
                         wordQueue.add(s);
                    }
                }
            }
          }
        }

    }
    return 0;
    }
}