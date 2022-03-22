class Solution {
    public String frequencySort(String s) {
        
        
        HashMap<Character, Integer > cntr = new HashMap<>();

	for ( char c: s.toCharArray()) {

		cntr.put( c, cntr.getOrDefault(c,0) +1);
	}

	PriorityQueue<Character> heap = new PriorityQueue<>((a, b) -> (cntr.get(b) - cntr.get(a)));

	heap.addAll(cntr.keySet());

	StringBuilder sb = new StringBuilder();

	while (!heap.isEmpty()) {
		char c = heap.poll();
		for (int i =0 ; i < cntr.get(c) ; i++){
			sb.append(c);
		}
	}
	return sb.toString();
    }
}