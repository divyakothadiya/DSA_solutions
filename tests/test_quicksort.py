from solutions.quicksort import quicksort

def test_quicksort():
    arr = [15, 32, 60, 44, 11, 39]
    expected = sorted(arr)
    quicksort(arr, 0, len(arr) - 1)
    assert arr == expected
    
