class Solution {
public:
    unordered_map<string, vector<string>> adjList;
    vector<string> currPath;
    vector<vector<string>> shortestPaths;

    vector<string> findNeighbors(string &word, unordered_set<string> &wordList) {
        vector<string> neighbors;

        for (int i = 0; i < word.size(); i++) {
            char oldChar = word[i];

            for (char c = 'a'; c <= 'z'; c++) {
                word[i] = c;

                if (c == oldChar || !wordList.count(word)) {
                    continue;
                }
                neighbors.push_back(word);
            }
            word[i] = oldChar;
        }
        return neighbors;
    }

    void backtrack(string &source, string &destination) {
        if (source == destination) {
            shortestPaths.push_back(vector<string>(currPath.rbegin(), currPath.rend()));
        }
        for (int i = 0; i < adjList[source].size(); i++) {
            currPath.push_back(adjList[source][i]);
            backtrack(adjList[source][i], destination);
            currPath.pop_back();
        }
    }

    void bfs(string& beginWord, string& endWord, unordered_set<string>& wordList) {
        queue<string> q;
        q.push(beginWord);

        if (wordList.find(beginWord) != wordList.end()) {
            wordList.erase(wordList.find(beginWord));
        }

        unordered_map<string, int> isEnqueued;
        isEnqueued[beginWord] = 1;

        while (!q.empty()) {
            vector<string> visited;

            for (int i = q.size() - 1; i >= 0; i--) {
                string currWord = q.front();
                q.pop();

                vector<string> neighbors = findNeighbors(currWord, wordList);
                for (auto word : neighbors) {
                    visited.push_back(word);
                    adjList[word].push_back(currWord);

                    if (isEnqueued.find(word) == isEnqueued.end()) {
                        q.push(word);
                        isEnqueued[word] = 1;
                    }
                }
            }
            for (int i = 0; i < visited.size(); i++) {
                if (wordList.find(visited[i]) != wordList.end()) {
                    wordList.erase(wordList.find(visited[i]));
                }
            }
        }
    }

    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string> &wordList) {
        unordered_set<string> copiedWordList(wordList.begin(), wordList.end());
        bfs(beginWord, endWord, copiedWordList);

        currPath = {endWord};
        backtrack(endWord, beginWord);

        return shortestPaths;
    }
};
