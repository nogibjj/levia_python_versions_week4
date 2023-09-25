import pytest
import main
import polars as pl

# Define test cases for calculate_statistics function
def test_calculate_statistics():
    # Create a sample CSV file for testing
    sample_data = pl.DataFrame({
        'danceability': [0.1, 0.1, 0.1],
        'energy': [0.8, 0.7, 0.9],
        'artist_popularity': [80, 70, 90],
        'loudness': [-5, -6, -4]
    })
    sample_data.write_csv('test_data.csv')


    # Test the calculate_statistics function
    result = main.calculate_statistics('test_data.csv')

    # Verify the expected output
    # assert result['mean']['danceability'] == 0.1
    # assert result['median']['danceability'] == 0.1


def teardown():
    import os
    if os.path.exists('test_data.csv'):
        os.remove('test_data.csv')

# Run the tests
if __name__ == "__main__":
    pytest.main()
