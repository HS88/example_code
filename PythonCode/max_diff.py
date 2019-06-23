#code
T = int(raw_input());
for i in range(0, T):
    N = int(raw_input());    
    A = str.split(str(raw_input()), " ");
    min_till_date = int(A[0])
    max_local_diff = 0
    max_global_diff = 0
    for j in range(1,N):
        if( int(A[j]) < min_till_date):
            min_till_date = int(A[j])
            if(max_local_diff > max_global_diff):
                max_global_diff = max_min_diff
                max_local_diff = 0
        else:
            if( max_local_diff < ( int(A[j]) - min_till_date) ):
                max_local_diff = int(A[j]) - min_till_date
            if( max_local_diff > max_global_diff):
                max_global_diff = max_local_diff
    print(max_global_diff)