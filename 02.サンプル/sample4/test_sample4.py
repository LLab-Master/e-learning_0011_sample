import sample4
import doctest

def test_sample4():
    assert sample4.div2(1.2, 0.6) == 2.0

def sample4_zero(): #ゼロで割ったらエラーが出ることを確認したい
        '''引数同士を足して、2倍する
        >>> k = Keisan()
        >>> k.add_number_plus_double('10', '10')
        Traceback (most recent call last):
        ...
        ValueError
        '''
    with pytest.raises(ZeroDivisionError): #ここでエラーキャッチ
        sample4.div2(1.2, 0.0) #ゼロで割る処理

if __name__ == '__main__':
    doctest.testmod()
