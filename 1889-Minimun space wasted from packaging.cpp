class Solution {
public:
    int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
        // Sort the Packages O (n log n)
        // Loop through the Suppliers and sort the box sizes
        // / Check if Package(n-1) > Box(n-1)
        // / Skip that supplier if True for the largest box,
        // / Largest package cannot be placed inside the n-1 box
        // Calculate the Wasted Space for each supplier
        // Example:
        // / packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]

        static const int MOD = 1e9 + 7;

        int n = packages.size();
        sort(packages.begin(), packages.end());

        // Prefix Sum of the packages
        // Example:
        // 3 5 8 10 11 12
        // Prefix P = {0, 3, 8, 16, 26, 37, 49}
        vector<long long> P(n + 1, 0);
        for (int i = 0; i < n; i++) {
            P[i + 1] = P[i] + packages[i];
        }

        long long ans = LLONG_MAX;

        for (auto Box : boxes) {
            sort(Box.begin(), Box.end());
            if (Box.back() < packages.back()) {
                continue;
            }

            long long waste = 0;
            int idx = 0;

            for (int b : Box) {
                if (idx == n) {
                    break;
                }
                int k = upper_bound(packages.begin() + idx, packages.end(), b) -
                        packages.begin();
                long long pkg_count = k - idx;
                long long sum_pkgs = P[k] - P[idx];
                waste += (long long)b * pkg_count - sum_pkgs;
                idx = k;
            }

            // Check if Supplier "i" fit all the packages
            // then update the minimum wasted space
            if (idx == n)
                ans = min(ans, waste);
        }
        if (ans == LLONG_MAX) {
            return -1;
        } else {
            return (int)(ans % MOD);
        }
    }
};
