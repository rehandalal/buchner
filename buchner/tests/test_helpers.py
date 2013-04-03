from nose.tools import eq_


from buchner.helpers import json_requested, jsonify, truthiness


def test_truthiness():
    for s in ('t', 'true', 'TRUE', '1'):
        eq_(truthiness(s), True)

    for s in ('f', 'false', 'FALSE', '0'):
        eq_(truthiness(s), False)

    # TODO: Test funky data


# TODO: Test jsonify


# TODO: Test json_requested
