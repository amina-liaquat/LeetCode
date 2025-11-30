import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        HashMap<Integer, List<Integer>> unique_map = new HashMap<>();
        HashMap<Integer, List<Integer>> dup_map = new HashMap<>();
        ArrayList<List<Integer>> main_list = new ArrayList<>();
        HashSet<String> seen = new HashSet<>();

        // Step 1: Build two maps: one for unique values, one for duplicates
        for (int i = 0; i < n; i++) {
            int val = nums[i];
            unique_map.computeIfAbsent(val, k -> new ArrayList<>()).add(i);

            if (unique_map.get(val).size() > 1) {
                dup_map.put(val, unique_map.get(val));
            }
        }

        // Special case: only [0, 0, 0] exists
        if (unique_map.size() == 1 && dup_map.size() == 1 && unique_map.containsKey(0)) {
            List<Integer> zero_indices = unique_map.get(0);
            if (zero_indices.size() >= 3) {
                main_list.add(Arrays.asList(0, 0, 0));
                return main_list;
            }
        }

        // Step 2: Try all (i, j) pairs, find k such that i ≠ j ≠ k
        for (int i = 0; i < n; i++) {
            int num_i = nums[i];

            for (int j = i + 1; j < n; j++) {
                int num_j = nums[j];
                int required = -(num_i + num_j);

                if (unique_map.containsKey(required)) {
                    for (int index_k : unique_map.get(required)) {
                        if (index_k != i && index_k != j) {
                            List<Integer> sub_list = Arrays.asList(num_i, num_j, nums[index_k]);
                            Collections.sort(sub_list);
                            String key = sub_list.toString();

                            if (!seen.contains(key)) {
                                main_list.add(sub_list);
                                seen.add(key);
                            }
                            break;
                        }
                    }
                }
            }
        }

        return main_list;
    }
}
