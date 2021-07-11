echo "Stop crawler"
ps -ef | grep main.py | grep -v grep | awk '{print $2}' | xargs kill
ps -ef | grep all_in_one | grep -v grep | awk '{print $2}' | xargs kill