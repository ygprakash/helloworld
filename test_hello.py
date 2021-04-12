from simple_server import app

def test_hello():
    response = app.test_client().get('/')
    url_pattern_response = app.test_client().get('/tri')

    assert response.status_code == 200
    #assert str(response.data) == 'hello world, Bravilor Bonamat!! first dayyyyyyyyyyy'
    #
    assert url_pattern_response.status_code == 200
    #assert str(url_pattern_response.data) == 'Bingoooooooooooo. woowwwwwww 2nd page of Bravilor Bonamat!!!!!'
