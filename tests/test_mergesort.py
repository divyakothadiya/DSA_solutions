from solutions.mergesort import mergesort

def test_mergesort():
    arr = [15, 32, 60, 44, 11, 39]
    expected = sorted(arr)
    mergesort(arr, 0, len(arr) - 1)
    assert arr == expected