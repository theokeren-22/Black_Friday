```python
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
```


```python
df1 = pd.read_csv('user_demographics.csv')
df2 = pd.read_csv('User_product_purchase_details_p2.csv')
```


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000001</td>
      <td>F</td>
      <td>0-17</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000002</td>
      <td>M</td>
      <td>55+</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000003</td>
      <td>M</td>
      <td>26-35</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000004</td>
      <td>M</td>
      <td>46-50</td>
      <td>7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000005</td>
      <td>M</td>
      <td>26-35</td>
      <td>20</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5886</th>
      <td>1004588</td>
      <td>F</td>
      <td>26-35</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>1004871</td>
      <td>M</td>
      <td>18-25</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>1004113</td>
      <td>M</td>
      <td>36-45</td>
      <td>17</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>1005391</td>
      <td>M</td>
      <td>26-35</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>1001529</td>
      <td>M</td>
      <td>18-25</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>5891 rows × 4 columns</p>
</div>




```python
df1['Age'].unique()
```




    array(['0-17', '55+', '26-35', '46-50', '51-55', '36-45', '18-25'],
          dtype=object)




```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>Product_ID</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000001</td>
      <td>P00069042</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8370</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000001</td>
      <td>P00248942</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>6.0</td>
      <td>14.0</td>
      <td>15200</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000001</td>
      <td>P00087842</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1422</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000001</td>
      <td>P00085442</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>12</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>1057</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000002</td>
      <td>P00285442</td>
      <td>C</td>
      <td>4+</td>
      <td>0</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7969</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>550063</th>
      <td>1006033</td>
      <td>P00372445</td>
      <td>B</td>
      <td>1</td>
      <td>1</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>368</td>
    </tr>
    <tr>
      <th>550064</th>
      <td>1006035</td>
      <td>P00375436</td>
      <td>C</td>
      <td>3</td>
      <td>0</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>371</td>
    </tr>
    <tr>
      <th>550065</th>
      <td>1006036</td>
      <td>P00375436</td>
      <td>B</td>
      <td>4+</td>
      <td>1</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>137</td>
    </tr>
    <tr>
      <th>550066</th>
      <td>1006038</td>
      <td>P00375436</td>
      <td>C</td>
      <td>2</td>
      <td>0</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>365</td>
    </tr>
    <tr>
      <th>550067</th>
      <td>1006039</td>
      <td>P00371644</td>
      <td>B</td>
      <td>4+</td>
      <td>1</td>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>490</td>
    </tr>
  </tbody>
</table>
<p>550068 rows × 9 columns</p>
</div>




```python
modified_df = df2.groupby('User_ID').agg({
    'City_Category': 'first',
    'Stay_In_Current_City_Years': 'first',
    'Marital_Status': 'first',
    'Product_Category_1': 'sum',
    'Product_Category_2': 'sum',
    'Product_Category_3': 'sum',
    'Purchase': 'sum'
}).reset_index()
```


```python
modified_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000001</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>213</td>
      <td>132.0</td>
      <td>148.0</td>
      <td>334093</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000002</td>
      <td>C</td>
      <td>4+</td>
      <td>0</td>
      <td>354</td>
      <td>539.0</td>
      <td>359.0</td>
      <td>810472</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000003</td>
      <td>A</td>
      <td>3</td>
      <td>0</td>
      <td>93</td>
      <td>117.0</td>
      <td>148.0</td>
      <td>341635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000004</td>
      <td>B</td>
      <td>2</td>
      <td>1</td>
      <td>33</td>
      <td>102.0</td>
      <td>127.0</td>
      <td>206468</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000005</td>
      <td>A</td>
      <td>1</td>
      <td>1</td>
      <td>659</td>
      <td>642.0</td>
      <td>207.0</td>
      <td>821001</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5886</th>
      <td>1006036</td>
      <td>B</td>
      <td>4+</td>
      <td>1</td>
      <td>3200</td>
      <td>3403.0</td>
      <td>1509.0</td>
      <td>4116058</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>1006037</td>
      <td>C</td>
      <td>4+</td>
      <td>0</td>
      <td>938</td>
      <td>894.0</td>
      <td>456.0</td>
      <td>1119538</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>1006038</td>
      <td>C</td>
      <td>2</td>
      <td>0</td>
      <td>83</td>
      <td>93.0</td>
      <td>51.0</td>
      <td>90034</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>1006039</td>
      <td>B</td>
      <td>4+</td>
      <td>1</td>
      <td>439</td>
      <td>580.0</td>
      <td>324.0</td>
      <td>590319</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>1006040</td>
      <td>B</td>
      <td>2</td>
      <td>0</td>
      <td>1141</td>
      <td>1110.0</td>
      <td>455.0</td>
      <td>1653299</td>
    </tr>
  </tbody>
</table>
<p>5891 rows × 8 columns</p>
</div>




```python
merged_df = pd.merge(df1, modified_df, on='User_ID')
```


```python
merged_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000001</td>
      <td>F</td>
      <td>0-17</td>
      <td>10</td>
      <td>A</td>
      <td>2</td>
      <td>0</td>
      <td>213</td>
      <td>132.0</td>
      <td>148.0</td>
      <td>334093</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000002</td>
      <td>M</td>
      <td>55+</td>
      <td>16</td>
      <td>C</td>
      <td>4+</td>
      <td>0</td>
      <td>354</td>
      <td>539.0</td>
      <td>359.0</td>
      <td>810472</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000003</td>
      <td>M</td>
      <td>26-35</td>
      <td>15</td>
      <td>A</td>
      <td>3</td>
      <td>0</td>
      <td>93</td>
      <td>117.0</td>
      <td>148.0</td>
      <td>341635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000004</td>
      <td>M</td>
      <td>46-50</td>
      <td>7</td>
      <td>B</td>
      <td>2</td>
      <td>1</td>
      <td>33</td>
      <td>102.0</td>
      <td>127.0</td>
      <td>206468</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000005</td>
      <td>M</td>
      <td>26-35</td>
      <td>20</td>
      <td>A</td>
      <td>1</td>
      <td>1</td>
      <td>659</td>
      <td>642.0</td>
      <td>207.0</td>
      <td>821001</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5886</th>
      <td>1004588</td>
      <td>F</td>
      <td>26-35</td>
      <td>4</td>
      <td>C</td>
      <td>0</td>
      <td>0</td>
      <td>114</td>
      <td>125.0</td>
      <td>20.0</td>
      <td>140990</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>1004871</td>
      <td>M</td>
      <td>18-25</td>
      <td>12</td>
      <td>C</td>
      <td>2</td>
      <td>0</td>
      <td>66</td>
      <td>83.0</td>
      <td>40.0</td>
      <td>108545</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>1004113</td>
      <td>M</td>
      <td>36-45</td>
      <td>17</td>
      <td>C</td>
      <td>3</td>
      <td>0</td>
      <td>79</td>
      <td>119.0</td>
      <td>90.0</td>
      <td>213550</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>1005391</td>
      <td>M</td>
      <td>26-35</td>
      <td>7</td>
      <td>A</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>36.0</td>
      <td>16.0</td>
      <td>60182</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>1001529</td>
      <td>M</td>
      <td>18-25</td>
      <td>4</td>
      <td>C</td>
      <td>4+</td>
      <td>1</td>
      <td>40</td>
      <td>61.0</td>
      <td>96.0</td>
      <td>152942</td>
    </tr>
  </tbody>
</table>
<p>5891 rows × 11 columns</p>
</div>




```python
sample_df = merged_df
```


```python
from sklearn.preprocessing import LabelEncoder
```


```python
label_encoder = LabelEncoder()
sample_df['Gender'] = label_encoder.fit_transform(sample_df['Gender'])
sample_df['Age'] = label_encoder.fit_transform(sample_df['Age'])
sample_df['City_Category'] = label_encoder.fit_transform(sample_df['City_Category'])
```


```python
sample_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000001</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>213</td>
      <td>132.0</td>
      <td>148.0</td>
      <td>334093</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000002</td>
      <td>1</td>
      <td>6</td>
      <td>16</td>
      <td>2</td>
      <td>4+</td>
      <td>0</td>
      <td>354</td>
      <td>539.0</td>
      <td>359.0</td>
      <td>810472</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000003</td>
      <td>1</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>93</td>
      <td>117.0</td>
      <td>148.0</td>
      <td>341635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000004</td>
      <td>1</td>
      <td>4</td>
      <td>7</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>33</td>
      <td>102.0</td>
      <td>127.0</td>
      <td>206468</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000005</td>
      <td>1</td>
      <td>2</td>
      <td>20</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>659</td>
      <td>642.0</td>
      <td>207.0</td>
      <td>821001</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5886</th>
      <td>1004588</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>114</td>
      <td>125.0</td>
      <td>20.0</td>
      <td>140990</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>1004871</td>
      <td>1</td>
      <td>1</td>
      <td>12</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>66</td>
      <td>83.0</td>
      <td>40.0</td>
      <td>108545</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>1004113</td>
      <td>1</td>
      <td>3</td>
      <td>17</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>79</td>
      <td>119.0</td>
      <td>90.0</td>
      <td>213550</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>1005391</td>
      <td>1</td>
      <td>2</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>36.0</td>
      <td>16.0</td>
      <td>60182</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>1001529</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>4+</td>
      <td>1</td>
      <td>40</td>
      <td>61.0</td>
      <td>96.0</td>
      <td>152942</td>
    </tr>
  </tbody>
</table>
<p>5891 rows × 11 columns</p>
</div>




```python
# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = sample_df['Purchase'].quantile(0.25)
Q3 = sample_df['Purchase'].quantile(0.75)
IQR = Q3 - Q1

# Define the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df_no_outliers = sample_df[(sample_df['Purchase'] >= lower_bound) & (sample_df['Purchase'] <= upper_bound)]

df_no_outliers
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000001</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>213</td>
      <td>132.0</td>
      <td>148.0</td>
      <td>334093</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000002</td>
      <td>1</td>
      <td>6</td>
      <td>16</td>
      <td>2</td>
      <td>4+</td>
      <td>0</td>
      <td>354</td>
      <td>539.0</td>
      <td>359.0</td>
      <td>810472</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000003</td>
      <td>1</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>93</td>
      <td>117.0</td>
      <td>148.0</td>
      <td>341635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000004</td>
      <td>1</td>
      <td>4</td>
      <td>7</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>33</td>
      <td>102.0</td>
      <td>127.0</td>
      <td>206468</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000005</td>
      <td>1</td>
      <td>2</td>
      <td>20</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>659</td>
      <td>642.0</td>
      <td>207.0</td>
      <td>821001</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5886</th>
      <td>1004588</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>114</td>
      <td>125.0</td>
      <td>20.0</td>
      <td>140990</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>1004871</td>
      <td>1</td>
      <td>1</td>
      <td>12</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>66</td>
      <td>83.0</td>
      <td>40.0</td>
      <td>108545</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>1004113</td>
      <td>1</td>
      <td>3</td>
      <td>17</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>79</td>
      <td>119.0</td>
      <td>90.0</td>
      <td>213550</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>1005391</td>
      <td>1</td>
      <td>2</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>36.0</td>
      <td>16.0</td>
      <td>60182</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>1001529</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>4+</td>
      <td>1</td>
      <td>40</td>
      <td>61.0</td>
      <td>96.0</td>
      <td>152942</td>
    </tr>
  </tbody>
</table>
<p>5482 rows × 11 columns</p>
</div>




```python
df_no_outliers.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 5482 entries, 0 to 5890
    Data columns (total 11 columns):
     #   Column                      Non-Null Count  Dtype  
    ---  ------                      --------------  -----  
     0   User_ID                     5482 non-null   int64  
     1   Gender                      5482 non-null   int64  
     2   Age                         5482 non-null   int64  
     3   Occupation                  5482 non-null   int64  
     4   City_Category               5482 non-null   int64  
     5   Stay_In_Current_City_Years  5482 non-null   object 
     6   Marital_Status              5482 non-null   int64  
     7   Product_Category_1          5482 non-null   int64  
     8   Product_Category_2          5482 non-null   float64
     9   Product_Category_3          5482 non-null   float64
     10  Purchase                    5482 non-null   int64  
    dtypes: float64(2), int64(8), object(1)
    memory usage: 513.9+ KB
    


```python
df_no_outliers['Stay_In_Current_City_Years'] = df_no_outliers['Stay_In_Current_City_Years'].str.replace('+', '').astype(int)
```


```python
df_no_outliers['Product_Category_1'] = df_no_outliers['Product_Category_1'].fillna(0).astype(int)
df_no_outliers['Product_Category_2'] = df_no_outliers['Product_Category_2'].fillna(0).astype(int)
df_no_outliers['Product_Category_3'] = df_no_outliers['Product_Category_3'].fillna(0).astype(int)
```


```python
df_no_outliers
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User_ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Marital_Status</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
      <th>Purchase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000001</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>213</td>
      <td>132</td>
      <td>148</td>
      <td>334093</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000002</td>
      <td>1</td>
      <td>6</td>
      <td>16</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>354</td>
      <td>539</td>
      <td>359</td>
      <td>810472</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000003</td>
      <td>1</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>93</td>
      <td>117</td>
      <td>148</td>
      <td>341635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000004</td>
      <td>1</td>
      <td>4</td>
      <td>7</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>33</td>
      <td>102</td>
      <td>127</td>
      <td>206468</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000005</td>
      <td>1</td>
      <td>2</td>
      <td>20</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>659</td>
      <td>642</td>
      <td>207</td>
      <td>821001</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5886</th>
      <td>1004588</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>114</td>
      <td>125</td>
      <td>20</td>
      <td>140990</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>1004871</td>
      <td>1</td>
      <td>1</td>
      <td>12</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>66</td>
      <td>83</td>
      <td>40</td>
      <td>108545</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>1004113</td>
      <td>1</td>
      <td>3</td>
      <td>17</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>79</td>
      <td>119</td>
      <td>90</td>
      <td>213550</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>1005391</td>
      <td>1</td>
      <td>2</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>36</td>
      <td>16</td>
      <td>60182</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>1001529</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>1</td>
      <td>40</td>
      <td>61</td>
      <td>96</td>
      <td>152942</td>
    </tr>
  </tbody>
</table>
<p>5482 rows × 11 columns</p>
</div>




```python
df_no_outliers.to_csv('model.csv', index=False)
```


```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
```


```python
x = df_no_outliers[['Age', 'City_Category', 'Stay_In_Current_City_Years', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3']]
y = df_no_outliers['Purchase']
```


```python
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2, random_state = 42)
```


```python
dt = DecisionTreeRegressor()
```


```python
dt.fit(xtrain, ytrain)
```




<style>#sk-container-id-5 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: black;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-5 {
  color: var(--sklearn-color-text);
}

#sk-container-id-5 pre {
  padding: 0;
}

#sk-container-id-5 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-5 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-5 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-5 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-5 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-5 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-5 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-5 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-5 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-5 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-5 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-5 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-5 label.sk-toggleable__label {
  cursor: pointer;
  display: block;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
}

#sk-container-id-5 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-5 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-5 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-5 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-5 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-5 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-5 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-5 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-5 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-5 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-5 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-5 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-5 div.sk-label label.sk-toggleable__label,
#sk-container-id-5 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-5 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-5 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-5 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-5 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-5 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-5 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-5 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-5 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 1ex;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-5 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-5 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-5 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-5 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-5" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>DecisionTreeRegressor()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-5" type="checkbox" checked><label for="sk-estimator-id-5" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;&nbsp;DecisionTreeRegressor<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.5/modules/generated/sklearn.tree.DecisionTreeRegressor.html">?<span>Documentation for DecisionTreeRegressor</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></label><div class="sk-toggleable__content fitted"><pre>DecisionTreeRegressor()</pre></div> </div></div></div></div>




```python
ypred_dt = dt.predict(xtest)
```


```python
mean_squared_error(ytest, ypred_dt, squared = False)
```




    np.float64(183346.83728026864)




```python
r2_score(ytest, ypred_dt)
```




    0.8942172263012904




```python
mean_absolute_error(ytest, ypred_dt)
```




    np.float64(124439.05104831359)




```python
dt.predict([[2,1,2,380,628,485]])
```




    array([1015469.])




```python
xtest[:7]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>City_Category</th>
      <th>Stay_In_Current_City_Years</th>
      <th>Product_Category_1</th>
      <th>Product_Category_2</th>
      <th>Product_Category_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>343</th>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>380</td>
      <td>628</td>
      <td>485</td>
    </tr>
    <tr>
      <th>33</th>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>718</td>
      <td>808</td>
      <td>395</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>355</td>
      <td>430</td>
      <td>194</td>
    </tr>
    <tr>
      <th>2257</th>
      <td>6</td>
      <td>2</td>
      <td>3</td>
      <td>114</td>
      <td>253</td>
      <td>176</td>
    </tr>
    <tr>
      <th>2265</th>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>114</td>
      <td>94</td>
      <td>45</td>
    </tr>
    <tr>
      <th>3020</th>
      <td>6</td>
      <td>2</td>
      <td>3</td>
      <td>75</td>
      <td>75</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3882</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>149</td>
      <td>140</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




```python
ytest[:7]
```




    343     920708
    33      821303
    8       594099
    2257    243214
    2265    144223
    3020    186272
    3882    287340
    Name: Purchase, dtype: int64




```python
rf = RandomForestRegressor(n_estimators = 500, random_state=42)
```


```python
rf.fit(xtrain, ytrain)
```




<style>#sk-container-id-6 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: black;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-6 {
  color: var(--sklearn-color-text);
}

#sk-container-id-6 pre {
  padding: 0;
}

#sk-container-id-6 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-6 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-6 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-6 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-6 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-6 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-6 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-6 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-6 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-6 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-6 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-6 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-6 label.sk-toggleable__label {
  cursor: pointer;
  display: block;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
}

#sk-container-id-6 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-6 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-6 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-6 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-6 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-6 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-6 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-6 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-6 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-6 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-6 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-6 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-6 div.sk-label label.sk-toggleable__label,
#sk-container-id-6 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-6 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-6 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-6 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-6 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-6 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-6 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-6 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-6 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 1ex;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-6 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-6 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-6 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-6 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-6" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>RandomForestRegressor(n_estimators=500, random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-6" type="checkbox" checked><label for="sk-estimator-id-6" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;&nbsp;RandomForestRegressor<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestRegressor.html">?<span>Documentation for RandomForestRegressor</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></label><div class="sk-toggleable__content fitted"><pre>RandomForestRegressor(n_estimators=500, random_state=42)</pre></div> </div></div></div></div>




```python
ypred_rf = rf.predict(xtest)
```


```python
mean_squared_error(ytest, ypred_rf, squared=False)
```




    np.float64(139399.04023725065)




```python
r2_score(ytest, ypred_rf)
```




    0.9388512375552188




```python
rf.predict([[2,0,4,149,140,90]])
```




    array([253897.838])




```python

```
